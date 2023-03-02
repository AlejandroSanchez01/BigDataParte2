import json
from urllib.request import urlopen
import boto3

def f(event, context):
    # TODO implement
    with urlopen("https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario") as response:
        body = response.read()
    client = boto3.client("s3")
    client.put_object(Body = body, Bucket = "dolar-raw-2023", Key = "dolar_timestamp.txt")
    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda!")
    }