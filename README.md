# Realtime Severless Analysis of Yahoo Finance Stock Data
*****************

## Data Collector
********************

#### Lambda Function URL 
- [x] [API Endpoint](www.google.com)



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


## Data Tranformer
********************
#### AWS Kinesis Firehouse Delivery Stream 
- [x] Monitoring Page  




## Data Analyzer
********************
- [x] `query.sql`

```
!#usr/bin/env SQL

```

- [x] `results.csv`




```
docker build -t local_lambda .
docker run -v $(pwd):/app local_lambda python lambda_function.py

docker build -t deployment -f Dockerfile.deployment_artifact .
docker run -v $(pwd):/app/artifact deployment
```
