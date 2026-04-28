import sys, os, requests, zipfile, subprocess, hashlib, time
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QLabel
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QPixmap

import winshell
from win32com.client import Dispatch

# CONFIGURACIÓN
USER = "monicodes-hub"
REPO = "EasyRS"
URL_JSON = f"https://raw.githubusercontent.com/{USER}/{REPO}/main/version.json?v={int(time.time())}"
EXE_PRINCIPAL = "EasyRS.exe"

def resource_path(relative_path):
    """ Obtiene la ruta absoluta al recurso, funciona para dev y para PyInstaller """
    try:
        # PyInstaller crea una carpeta temporal y guarda la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class UpdateWorker(QThread):
    progress = Signal(int)
    status = Signal(str)
    finished = Signal(bool)

    def crear_accesos_directos(self):
        """Crea accesos directos robustos usando el icono embebido en el EXE."""
        try:
            if getattr(sys, 'frozen', False):
                launcher_path = sys.executable
            else:
                launcher_path = os.path.abspath(__file__)
            
            desktop = winshell.desktop()
            start_menu = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs")
            
            for location in [desktop, start_menu]:
                shortcut_path = os.path.join(location, "EasyRS.lnk")
                shell = Dispatch('WScript.Shell')
                shortcut = shell.CreateShortCut(shortcut_path)
                
                if not launcher_path.endswith(".exe"):
                    shortcut.Targetpath = sys.executable.replace("python.exe", "pythonw.exe")
                    shortcut.Arguments = f'"{launcher_path}"'
                else:
                    shortcut.Targetpath = launcher_path
                    # USAMOS EL PROPIO EXE COMO FUENTE DEL ICONO
                    shortcut.IconLocation = launcher_path 
                
                shortcut.WorkingDirectory = os.path.dirname(launcher_path)
                shortcut.Description = "Lanzador de EasyRS"
                shortcut.save()
        except Exception as e:
            print(f"Error en accesos directos: {e}")

    def run(self):
        try:
            response = requests.get(URL_JSON, timeout=5)
            data = response.json()
            remote_version = data['version']
            
            local_version = "0.0.0"
            if os.path.exists("version.txt"):
                with open("version.txt", "r") as f:
                    local_version = f.read().strip()

            if remote_version > local_version:
                self.status.emit(f"Actualizando a v{remote_version}...")
                r = requests.get(data['url'], stream=True)
                total_size = int(r.headers.get('content-length', 0))
                downloaded = 0
                with open("update.zip", "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            self.progress.emit(int(downloaded * 100 / total_size))

                with open("update.zip", "rb") as f:
                    if hashlib.sha256(f.read()).hexdigest() != data['sha256']:
                        raise Exception("Error de integridad")

                with zipfile.ZipFile("update.zip", 'r') as zip_ref:
                    zip_ref.extractall(".")
                
                with open("version.txt", "w") as f:
                    f.write(remote_version)
                os.remove("update.zip")
            
            self.status.emit("Verificando accesos directos...")
            self.crear_accesos_directos()
            
            self.status.emit("Iniciando aplicación...")
            time.sleep(1) 
            self.finished.emit(True)
        except Exception as e:
            print(f"Error: {e}")
            self.finished.emit(True)

class LauncherUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(400, 300)
        
        self.container = QWidget(self)
        self.container.setFixedSize(400, 300)
        self.container.setStyleSheet("""
            QWidget { 
                background-color: #2b2b2b; 
                border-radius: 15px;
                border: 1px solid #444;
            }
            QLabel { color: #ffffff; border: none; font-family: 'Segoe UI'; }
            QProgressBar {
                border: 1px solid #555;
                border-radius: 5px;
                text-align: center;
                height: 10px;
                background-color: #1a1a1a;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0078d7, stop:1 #00c6ff);
                border-radius: 5px;
            }
        """)
        
        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # LOGO USANDO RESOURCE_PATH
        self.logo = QLabel()
        ruta_icono = resource_path("icon.ico")
        if os.path.exists(ruta_icono):
            pixmap = QPixmap(ruta_icono).scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.logo.setPixmap(pixmap)
        self.logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.logo)
        
        self.title = QLabel("EasyRS")
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; margin-top: 10px;")
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)
        
        layout.addStretch()
        
        self.lbl_status = QLabel("Buscando actualizaciones...")
        self.lbl_status.setStyleSheet("font-size: 13px; color: #aaa;")
        layout.addWidget(self.lbl_status)
        
        self.pbar = QProgressBar()
        self.pbar.setValue(0)
        layout.addWidget(self.pbar)
        
        self.thread = UpdateWorker()
        self.thread.progress.connect(self.pbar.setValue)
        self.thread.status.connect(self.lbl_status.setText)
        self.thread.finished.connect(self.launch)
        self.thread.start()

    def launch(self):
        ruta_directa = EXE_PRINCIPAL
        ruta_carpeta = os.path.join("EasyRS", EXE_PRINCIPAL)
        if os.path.exists(ruta_directa):
            subprocess.Popen([ruta_directa])
        elif os.path.exists(ruta_carpeta):
            subprocess.Popen([ruta_carpeta], cwd="EasyRS")
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = LauncherUI()
    ui.show()
    sys.exit(app.exec())