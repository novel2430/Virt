# 人机交互与虚拟人 - 课程项目 - Bonfire🔥 解忧旅社
## 介绍
简单演示了本小组对项目要求所思考的功能实践。  
开发了最基础的介面交互，以及调用本地运行的大语言模型 (**ChatGLM3**) 进行心理咨商对话内容的推理生成。  
[Demo](https://www.yejsgk.top)展示  
>UI介面建议**手机端**浏览，但也支持电脑、平板端

## UI 展示
> 非全部页面
### 主页
![img](https://github.com/novel2430/Virt/blob/main/img/Nav-Home.png?raw=true)
### 咨询
![img](https://github.com/novel2430/Virt/blob/main/img/Nav-Chat.png?raw=true)
### 信息
![img](https://github.com/novel2430/Virt/blob/main/img/Nav-Msg.png?raw=true)
### 个人
![img](https://github.com/novel2430/Virt/blob/main/img/Nav-Profile.png?raw=true)
### 倾诉解答
![img](https://github.com/novel2430/Virt/blob/main/img/Child-Post.png?raw=true)
### 每日一问
![img](https://github.com/novel2430/Virt/blob/main/img/Child-Ques.png?raw=true)
## 依赖
  - [Python](https://www.python.org/) >= 3.10
  - [Node.js](https://nodejs.org/)
## 部属
请先`git clone https://github.com/novel2430/Virt.git`，把代码同步至本地，并进入项目路径
### 前端
#### 进入前端目录
```sh
cd frontEnd
```
#### (可选) 编辑后端api host
可以将`src/main.js`中的后端地址改成你自己部属的后端地址
```js
// src/main.js
import { createApp } from 'vue'
import router from './router';
import vuetify from './vuetify.js'

// Components
import App from './App.vue'

const app = createApp(App);

// Env
app.provide("apiHost", "http://127.0.0.1:5000") // change here

app.use(router).use(vuetify).mount('#app')
```
#### 测试运行
```sh
npm run dev
```
#### 发布
```sh
npm run build
```
### 后端
#### 进入后端目录
```sh
cd backEnd
```
#### 安装依赖
```sh
pip install -r requirements.txt
```
#### 运行
```sh
python main.py
```
## 技术栈
### 前端
  - [Vue3.js](https://vuejs.org/)  
    提供快速开发html+js前端的框架
  - [Vuetify](https://vuetifyjs.com/)  
    提供外观一致，Material Design风格的完善组件库
  - [Sass](https://sass-lang.com/)  
    CSS管理
  - [Vite](https://vite.dev/)  
    快速部属，建构前端工具
### 后端
  -  [Python Flask](https://flask.palletsprojects.com/s)  
    后端server开发框架
  - 推理模型: [ChatGLM3-6b](https://huggingface.co/THUDM/chatglm3-6b)
### 前后端部属
  - [Nginx](https://nginx.org/)  
    提供反向代理，解决前后端跨域问题
## 后端API
### Api 列表
| api | method | 功能概述 | args | response |
| --- | --- | --- | --- | --- |
| /start_session | POST | 获取新的session ID | None | `user_id` |
| /chat| POST | 获取生成的回复 | `user_id`, `input` | `response` |
### Api 简述
#### /start_session
对于后端服务器而言，不同的`user_id`对应的是不同的对话纪录，所以需要在请求对话之前，为不同的终端分配一个ID，该ID保存在使用者cookie中，**期限为1天**
  - Method  
    `POST`
  - Request  
    None
  - Response  
    ```json
    {
      "user_id": "<新的UUID>"
    }
    ```
#### /chat
请求后端大语言模型的API，根据用户ID验证是否是第一次访问，并查找对话纪录。最后根据用户咨询内容，生成回应并回传。
  - Method  
    `POST`
  - Request  
    ```json
    {
      "user_id": "<用户UUID>",
      "input": "<咨询内容>"
    }
    ```
  - Response  
    ```json
    {
      "response": "<对话回复>"
    }
    ```
