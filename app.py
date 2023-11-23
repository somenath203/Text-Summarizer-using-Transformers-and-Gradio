from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


summarizer = pipeline('summarization')


class InputTextModel(BaseModel):
    text: str


@app.get('/')
def welcome():
    return {
        'success': True,
        'message': 'server of "text summarization using transformer" is up and running successfully.'
    }


@app.post('/summarize-text')
async def summarize_text(textInput: InputTextModel):
    return {
        'success': True,
        'message': 'okkk'
    }
