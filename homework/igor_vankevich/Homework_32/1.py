from datetime import datetime
import requests

while True:
    requests.get('https://www.google.com')
    print(datetime.now())
