from __future__ import print_function
from .event_handler import event_handler

def lambda_handler(event, context):
    for record in event['Records']:
        event_handler(record)
        payload = record["body"]
        print(str(payload))
