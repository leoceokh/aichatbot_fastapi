from googleapiclient.discovery import build
from app.core.config import settings

class YouTubeRecommender:
    def __init__(self):
        self.youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

    def get_recommendations(self, query):
        try:
            search_response = self.youtube.search().list(
                q=query + " 오은영 박사 고민상담",
                type='video',
                part='id,snippet',
                maxResults=3
            ).execute()

            videos = []
            for search_result in search_response.get('items', []):
                video = {
                    'title': search_result['snippet']['title'],
                    'videoId': search_result['id']['videoId'],
                    'thumbnail': search_result['snippet']['thumbnails']['default']['url']
                }
                videos.append(video)
            return videos
        except Exception as e:
            print(f"YouTube API 오류: {e}")
            return []
