from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hi():
    return "{'hi':'this is just fastapi and uvicorn'}"