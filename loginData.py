class LoginData(object):

	
	def __init__(self,infCont):
		self.procesar(infCont)

	def procesar(self,infCont):
	    self.terminalID=infCont

	def information(self):
	    return 'Login Message Packet \nInformation \nTerminal ID IMEI number: ' + self.terminalID +"\n¡QUAK!"

