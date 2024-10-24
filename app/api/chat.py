from fastapi import APIRouter, Depends
from app.schemas.chat import ChatRequest, ChatResponse
from app.domain.chatbot import Chatbot
from app.domain.youtube_recommender import YouTubeRecommender

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, chatbot: Chatbot = Depends(Chatbot), youtube_recommender: YouTubeRecommender = Depends(YouTubeRecommender)):
    response = chatbot.get_response(request.messages)
    videos = youtube_recommender.get_recommendations(response)
    return ChatResponse(response=response, videos=videos)
