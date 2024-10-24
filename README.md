bash 
git clone https://github.com/leoceokh/aichatbot_fastapi.git 
cd aichatbot_fastapi 
python -m venv venv 
source venv/bin/activate # Windows: venv\Scripts\activate 
pip install -r requirements.txt 

2. 환경설정
- `.env.example` → `.env` 복사
- API 키 설정 필요:
  - OPENAI_API_KEY
  - YOUTUBE_API_KEY
3. 실행
4. bash
uvicorn app.main:app --reload

## 디자인 가이드
### 색상
- 메인: #007AFF
- 배경: #f5f5f5
- 텍스트: #333333

### 레이아웃
- 모바일 우선 (최대 너비 430px)
- 채팅창 중앙 정렬
- 반응형 디자인 (480px 브레이크포인트)

### 주요 컴포넌트
- 헤더 (상단 고정)
- 채팅 영역 (스크롤)
- 입력창 (하단 고정)
- 유튜브 추천 섹션

## 주의사항
- `.env` 파일 깃허브 업로드 금지
- 모바일 환경 우선 고려

![image](https://github.com/user-attachments/assets/4645f100-a199-4a7d-bb62-18957ced2e81)
