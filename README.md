# Realtime Severless Analysis of Yahoo Finance Stock Data
*****************

### Data Collector
********************

#### Lambda Function URL 
- [x]



#### Lambda Fucntion Source Code 
- [x] `data_collector.py`


```
!#usr/bin/env python 


```


### Data Tranformer
********************
#### AWS Kinesis Firehouse Delivery Stream 
- [x] Monitoring Page  




### Data Analyzer
********************
- [x] `query.sql

```
!#usr/bin/env SQL

```

- [x] `results.csv




```
docker build -t local_lambda .
docker run -v $(pwd):/app local_lambda python lambda_function.py

docker build -t deployment -f Dockerfile.deployment_artifact .
docker run -v $(pwd):/app/artifact deployment
```


### Requirements.txt
`yfinance==0.1.54`


```python
import boto3
import os
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')
import yfinance 

def lambda_handler(event, context):
    pass



```




















