import time
import os

# Rutas
BASE    = os.path.join(os.path.dirname(__file__), '..', 'comunicacion')
ENTRADA = os.path.join(BASE, 'entrada_servidor.txt')
SALIDA  = os.path.join(BASE, 'salida_servidor.txt')

LATENCIA = 2  

def limpiar_salida():
    """Limpia la respuesta anterior para no leer datos viejos."""
    with open(SALIDA, 'w', encoding='utf-8') as f:
        f.write("")

def enviar_mensaje(mensaje):
    with open(ENTRADA, 'w', encoding='utf-8') as f:
        f.write(mensaje)
    print(f"[→] Mensaje enviado al servidor.")

def esperar_respuesta():
    print(f"[…] Esperando respuesta ({LATENCIA}s de latencia simulada)...")
    time.sleep(LATENCIA)

    with open(SALIDA, 'r', encoding='utf-8') as f:
        respuesta = f.read().strip()

    return respuesta

def iniciar_cliente():
    print("=" * 45)
    print("  CLIENTE - Sistemas Distribuidos")
    print("=" * 45)
    print("  Escribe 'salir' para terminar\n")

    while True:
        mensaje = input("Ingresa un mensaje: ").strip()

        if mensaje.lower() == 'salir':
            print("Cliente cerrado.")
            break

        if not mensaje:
            print("[!] Mensaje vacío, intenta de nuevo.\n")
            continue

        limpiar_salida()          
        enviar_mensaje(mensaje)   # escribir en entrada_servidor.txt
        respuesta = esperar_respuesta()  # leer desde salida_servidor.txt

        if respuesta:
            print("\n--- Respuesta del Servidor ---")
            print(respuesta)
            print("------------------------------\n")
        else:
            print("[!] No se recibió respuesta. ¿Está el servidor activo?\n")

if __name__ == "__main__":
    iniciar_cliente()
