from fastapi import FastAPI, APIRouter

app = FastAPI()
api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """

    :return:
    """
    return {"msg": "Angstgegner"}

@api_router.get("/data/{input}")
def get_some_data(input: str) -> dict:
    """

    :param input: something to return
    :return: input
    """
    result = {4711: input}
    return result

app.include_router(api_router)


