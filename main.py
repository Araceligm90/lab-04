from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "Welcome to my API"}

@app.get("/greeting/{name}")
def greetings(name: str):
    current_date = datetime.now().strftime("%Y- %m- %d %H:%M")
    return {
        "message": f"Hello {name}, today is {current_date}"
    }
    
@app.get("/textlen/{text}")
def text_length(text: str):
    return{
        "text": text,
        "length": len(text) 
        }

