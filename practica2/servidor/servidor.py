import time
import os

# Rutas 
BASE = os.path.join(os.path.dirname(__file__), '..', 'comunicacion')
ENTRADA = os.path.join(BASE, 'entrada_servidor.txt')
SALIDA  = os.path.join(BASE, 'salida_servidor.txt')

ultimo_mensaje = ""  

def procesar_mensaje(mensaje):
    """
    Procesamiento del mensaje:
    - Convierte a mayúsculas
    - Invierte el texto
    - Cuenta los caracteres
    """
    mayusculas = mensaje.upper()
    invertido  = mensaje[::-1]
    longitud   = len(mensaje)
    resultado  = (
        f"[SERVIDOR PROCESÓ]\n"
        f"  Original   : {mensaje}\n"
        f"  Mayúsculas : {mayusculas}\n"
        f"  Invertido  : {invertido}\n"
        f"  Longitud   : {longitud} caracteres\n"
        f"  Timestamp  : {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
    )
    return resultado

def iniciar_servidor():
    global ultimo_mensaje
    print("=" * 45)
    print("  SERVIDOR ACTIVO - Sistemas Distribuidos")
    print("=" * 45)
    print(f"  Escuchando en: {ENTRADA}")
    print(f"  Respondiendo en: {SALIDA}")
    print("  Presiona Ctrl+C para detener\n")

    while True:
        try:
            with open(ENTRADA, 'r', encoding='utf-8') as f:
                contenido = f.read().strip()

            if contenido and contenido != ultimo_mensaje:
                print(f"[+] Nuevo mensaje recibido: '{contenido}'")
                resultado = procesar_mensaje(contenido)

                with open(SALIDA, 'w', encoding='utf-8') as f:
                    f.write(resultado)

                print(f"[✓] Respuesta escrita en salida_servidor.txt\n")
                ultimo_mensaje = contenido 

        except FileNotFoundError:
            print("[!] Archivos de comunicación no encontrados.")
            print("    Asegúrate de que existan en ../comunicacion/")

        time.sleep(1) 

if __name__ == "__main__":
    iniciar_servidor()
