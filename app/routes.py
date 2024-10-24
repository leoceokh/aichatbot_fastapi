from fastapi import APIRouter, Request, Body, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.domain.chatbot import Chatbot
from app.domain.youtube_service import YouTubeService

router = APIRouter()
chatbot = Chatbot()
youtube_service = YouTubeService()
templates = Jinja2Templates(directory="templates")

class ChatMessage(BaseModel):
    message: str

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/chat")
async def chat(chat_message: ChatMessage = Body(...)):
    try:
        user_message = chat_message.message
        response = chatbot.get_response([{"role": "user", "content": user_message}])
        return JSONResponse(content={"response": response})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/youtube_recommendations")
async def get_youtube_recommendations(chat_message: ChatMessage = Body(...)):
    try:
        query = chat_message.message
        videos = youtube_service.search_videos(query)
        return JSONResponse(content={"videos": videos})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/end_consultation")
async def end_consultation():
    return JSONResponse(content={"response": "상담이 종료되었습니다. 이용해 주셔서 감사합니다."})
