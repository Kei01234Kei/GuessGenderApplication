from fastapi import FastAPI
from handler import handler

app = FastAPI()

handler.handler(app)
