from time import sleep

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def slow_root():
    sleep(7)
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8004)

