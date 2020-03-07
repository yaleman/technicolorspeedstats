#!/usr/bin/env python3


from datetime import datetime
from time import sleep
from json import dumps
from technicolorspeedstats import get_data

LOGFILE = 'logfile.txt'
LOG_TIMER = 300 # seconds

while True:
    data = get_data()
    data['timestamp'] = str(datetime.now())
    
    with open(LOGFILE, 'a') as fh:
        fh.write(dumps(data))
    print(dumps(data))
    sleep(LOG_TIMER)