# Practica 2 - Arquitectura de Sistemas Distribuidos

Simulacion de comunicacion entre un cliente y un servidor usando archivos de texto como canal. Los dos componentes corren de forma independiente y solo se "hablan" a traves de dos archivos compartidos.



# Estructura del proyecto


practica2/

├── comunicacion/

│   ├── entrada_servidor.txt 

│   └── salida_servidor.txt

├── servidor/

│   └── servidor.py

└── cliente/

   └── cliente.py



# Como iniciarlo

Necesitas dos terminales abiertas al mismo tiempo.


**Terminal 1**


cd ~/practica2/servidor
python3 servidor.py


**Terminal 2**


cd ~/practica2/cliente
python3 cliente.py



Escribe un mensaje en el cliente y el servidor lo va a procesar y devolver la respuesta.



# Notas

* Siempre arrancar el servidor antes que el cliente

  
* Si el cliente no recibe respuesta, verificar que el servidor este corriendo


* Este modelo no soporta multiples clientes al mismo tiempo (un cliente pisaria el mensaje del otro)
