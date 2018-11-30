import socket
import time

class casoLoginSpam():
    def __init__(self):
        self.hostname, self.port = '192.168.15.62', 1050
        # create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect the client
        # client.connect((target, port))
        self.client.connect((self.hostname, self.port))

    def spam(self):
        while True:
            # send some data
            pack = b'78780D01012345678901234500018CDD0D0A'
            self.client.send(pack)
            # receive the response data (4096 is recommended buffer size)
            response = self.client.recv(4096)
            print (response)
            time.sleep(1)
