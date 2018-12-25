import socket

def main():
	try:
		print('Please specify connection details')
		host = str(input('IP Address: '))
		port = int(input('Port: '))	
		print('Starting connection')
		
		mySocket = socket.socket()
		mySocket.connect((host, port))
		print('Client connected')
		
		
		while True:
			print()
			serverData = mySocket.recv(64).decode()
			print('Received from server: ' + serverData)
			print()
			
			fileName = input('Reply -> ')
			mySocket.send(fileName.encode())
			print()
			
			try:
				if '.zip' in fileName or '.jpg' in fileName or '.png' in fileName or '.exe' in fileName:
					f = open(fileName,'r+b')
					print('Opening binary file')
					
					print('Sending binary data')
					fileData = f.read(1024)
					while (fileData):
						mySocket.send(fileData)
						fileData = f.read(1024)
					print('File sent!')
						
				if '.py' in fileName or '.txt' in fileName:
					f = open(fileName, 'r', encoding = 'utf-8')
					
					print('Sending text data')
					fileData = f.read(1024)
					print(fileData)
					while (fileData):
						mySocket.sendall(fileData.encode())
						fileData = f.read(1024)
					print('File sent!')
					
			finally:
				f.close()
				break
				
	except Exception as e:
		print(e)
		print('Client stopped with an error')
	finally:
		mySocket.close()
		print('Client stopped')

if __name__ == '__main__' : main()
