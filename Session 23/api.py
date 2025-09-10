from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "Bine ai venit!"

@app.get('/salut')
def hello():
    return "Salut, utilizatorule!"