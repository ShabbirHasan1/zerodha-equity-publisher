import json
import os
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen, Request
from django.core.cache import caches
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def downloadAndLoadToRedis():
    print("Running Cron Job")    # do your thing here
    # f = open('/home/allen/cronjob.txt', 'a')
    f = open(os.path.join(BASE_DIR, 'cronjob.log'), 'a')
    
    try:
        today = date.today().strftime("%d%m%y")
        ZERODHA_URL = 'https://bseindia.com/download/bhavcopy/equity/eq' + today + '_csv.zip'
        req = Request(ZERODHA_URL, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urlopen(req)
        zipfile = ZipFile(BytesIO(resp.read()))
        
        redis_cache = caches['default']
        redis_client = redis_cache.client.get_client()

        lines = zipfile.open('EQ' + today + '.CSV').readlines()
        for i in range(1, len(lines)):

            line = lines[i].decode('utf-8').split(',')
            code = line[0] 
            name = line[1] 
            openn = line[4] 
            high = line[5] 
            low = line[6] 
            close = line[7]

            equity = {
                'code': code.rstrip(),
                'name': name.rstrip().upper(),
                'open': openn.rstrip(),
                'high': high.rstrip(),
                'low': low.rstrip(),
                'close': close.rstrip()
            }
            # redis_client.hset('bhavcopy', 'equities', json.dumps(equities))
            redis_client.hmset(name, equity)
        today = date.today().strftime("%d - %m - %y")
        redis_client.hmset('lastUpdated', {'lastUpdated': today})
        f.writelines('Data pull success on ' + today + '\n')

    except Exception as e:
        today = date.today().strftime("%d - %m - %y")
        f.writelines('Data pull failed on ' + today + '. Error Captured : ' + str(e) + '\n')
    f.close()

