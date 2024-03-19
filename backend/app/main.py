from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import chatgpt

app = FastAPI()

# Set all origins wildcard ("*") for demonstration purposes only. Specify your domain in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Request(BaseModel):
    prompt: str
    temperature: float = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ask")
def read_item(req: Request):
    return {"response": chatgpt.get_completion_text(req.prompt)}