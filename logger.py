#!/usr/bin/env python3


from datetime import datetime
from time import sleep
from json import dumps
from technicolorspeedstats import get_data

LOGFILE = 'logfile.txt'

while True:
    data = get_data()
    data['timestamp'] = str(datetime.now())
    
    with open(LOGFILE, 'a') as fh:
        fh.write(dumps(data))
    print(dumps(data))
    sleep(60)