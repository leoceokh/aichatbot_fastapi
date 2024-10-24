<script>
    import { onMount } from 'svelte';
  
    let messages = [];
    let input = '';
  
    async function handleSubmit() {
      if (input.trim() === '') return;
  
      const newMessages = [...messages, { role: 'user', content: input }];
      messages = newMessages;
      input = '';
  
      try {
        const response = await fetch('http://localhost:8000/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ messages: newMessages }),
        });
        const data = await response.json();
        messages = [...messages, { role: 'assistant', content: data.response }];
      } catch (error) {
        console.error('Error:', error);
        messages = [...messages, { role: 'system', content: '오류가 발생했습니다. 다시 시도해 주세요.' }];
      }
    }
  
    function endChat() {
      messages = [];
    }
  
    onMount(() => {
      const chatMessages = document.getElementById('chat-messages');
      if (chatMessages) {
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
    });
  </script>
  
  <main>
    <div class="chat-container">
      <h1>오은영 박사 AI 상담소</h1>
      <div id="chat-messages">
        {#each messages as message}
          <div class="message {message.role}">{message.content}</div>
        {/each}
      </div>
      <form on:submit|preventDefault={handleSubmit}>
        <input type="text" bind:value={input} placeholder="고민을 입력하세요..." />
        <div class="button-container">
          <button type="submit">전송</button>
          <button type="button" on:click={endChat}>상담 종료</button>
        </div>
      </form>
    </div>
  </main>
  
  <style>
    .chat-container {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
    }
  
    #chat-messages {
      height: 400px;
      overflow-y: auto;
      border: 1px solid #ccc;
      padding: 10px;
      margin-bottom: 20px;
    }
  
    .message {
      margin-bottom: 10px;
      padding: 5px;
      border-radius: 5px;
    }
  
    .user {
      background-color: #e6f3ff;
      text-align: right;
    }
  
    .assistant {
      background-color: #f0f0f0;
    }
  
    form {
      display: flex;
      flex-direction: column;
      margin-bottom: 20px;
    }
  
    input {
      padding: 5px;
      margin-bottom: 10px;
    }
  
    .button-container {
      display: flex;
      justify-content: space-between;
    }
  
    button {
      padding: 5px 10px;
    }
  </style>
  