import sys
import os
import shutil
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QFileDialog, QMessageBox
)
from PySide6.QtCore import QTimer
from interface.ui_mainwindow import Ui_MainWindow
from interface.ui_conversations import Ui_Dialog as Ui_ConversationsDialog
from interface.ui_routing import Ui_Dialog as Ui_RoutingDialog
import resources_mainwindow_rc
import resources_conversations_rc
import resources_routing_rc
import conversations
import routing
import re

def get_downloads_folder():
    if sys.platform == "win32":
        import ctypes
        from ctypes import wintypes, windll

        _SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
        _SHGetKnownFolderPath.argtypes = [
            ctypes.c_void_p, wintypes.DWORD, wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)
        ]

        # FOLDERID_Downloads from KnownFolders.h
        FOLDERID_Downloads = ctypes.c_char_p(b'{374DE290-123F-4565-9164-39C4925E467B}')
        path_ptr = ctypes.c_wchar_p()
        result = _SHGetKnownFolderPath(FOLDERID_Downloads, 0, 0, ctypes.byref(path_ptr))
        if result == 0:
            downloads = path_ptr.value
            ctypes.windll.ole32.CoTaskMemFree(path_ptr)
            return downloads
        else:
            # fallback to home directory
            return os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        return os.path.join(os.path.expanduser("~"), "Downloads")

class ConversationsDialog(QDialog, Ui_ConversationsDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Connect your custom buttons to accept/reject
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_values(self):
        agent = self.select_agent.currentText()
        # Return conv_mode as string, to match conversations.py logic
        mode = "1" if self.conversations_all.isChecked() else "2"
        return agent, mode

class RoutingDialog(QDialog, Ui_RoutingDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Connect your custom buttons to accept/reject
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_rp_ids(self):
        return [val.strip() for val in self.routingID_input.text().split(",") if val.strip()]

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Connect your main window buttons here
        self.pushButton.clicked.connect(self.close)  # Exit button
        self.pushButton_2.clicked.connect(self.handle_routing)
        self.pushButton_3.clicked.connect(self.handle_conversations)

    def select_file(self, title, filter_str=None):
        default_dir = "C:/ipdialbox/rep/"
        if not os.path.exists(default_dir):
            default_dir = os.path.expanduser("~")
        # Always show all files, HTML, and CSV
        if filter_str is None:
            filter_str = "All Files (*);;HTML Files (*.html);;CSV Files (*.csv)"
        file_path, _ = QFileDialog.getOpenFileName(self, title, default_dir, filter_str)
        return file_path

    def handle_conversations(self):
        file_path = self.select_file("Selecciona archivo de conversaciones")
        if not file_path:
            return
        import pandas as pd
        try:
            if file_path.lower().endswith(".html"):
                df = pd.read_html(file_path)[0]
            elif file_path.lower().endswith(".csv"):
                # Try comma, then semicolon
                try:
                    df = pd.read_csv(file_path)
                except pd.errors.ParserError:
                    df = pd.read_csv(file_path, sep=";")
            else:
                QMessageBox.critical(self, "Error", "Formato de archivo no soportado.")
                return
            if "CHANNEL" not in df.columns:
                QMessageBox.critical(self, "Error", "No se encontraron agentes en la columna CHANNEL.")
                return
            # Extract only agent names using regex, just like in reports_gui_ps.py
            agent_pattern = re.compile(r"AGENT:\s*([^,]+)")
            agent_names = set()
            for val in df["CHANNEL"].astype(str):
                for match in agent_pattern.findall(val):
                    agent_names.add(match.strip())
            agent_names = sorted(agent_names)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error leyendo el archivo:\n{e}")
            return

        dlg = ConversationsDialog(self)
        dlg.select_agent.addItems(agent_names)
        if dlg.exec():
            agent_name, conv_mode = dlg.get_values()
            try:
                conversations.main(file_path, agent_name, conv_mode)
                downloads = get_downloads_folder()
                pdf_folder = "chats_filtrados_pdf"
                found = False
                for f in os.listdir(pdf_folder):
                    if agent_name.replace(" ", "_") in f and f.endswith(".pdf"):
                        src = os.path.join(pdf_folder, f)
                        dst = os.path.join(downloads, f)
                        shutil.copy(src, dst)
                        QMessageBox.information(self, "Éxito", f"¡PDF generado con éxito!\nGuardado en:\n{dst}")
                        found = True
                        break
                if not found:
                    QMessageBox.warning(self, "Advertencia", "¡PDF generado, pero no se encontró el archivo esperado para copiar a Descargas!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrió un error en Conversaciones:\n{e}")

    def handle_routing(self):
        file_path = self.select_file("Selecciona archivo de routing")
        if not file_path:
            return
        dlg = RoutingDialog(self)
        if dlg.exec():
            rp_id_list = dlg.get_rp_ids()
            if not rp_id_list:
                QMessageBox.warning(self, "Advertencia", "No se ingresaron RP_IDs.")
                return
            try:
                routing.main(file_path, rp_id_list)
                downloads = get_downloads_folder()
                pdf_folder = "reportes_filtrados_pdf"
                # Ensure the output folder exists
                if not os.path.exists(pdf_folder):
                    os.makedirs(pdf_folder)
                found = False
                pdfs_copied = []
                for f in os.listdir(pdf_folder):
                    if f.endswith(".pdf"):
                        src = os.path.join(pdf_folder, f)
                        dst = os.path.join(downloads, f)
                        shutil.copy(src, dst)
                        pdfs_copied.append(dst)
                if pdfs_copied:
                    msg = "¡PDF(s) generado(s) con éxito!\nGuardado(s) en:\n" + "\n".join(pdfs_copied)
                    QMessageBox.information(self, "Éxito", msg)
                else:
                    QMessageBox.warning(self, "Advertencia", "¡PDF generado, pero no se encontró el archivo esperado para copiar a Descargas!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrió un error en Routing:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())