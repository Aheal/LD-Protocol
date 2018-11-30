import sys
import socket
import time
import os
import logging 
import Main
#import main from protocolo
 
 
#configuracion UDP
udp_ip = "192.168.15.62"
udp_port = 1050
udp_max_size = 65507

#ubicacion del archivo de registros
dirLogs = "/home/andriuxboy/Documents/git/protocol/LD-Protocol/logs"
 
# Primero nos aseguramos de cerrar cualquier ejecucion anterior de este servicio que pueda estar abierto 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#linea para terminar el protocolo
line = b'bye'
sock.sendto(line, (udp_ip, udp_port))
#Hacemos un delay de 10 segundos para que se cierre correctamente el servicio anterior
time.sleep(2)

#Ejecutamos el servicio 
try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind((udp_ip, udp_port))
 
    code=''

    while code!='bye':
        code, addr = socket.recvfrom(udp_max_size)
        if code!='bye':
            if (len(code) > 10):
                #main del protocolo
                respuesta = Main.LittlestDuck(code)
                print(respuesta)
                #guardar archivo
                logging.basicConfig(filename="LD.log", level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
                f= open("LDlog.txt","a")
                time.sleep(1)
                #escribir respuesta
                logging.debug(respuesta)           
except Exception as e:
    print(e)
    print(os.getcwd())
    print("directorio arriba mencionado")
    sys.exit(1)
