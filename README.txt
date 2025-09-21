# Easy RepSift (EasyRS)

**EasyRS** is a desktop application developed in Python with a Qt interface (PySide6 and Qt Designer), designed to generate PDF files from HTML data. The tool allows filtering and organizing key information, streamlining daily tasks for the **Easydona** team within **Nextclinics Spain**.

> ⚠️ Internal use only: authorized members of Easydona / Nextclinics Spain.

---

# Easy RepSift (EasyRS)

**EasyRS** es una aplicación de escritorio desarrollada en Python con interfaz Qt (PySide6 y Qt Designer), cuyo objetivo es generar archivos PDF a partir de datos HTML. La herramienta permite filtrar y organizar información clave, agilizando tareas diarias del equipo **Easydona**, dentro de **Nextclinics Spain**.

> ⚠️ Uso exclusivo para miembros autorizados del equipo Easydona / Nextclinics Spain.

---

## Features / Características

- Intuitive graphical interface with selection buttons (`QRadioButton`) and custom styles (QSS).  
- Fast and organized HTML to PDF conversion.  
- Smooth user experience powered by PySide6.  
- Standalone executable packaged with PyInstaller for internal distribution.  
- Interactive installer created with Inno Setup, including app icon and license.

- Interfaz gráfica intuitiva con botones de selección (`QRadioButton`) y estilos personalizados (QSS).  
- Conversión rápida y organizada de datos HTML a PDF.  
- Experiencia de usuario fluida gracias a PySide6.  
- Ejecutable independiente empaquetado con PyInstaller para distribución interna.  
- Instalador interactivo creado con Inno Setup, incluyendo ícono y licencia.

---

## Installation / Instalación

The application is distributed internally via an installer. To install:

1. Run the `EasyRS_Installer.exe`.  
2. Accept the internal-use license.  
3. Follow the installation steps.

La aplicación se distribuye internamente mediante un instalador. Para instalar:

1. Ejecuta el archivo `EasyRS_Instalador.exe`.  
2. Acepta la licencia de uso interno.  
3. Sigue los pasos del asistente de instalación.

---

## Development Requirements / Requisitos para desarrollo

- Python 3.10+  
- PySide6  
- PyInstaller (to package the application)  
- Inno Setup (to generate the installer, optional)