from fastapi import FastAPI  # type: ignore

app = FastAPI()

# Business logic as standalone functions
def get_root_message():
    return {"message": "Hello World"}

def calculate_addition(num1: int, num2: int):
    return {"result": num1 + num2}

def calculate_substract(num1: int, num2: int):
    return {"result": num1 - num2}

# FastAPI routes
@app.get("/")
async def root():
    return get_root_message()

@app.get("/addition/{num1}/{num2}")
async def addition(num1: int, num2: int):
    return calculate_addition(num1, num2)

@app.get("/substract/{num1}/{num2}")
async def addition(num1: int, num2: int):
    return calculate_addition(num1, num2)
