# Realtime Severless Analysis of Yahoo Finance Stock Data
*****************

## Data Collector
********************

#### Lambda Function URL 
- [x] [API Endpoint](www.google.com)



#### Lambda Fucntion Source Code 
- [x] `data_collector.py`


```
!#usr/bin/env python 
import boto3
import os
import subprocess
import sys
import json

print('Loading function')

subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')

import yfinance as yf

tk = ['FB', 'SHOP',
      'BYND', 'NFLX', 'PINS',
      'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']


def lambda_handler(event, context):   
    tk_list = tk.split()
    fire = boto3.client("firehose", "us-east-1")    
    for i in tk_list:
	data = yf.download(tk, start="2020-05-14", end="2020-05-15", interval = "1m",group_by = 'ticker')
        for datetime, rows in data[i].iterrows():
            jsonstr = json.dumps({"high": rows.High, "low": rows.Low, "ts": str(datetime), 'name': i})
            fire.put_record(DeliveryStreamName="DataStreaming", Record={"Data": jsonstr.encode('utf-8')})

    return {
        'statusCode': 200,
        'body': json.dumps(f'Completed! Data Recorded into your bucket')
        }

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
