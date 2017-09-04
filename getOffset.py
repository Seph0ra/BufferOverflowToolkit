#!/usr/bin/python
from sys import argv
import subprocess
if len(argv) != 2:
	print "Usage: getOffset.py [size]"
	exit(0)
ADDRESS = argv[1]
try:
	OFFSET = subprocess.Popen(["/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb", "-q", ADDRESS], stdout=subprocess.PIPE)
	OUTPUT = OFFSET.stdout.read()
	print "[x] {}".format(OUTPUT)
except:
	print "[!] Unable to get offset"
