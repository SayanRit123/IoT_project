from flask import Flask, jsonify
import boto3
from boto3.dynamodb.conditions import Key
from flask_cors import CORS # type: ignore
import time

app = Flask(__name__)
CORS(app)  # To allow frontend JS to access this API

session = boto3.Session(
    aws_access_key_id='AKIAS2RBT7PDOMXMH6OM',
    aws_secret_access_key='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',
    region_name='us-east-1'
)

# Initialize DynamoDB client
dynamodb = session.resource('dynamodb', region_name='us-east-1')  # e.g. 'ap-south-1'
table = dynamodb.Table('Machine_data')  # Replace with your actual table name

@app.route('/', methods=['GET'])
def get_vehicles():
    try:
        # Scan all data (for demo purpose – use filters in real usage)
        response = table.scan()
        items = response.get('Items', [])
        return jsonify(items)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True,port=5000)
