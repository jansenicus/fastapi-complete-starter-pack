import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.index:api", host="localhost", port=8000, log_level="info")
