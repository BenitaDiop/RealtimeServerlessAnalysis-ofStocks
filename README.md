# Realtime Severless Analysis of Yahoo Finance Stock Data
*****************

## Data Collector
********************

#### Lambda Function URL 
- [x] [API Endpoint](https://vlmmfo9shb.execute-api.us-east-1.amazonaws.com/default/DataCollector)



#### Lambda Fucntion Source Code 
- [x] `data_collector.py`


```python
from datetime import date
import json
import boto3
import os
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')

import yfinance as yf
def lambda_handler(event, context):
    stocks=['FB','SHOP', 'BYND', 'NFLX', 'PINS', 'SQ' ,'TTD', 'OKTA' ,'SNAP', 'DDOG'] 
    def get_js(high,low,ts,name):
        return json.dumps({'high':high,'low':low,'ts':str(ts),'name':name})
        fh=boto3.client("firehose", "us-east-2")
        data=yf.download(tickers='FB SHOP BYND NFLX PINS SQ TTD OKTA SNAP DDOG', start="2020-05-14", end="2020-05-15",interval = "1m",group_by='tickers')
        output=data.melt(value_vars =stocks,var_name=['Symbol'])
        output=data.unstack().unstack(level=1).reset_index(level=1, drop=False).rename_axis('names').reset_index() 
        output['js']=data.apply(lambda x:get_js(x['High'],x['Low'],x['Datetime'],x['names']),axis=1) 
        
        
        for i in output['js'].values:
            fh.put_record(DeliveryStreamName="stream", Record={"Data": i.encode('utf-8')}) 
            
    return { 'statusCode': 200, 'body': json.dumps(f'Ok!') }
        

```

![](https://github.com/BenitaDiop/RealtimeServerlessAnalysis-ofStocks/blob/master/assets/datcollector.png)



## Data Tranformer
********************
#### AWS Kinesis Firehouse Delivery Stream 
- [x] Monitoring Page  

![](https://github.com/BenitaDiop/RealtimeServerlessAnalysis-ofStocks/blob/master/assets/watch.png)


## Data Analyzer
********************
- [x] `query.sql`

```
!#usr/bin/env SQL

```

- [x] `results.csv`




```json
Name	High	Hour	Timestamp	     Recurrence
BYND	137.97	09	05/14/2020 09:39:00	1
BYND	139.56	10	05/14/2020 10:31:00	1
BYND	141.0	11	05/14/2020 11:15:00	1
BYND	138.24	12	05/14/2020 12:57:00	1
BYND	137.79	13	05/14/2020 13:00:00	1
BYND	135.73	14	05/14/2020 14:12:00	1
BYND	135.85	15	05/14/2020 15:54:00	1
DDOG	67.25	09	05/14/2020 09:32:00	1
DDOG	66.55	10	05/14/2020 10:09:00	1
DDOG	65.0	11	05/14/2020 11:05:00	4
```
