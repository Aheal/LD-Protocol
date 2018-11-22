
import socket
import sys
 
#configuracion UDP
udp_id = "192.168.15.62"
udp_port = 1050
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
line=''
print ("Escribe 'bye' en una linea para que terminen ambos programas")
while line!='bye':
    line=input(' # ')
    linebytes = line.encode()
    sock.sendto(linebytes, (udp_id, udp_port))
    