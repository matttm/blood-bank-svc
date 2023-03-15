from __future__ import print_function
import services

def lambda_handler(event, context):
    for record in event['Records']:
        services.event_handler.event_handler(record)
        payload = record["body"]
        print(str(payload))
