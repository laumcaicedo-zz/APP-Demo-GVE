from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from flask import Flask

app = Flask(__name__)

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
   def default(self, o):
       if isinstance(o, decimal.Decimal):
           if o % 1 > 0:
               return float(o)
           else:
               return int(o)
       return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('photos')

response = table.scan()


@app.route('/app')
def hello_world():
    for i in response['Items']:
        text += str(i['content']) + '<br/>'

    return (text)

if __name__ == '__main__':
   app.run(port=3000,host='0.0.0.0')
