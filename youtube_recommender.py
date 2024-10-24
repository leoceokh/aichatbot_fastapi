from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

class YouTubeRecommender:
    def __init__(self):
        api_key = os.getenv("YOUTUBE_API_KEY")
        if not api_key:
            logging.error("YouTube API key is missing")
            raise ValueError("YouTube API key is not set")
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_recommendations(self, query):
        try:
            logging.info(f"Searching for videos with query: {query}")
            search_response = self.youtube.search().list(
                q=query + " 오은영 박사 고민상담",
                type='video',
                part='id,snippet',
                maxResults=3,
                channelId="UCLQBi5_bI85hqEWGHJkwrHw"  # @play-channelA의 채널 ID
            ).execute()

            videos = []
            for search_result in search_response.get('items', []):
                video = {
                    'title': search_result['snippet']['title'],
                    'videoId': search_result['id']['videoId'],
                    'thumbnail': search_result['snippet']['thumbnails']['default']['url']
                }
                videos.append(video)
            logging.info(f"Found {len(videos)} videos: {videos}")
            return videos
        except Exception as e:
            logging.error(f"YouTube API 오류: {e}")
            return []
