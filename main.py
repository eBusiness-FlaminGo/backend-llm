import http
import sys

from llm import FunFactGenerator
from fastapi import FastAPI

app = FastAPI()

ffg = FunFactGenerator()


@app.get("/", status_code=http.HTTPStatus.NOT_FOUND)
async def root():
    return {"message": "Nothing here!"}


@app.get("/fun-fact", status_code=http.HTTPStatus.OK)
async def generate_fun_fact(category :str = None):
    if category:
        response = await ffg.llm_categories(category)
    else:
        response = await ffg.llm()
    return {"message": response}


def main():
    print("Hello from backend-llm!")


if __name__ == "__main__":
    main()
