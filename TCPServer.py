import socket

def main():
	
	count = 0
	port = int(input('Choose a port: '))
	try:
		mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mySocket.bind(('0.0.0.0',port))
		
		print('Listening for connection...')
		mySocket.listen(1)
		print()
		
		while True:
			conn, addr = mySocket.accept()
			print('Connected to %s' % str(addr))
			print()
			data = 'Please send full name of file including file extension'
			conn.send(data.encode())
			fileName = conn.recv(512).decode()
			print('Receiving %s from connected client' % fileName)
			print()
			
			#for binary -- .jpg, .exe, etc.
			try:
				if '.zip' in fileName or '.jpg' in fileName or '.png' in fileName or '.exe' in fileName:
					
					f = open(fileName,'w+b')
					print('Opening binary file')
					
					print('Writing')
					fileData = conn.recv(1024)
					while (fileData):
						f.write(fileData)
						fileData = conn.recv(1024)
						
						count += 1
						if count == 1000:
							print('This file is greater than 1MB')
						if count == 54000:
							print('This file is greater than 50MB!')
							
					print('Received')
						
			except Exception as e:
				print(e)
				print('write failed in binary')
			
			#for text -- .txt, .py	
			try:
				if '.py' in fileName or '.txt' in fileName:
					print('In txt')
					
					f = open(fileName,'w',encoding = 'utf-8')
					print('Opening txt file')
						
					fileData = conn.recv(1024).decode()
					while (fileData):
						print('Writing')
						f.write(fileData)
						fileData = conn.recv(1024).decode()
						
			except Exception as e:
				print(e)
				print('write failed in text')
			finally:
				f.close()
			
			print('Process completed')
			print()
			break
			
	except Exception as e:
		print(e)
		print('Server closed')
	finally:
		print('Connection shutting down')
		conn.shutdown(socket.SHUT_RDWR)
		print('Connection closing')
		conn.close()
		quit()

if __name__ == "__main__": main()
