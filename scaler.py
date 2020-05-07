#!/bin/python
import os
stream = os.popen('docker service ls')
output = stream.read()
lines = output.splitlines()
for l in lines:
    cols = l.split()
    if cols[1].endswith("_app") and ("1" in cols[3]):
        prompt = "Scale service " + cols[1] + "?"
	reply = str(raw_input(prompt + ' y/n:')).lower().strip()
        if reply[0] == 'y':
            command = "docker service scale " + cols[1] + "=2"
	    os.system(command)
        else:
            continue
