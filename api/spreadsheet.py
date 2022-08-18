import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_ENDPOINT = os.getenv('API_ENDPOINT')

headers = {"content-type": "application/json"}
r = requests.get(API_ENDPOINT, headers=headers)
data = r.json()

# スプレッドシートからsatisfactionの値をリストとして引っ張り出す
def get_satisfaction():
    output = []
    for d in data:
        output.append(d["satisfaction"])
    print(output)
    return output

def get_label():
    output = []
    for d in data:
        output.append(f"{d['id']}: {d['title']}")
    print(output)
    return output
