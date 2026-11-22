from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}


# pip install fastapi uvicorn
# uvicorn zad_1:app --reload
# http://127.0.0.1:8000
