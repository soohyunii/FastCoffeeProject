from fastapi import FastAPI
from params import *

app = FastAPI()

@app.get("/")
async def root():
	return {"message":"Hello World"}


@app.post("/form_receiver")
async def form_receiver(params: Params):
	return params

