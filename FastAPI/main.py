from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}
    
@app.get("/url")
async def show_url():
    return {"url":"https://localhost"}