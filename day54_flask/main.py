# Just playing around with the difference between requests and httpx
# import requests
# from icecream import ic

# r = requests.get("https://www.google.com")
# ic(r)
# ic(r.status_code)


# import httpx

# r = httpx.get("https://www.google.com")
# ic(r)
# ic(r.status_code)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'