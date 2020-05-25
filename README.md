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
