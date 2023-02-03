from fastapi import FastAPI
import base64

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hola Mundo" }

@app.get("/url")
async def url():
    return { "url": "https://mouredev.com/puthon" }

@app.get("/decode/")
async def decode():
    code = base64.b64encode(b"Jose Castro")
    decode = base64.b64decode(code)
    return {"Code": code, "Decode": decode}