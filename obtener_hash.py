import hashlib
import os

# CAMBIA ESTO por el nombre exacto que ves en tu carpeta
nombre_archivo = "dist/EasyRS/v.1.0.0.zip" 

def calcular_hash(archivo):
    if not os.path.exists(archivo):
        print(f"❌ ERROR: El archivo '{archivo}' no está en esta carpeta.")
        print(f"📂 Archivos que SÍ veo aquí: {os.listdir('.')}")
        return None
        
    sha256_hash = hashlib.sha256()
    with open(archivo, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            sha256_hash.update(bloque)
    return sha256_hash.hexdigest()

resultado = calcular_hash(nombre_archivo)
if resultado:
    print(f"✅ HASH SHA-256:\n{resultado}")