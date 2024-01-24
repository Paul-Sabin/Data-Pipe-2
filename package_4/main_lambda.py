import os
import requests
from dotenv import load_dotenv
import urllib3
# import json

def get_data_lambda(event, context):
    load_dotenv("C:\Asus WebStorage\psabin@gmail.com\MySyncFolder\Data Science Course\_offline\.env") #If this returns False, you can specify path to the .env inside the brackets
    BASE_URL = "https://cloud.iexapis.com/stable/stock/tsla/previous?"
    API_KEY = os.getenv('IEX_API_KEY') #Best way. Can save many API keys in one file and reference them.
    url = f"{BASE_URL}token={API_KEY}"
    response = requests.get(url)
    values = response.json()
    return values
