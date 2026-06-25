from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from backend.agent import support_agent
import asyncio

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Customer Support Agent Running"}

@app.post("/chat")
async def chat(request: ChatRequest):

    response = support_agent(request.message)

    return {"response": response}

@app.post("/stream")
async def stream_chat(request: ChatRequest):

    response = support_agent(request.message)

    async def generate():

        for word in response.split():
            yield word + " "
            await asyncio.sleep(0.1)

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )