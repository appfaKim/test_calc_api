from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from router import test

app = FastAPI(title="테스트 중 입니다.")

origins = [
    "http://127.0.0.1:8080",    # 또는 "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return "home"

@app.get('/hello')
def hello():
    return {"message": "hello world"}

app.include_router(test.router, tags=['test'])

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
