from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

class Video(BaseModel):
    title: str
    videoId: str
    thumbnail: str

class ChatResponse(BaseModel):
    response: str
    videos: List[Video]
