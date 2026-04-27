import sys
import os
import requests
import zipfile
import subprocess
import hashlib
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QLabel
from PySide6.QtCore import Qt, QThread, Signal

# Configuración: Reemplaza con tus datos reales de GitHub
USER = "monicodes-hub"
REPO = "https://github.com/monicodes-hub/EasyRS"
URL_JSON = f"https://raw.githubusercontent.com/{USER}/{REPO}/main/version.json"
EXE_PRINCIPAL = "EasyRS.exe"

class UpdateWorker(QThread):
    progress = Signal(int)
    status = Signal(str)
    finished = Signal(bool)

    def run(self):
        try:
            # 1. Comprobar actualización
            self.status.emit("Buscando actualizaciones...")
            response = requests.get(URL_JSON, timeout=5)
            data = response.json()
            remote_version = data['version']
            
            local_version = "0.0.0"
            if os.path.exists("version.txt"):
                with open("version.txt", "r") as f:
                    local_version = f.read().strip()

            if remote_version > local_version:
                self.status.emit(f"Descargando v{remote_version}...")
                
                # 2. Descarga
                r = requests.get(data['url'], stream=True)
                total_size = int(r.headers.get('content-length', 0))
                downloaded = 0
                
                with open("update.zip", "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            self.progress.emit(int(downloaded * 100 / total_size))

                # 3. Seguridad: Verificar SHA-256
                self.status.emit("Verificando integridad...")
                with open("update.zip", "rb") as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()
                
                if file_hash != data['sha256']:
                    raise Exception("Fallo de seguridad: Hash no coincide")

                # 4. Instalación
                self.status.emit("Instalando mejoras...")
                with zipfile.ZipFile("update.zip", 'r') as zip_ref:
                    zip_ref.extractall(".")
                
                with open("version.txt", "w") as f:
                    f.write(remote_version)
                os.remove("update.zip")
                
            self.finished.emit(True)
        except Exception as e:
            print(f"Error: {e}")
            self.finished.emit(True) # Intentar abrir la app de todos modos

class LauncherUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EasyRS Updater")
        self.setFixedSize(350, 120)
        # Diseño elegante y oscuro
        self.setStyleSheet("""
            QWidget { background-color: #1e1e1e; color: white; font-family: Segoe UI; }
            QProgressBar { border: 2px solid #3d3d3d; border-radius: 5px; text-align: center; }
            QProgressBar::chunk { background-color: #0078d7; }
        """)
        
        layout = QVBoxLayout()
        self.lbl_status = QLabel("Iniciando...")
        self.pbar = QProgressBar()
        layout.addWidget(self.lbl_status)
        layout.addWidget(self.pbar)
        self.setLayout(layout)

        self.thread = UpdateWorker()
        self.thread.progress.connect(self.pbar.setValue)
        self.thread.status.connect(self.lbl_status.setText)
        self.thread.finished.connect(self.launch_main_app)
        self.thread.start()

    def launch_main_app(self):
        if os.path.exists(EXE_PRINCIPAL):
            subprocess.Popen([EXE_PRINCIPAL])
        else:
            print("Error: No se encuentra el ejecutable principal.")
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = LauncherUI()
    ui.show()
    sys.exit(app.exec())