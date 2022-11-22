from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
	return {"message":"Hello World"}


@app.post("/form_receiver")
async def form_receiver():
	return {"title":'hi', "author":'iii'}

