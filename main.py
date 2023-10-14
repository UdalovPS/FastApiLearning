"""Start module in app"""
import uvicorn
from fastapi import FastAPI

#create FastApi app
app = FastAPI()


@app.get("/")
def hello(name: str):
    return f"Hello {name}"


if __name__ == '__main__':
    #run app
    uvicorn.run(app, host="0.0.0.0", port=8000)
