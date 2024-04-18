from fastapi import FastAPI
from calculator_core.calculator import Calculator
import random
import uvicorn


app = FastAPI()
calculator = Calculator()


@app.get("/calculate")
def calculate():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(["add", "subtract", "multiply", "divide"])

    match operation:
        case "add":
            result = calculator.add(num1, num2)
        case "subtract":
            result = calculator.subtract(num1, num2)
        case "multiply":
            result = calculator.multiply(num1, num2)
        case "divide":
            result = calculator.divide(num1, num2)

    response = {"num1": num1, "num2": num2, "operation": operation, "result": result}

    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
