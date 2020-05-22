# RealtimeStockDataServerlessAnalysis


### Docker
```
docker build -t local_lambda .
docker run -v $(pwd):/app local_lambda python lambda_function.py

docker build -t deployment -f Dockerfile.deployment_artifact .
docker run -v $(pwd):/app/artifact deployment
```


### Requirements.txt
`yfinance==0.1.54`























