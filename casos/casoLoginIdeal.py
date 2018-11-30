import socket
import time

class casoLoginIdeal():
    def __init__(self):
        self.hostname, self.port = '192.168.15.62', 1050
        # create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect the client
        # client.connect((target, port))
        self.client.connect((self.hostname, self.port))

    def sendChido(self):
        # send some data
        pack = b'78780D01012345678901234500018CDD0D0A'
        self.client.send(pack)
        # receive the response data (4096 is recommended buffer size)
        response = self.client.recv(4096)
        print (response)
        time.sleep(1)

        #Location Data
        pack = b'78780D0101234567890178781F120B081D112E10CC027AC7EB0C46584900148F01CC00287D001FB8000380810D0A234500018CDD0D0A'
        self.client.send(pack)
        response = self.client.recv(4096)
        print (response)
        time.sleep(1)

        #Alarm Data
        pack = b'787825160B0B0F0E241DCF027AC8870C4657E60014020901CC00287D001F726506040101003656A40D0A'
        self.client.send(pack)
        response = self.client.recv(4096)
        print (response)
        time.sleep(1)

        #Status Data
        pack = b'78780A134B040300010011061F0D0A'
        self.client.send(pack)
        response = self.client.recv(4096)
        print (response)
        time.sleep(1)