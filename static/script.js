const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const chatMessages = document.getElementById('chat-messages');
const videoRecommendations = document.getElementById('video-recommendations');
const endChatButton = document.getElementById('end-chat');

let messages = [];

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const userMessage = userInput.value.trim();
    if (userMessage) {
        addMessage('user', userMessage);
        userInput.value = '';
        messages.push({role: 'user', content: userMessage});
        
        const response = await sendMessage(messages);
        addMessage('assistant', response.response);
        messages.push({role: 'assistant', content: response.response});
        
        displayVideoRecommendations(response.videos);
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const endChatButton = document.getElementById('end-chat');
    if (endChatButton) {
        endChatButton.addEventListener('click', () => {
            console.log("상담 종료 버튼 클릭됨");
            messages = [];
            chatMessages.innerHTML = '';
            videoRecommendations.innerHTML = '';
            // 상담 종료 메시지 제거
        });
    } else {
        console.error("상담 종료 버튼을 찾을 수 없습니다.");
    }
});

async function sendMessage(messages) {
    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ messages }),
    });
    return response.json();
}

function addMessage(role, content) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', role);
    messageElement.textContent = content;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function displayVideoRecommendations(videos) {
    videoRecommendations.innerHTML = '';
    if (videos && videos.length > 0) {
        const header = document.createElement('h2');
        header.textContent = '관련 영상 추천';
        videoRecommendations.appendChild(header);
        
        videos.forEach(video => {
            const videoElement = document.createElement('div');
            videoElement.classList.add('video-item');
            videoElement.innerHTML = `
                <img src="${video.thumbnail}" alt="${video.title}">
                <a href="https://www.youtube.com/watch?v=${video.videoId}" target="_blank">${video.title}</a>
            `;
            videoRecommendations.appendChild(videoElement);
        });
    } else {
        console.log("No videos found");
    }
}
