import socket
import time

class casoNoLoginEnvioPack():
    def __init__(self):
        self.hostname, self.port = '192.168.15.62', 1050
        # create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect the client
        # client.connect((target, port))
        self.client.connect((self.hostname, self.port))

    def sendNoLogin_And_LocationPack(self):
        # send some data, Mensaje de tipo Location Data
        pack = b'78781F120B081D112E10CC027AC7EB0C46584900148F01CC00287D001FB8000380810D0A'
        self.client.send(pack)
        # receive the response data (4096 is recommended buffer size)
        response = self.client.recv(4096)
        print (response)
