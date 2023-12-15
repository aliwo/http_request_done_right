import time

import requests
from flask import Flask

app = Flask(__name__)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/req")
def req():
    print(f"요청 들어옴 {time.time():.3f}")
    response = requests.get("http://localhost:8004")
    return {"message": f"request finished: {response.json()}"}


@app.get("/req500")
def req_500():
    return {"message": f"Hello"}

