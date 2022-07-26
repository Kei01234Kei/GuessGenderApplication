from typing import Union
from fastapi import status
from fastapi.responses import JSONResponse
from controller import controller


def handler(app):
    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.get("/hello/{name}")
    async def say_hello(name: str):
        return {"message": f"Hello {name}"}

    @app.get("/api")
    async def api(name: Union[str, None] = None):
        res = controller.get_gender(name)
        if res:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=res
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=None
            )
