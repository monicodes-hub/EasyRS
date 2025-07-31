# Easy RepSift (EasyRS)

**EasyRS** es una aplicación de escritorio desarrollada en Python con interfaz Qt (Qt Designer) cuyo objetivo es generar archivos PDF a partir de datos HTML. La herramienta permite filtrar y organizar información clave para agilizar el trabajo diario del equipo Easydona, parte de Nextclinics Spain.

## Características

- Interfaz gráfica amigable con botones de selección (QRadioButton)
- Conversión de datos HTML a PDF
- Estilo visual personalizado con QSS
- Empaquetado en ejecutable (.exe) mediante PyInstaller
- Instalador interactivo creado con Inno Setup

## Instalación

Esta aplicación es distribuida de forma interna mediante un instalador. Para instalar:

1. Ejecuta el archivo `EasyRS_Instalador.exe`
2. Acepta la licencia de uso interno
3. Sigue los pasos de instalación

> ⚠️ **Uso exclusivo** para miembros autorizados del equipo Easydona / Nextclinics Spain.

## Requisitos para desarrollo

- Python 3.10+
- PySide6
- PyInstaller
- Inno Setup (solo para empaquetado del instalador)

Instala las dependencias con:

```bash
pip install -r requirements.txt
