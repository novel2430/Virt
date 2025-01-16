<script setup>
  import TopBar from '@/components/NavTopBar.vue'
  import MsgCard from '@/components/MsgCard.vue'
</script>

<template>
  <!-- Top Bar -->
  <TopBar title="咨询"/>
  <!-- Main Area -->
  <v-main class="main">
    <v-container style="padding-bottom: 30vh;">
      <v-row
        v-for="n in messages"
        :key="n"
      >
        <v-col>
          <MsgCard
            :icon="n.icon"
            :isAi="n.isAi"
            :content="n.content"
          />
        </v-col>
      </v-row>
      <!-- 👇 Element created at the bottom -->
      <div ref="bottomEl"></div>
    </v-container>
    <!-- 输入框和发送按钮 -->
    <div class="input-container" >
      <v-container>
        <v-sheet
          rounded="xl"
          class="input-sheet"
          :elevation="10"
        >
        <v-row dense>
          <v-textarea
            v-model="newMessage"
            label="输入消息"
            variant="outlined"
            rows="1"
          ></v-textarea>
        </v-row>
        <v-row dense style="justify-content: center;">
          <v-btn class="input-btn" @click="sendMessage">发送</v-btn>
        </v-row>
        </v-sheet>
      </v-container>
    </div>
  </v-main>
</template>

<script>
  export default {
    data: () => ({ 
      newMessage: "",
      sessionId: "",
      apiHost: "https://www.yejsgk.top/ff",
      messages: [
        {
          content: "今天有什么疑问吗？",
          isAi: true,
        },
      ],
    }),
    methods: {
      addMessage(msg) {
        this.messages.push(msg);
      },
      scrollToBottom() {
        this.$nextTick(() => {
          this.$refs.bottomEl?.scrollIntoView({ behavior: 'smooth' });
        });
      },
      getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(";").shift();
        return null;
      },
      setCookie(name, value, days) {
        const date = new Date();
        date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
        document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`;
      },
      // 初始化 Session
      async initializeSession() {
        const existingSessionId = this.getCookie("session_id");
        if (existingSessionId) {
          this.sessionId = existingSessionId;
        } else {
          await this.requestNewSessionId();
        }
      },
      // 请求新的 session_id
      async requestNewSessionId() {
        const response = await fetch(`${this.apiHost}/start_session`, {
          method: "POST",
        });
        const data = await response.json();
        this.sessionId = data.user_id;
        this.setCookie("session_id", this.sessionId, 1); // 设置 1 天有效期
      },
      // 通用请求函数（处理 400 错误）
      async sendRequest(url, options) {
        const response = await fetch(url, options);
        if (response.status === 400) {
          console.warn("Session ID 失效，重新请求新的 ID...");
          await this.requestNewSessionId(); // 请求新的 session_id
          const retryOptions = {
            ...options,
            body: JSON.stringify({
              ...JSON.parse(options.body),
              user_id: this.sessionId, // 使用新的 session_id
            }),
          };
          return fetch(url, retryOptions).then((res) => res.json());
        }
        return response.json();
      },
      // 模拟后端响应（替换为真实后端调用）
      async fetchAIResponse(input) {
        const url = `${this.apiHost}/chat`;
        const options = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ input, user_id: this.sessionId }),
        };
        return this.sendRequest(url, options);
      },
      async sendMessage() {
        if (this.newMessage.trim() !== '') {
          // Add User Msg
          this.addMessage({ 
            icon: "🚀",
            content: this.newMessage,
            isAi: false,
          });
          this.newMessage = '';
          // Loading Ai Response
          this.addMessage({ 
            content: "loading ...",
            isAi: true,
          });
          this.scrollToBottom();
          // send msg to backend
          try {
            const data = await this.fetchAIResponse(this.messages[this.messages.length - 2]?.content);
            //loading.value = false;

            // 更新 AI 消息
            this.messages[this.messages.length - 1].content = data.response;
          } catch (error) {
            //loading.value = false;
            console.error("请求失败：", error);
            this.messages[this.messages.length - 1].content = "抱歉，请求失败，请稍后重试。";
          }
          this.scrollToBottom();
        }
      },
    },
    mounted() {
      this.initializeSession(); // 初始化会话
      window.addEventListener("resize", this.scrollToBottom);
    },
    beforeDestroy() {
      window.removeEventListener("resize", this.scrollToBottom);
    },
  };
</script>

<style lang="scss" scoped>
.input-container {
  position: fixed;
  bottom: 50px; /* Navbar 的高度 */
  z-index: 10;
  width: 100%;
}
.input-sheet {
  padding: 5%;
  background-color: $second-background-color;
  color: $text-color;
}
.input-btn {
  background-color: $primary-highlight-color;
  color: $text-color
}
.btn-area {
  display: flex;                /* 使用 flexbox */
  justify-content: space-around; /* 水平居中并在元素之间添加间隔 */
  align-items: center;          /* 垂直居中 */
  width: 100%;
}
.btn-yes {
  background-color: $primary-highlight-color;
  color: $text-color;
}
.btn-no {
  background-color: $primary-background-color;
  color: $text-color;
}
</style>
