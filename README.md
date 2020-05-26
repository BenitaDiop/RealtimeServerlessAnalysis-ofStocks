# Realtime Severless Analysis of Yahoo Finance Stock Data
*****************
A Kinesis Firehose Delivery Stream, DataTransformer, that has a lambda function which transforms records and streams it into an S3 bucket. Another Lambda function, DataCollector, that is triggered from a simple URL call and grabs stock price data and places it into the delivery defined in the DataTransformer. Configure AWS Glue to point to the S3 Bucket. To interactively query the S3 files, DataAnalyzer,  using AWS Athena to gain insight into our streamed data. 


## Data Collector
********************

#### Lambda Function URL 
- [x] [API Endpoint](https://vlmmfo9shb.execute-api.us-east-1.amazonaws.com/default/DataCollector)



#### Lambda Fucntion Source Code 
- [x] `data_collector.py`



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
