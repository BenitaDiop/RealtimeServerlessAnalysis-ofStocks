#!usr/bin/env python 

# import json 

# def lambda_handler(event, context):
#    return {
#        'statusCode': 200, 
#        'body': json.dumps('Hello From AWS Lambda!')
# }


import json 

def lambda_handler(event, context):
    output_records = [] 
		for record in event["records"]: 
			print(type(record['data']))
			print(record['data']))
			output_records.append({
						"recordID": record['recordID],
						"result": "OK",
						"data": record['data']
			
			})
print(len(ouput_records))
return {"records": output_records}


import base64 
base64.b64encode(b'\n')

# docker run -it python:3.7



import json 

def lambda_handler(event, context):
    output_records = [] 
		for record in event["records"]: 
		output_records.append({
				"recordID": record['recordID'], 
				"result": "OK", 
				"data": record['data'] + "Cg=="})
				
return {"records": output_records}




import json 
import boto3 
import random 

CHOICES = ["Technology", "Energy", "Fianncial"]

data = {"ticker_symbol":"HJK", 
					"sector":random.choice(CHOICES), "change":0.04, "price":4.79}
					
					as_jsonstr = json.dumps(data) 
					fh = boto3.client("firehouse", "us-east-2") 
					
					
					fh.put_record(
								DeliveryStreamName="test-delivery-stream", 
								Record=('Data': as.jsonstr.encode('utf-8')))
								
								
								return {
								'statusCode': 200, 
								'body': json.dumps(f'Done! Recorded: {as_jsonstr}'}}
