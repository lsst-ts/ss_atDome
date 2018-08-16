import socket               # Import socket module
import domeSimulatorController

host = "localhost"		    # local machine name
port = 50000                # Reserve a port for your service.

def createServer():
	s = socket.socket()         # Create a socket object
	s.settimeout(5)
	s.bind((host, port))        # Bind to the port
	s.listen(5)                 # Now wait for client connection.
	c, addr = s.accept()     # Establish connection with client.
	print(addr)
	#print("Got connection from: "+addr)
	return c, addr
	   
def disconnectServer(c):
	c.close()
	
def execSimulator(c, addr):
	dome = domeSimulatorController.DomeSimulator()
	while True:
		messageReceived = c.recv(1024).decode('ascii', 'ignore').strip()
		print(messageReceived)
		if(messageReceived=='?' or messageReceived=='+' or messageReceived=='CFR' or messageReceived=='HELP'):
			messageToSend = dome.queryStatus(messageReceived)+"\r\n"
			#print(messageToSend)
			c.sendall(messageToSend.encode())
		else:
			dome.executeCommand(messageReceived)

	
while True:
	
	c, addr = createServer()
	execSimulator(c, addr)
