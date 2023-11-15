from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello_world():
    return 'Hello, World!'

@app.get('/test/')
def test():
    return 'pssst, hier wird getestet!'