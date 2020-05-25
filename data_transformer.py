def lambda_handler(event, context): 
  output_records = [] 
  for record in event["records"]: 
      output_records.append({
          "recordId": record["recordIId"], 
          "result": "Ok", 
          "data":record["data"] + "Cg=="
          })
          
      return {"records":output_records}
