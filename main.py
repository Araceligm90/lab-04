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

@app.get("/add")
def add(num1: int, num2: int):
    return {"result": num1 + num2}

@app.get("/subtract")
def subtract(num1: int, num2: int):
    return {"result": num1 - num2} 
    

@app.get("/multiply")
def multiply(num1: int, num2: int):
    return {"result": num1 * num2} 

@app.get("/divide")
def divide(num1: int, num2: int):
  if num2 == 0:
    return {"error: cannot divide by 0"}
  return {"result": num1 // num2}


## uvicorn main:app --reload <-- to reload page 
