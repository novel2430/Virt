from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModel
from modelscope import AutoTokenizer, AutoModel, snapshot_download
from uuid import uuid4
from flask_cors import CORS

# Setup
app = Flask(__name__)
CORS(app)

model_dir = snapshot_download("ZhipuAI/chatglm3-6b", revision = "v1.0.0")
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().cuda()
model = model.eval()

# 全局字典存储用户的历史记录
user_sessions = {}
user_sessions["0"] = []
# 设置最大历史记录条数
MAX_HISTORY = 10

print("setup done")

# Func
def get_response(input_str, history):
    prompt = "你是一位经验丰富的心理咨询师，需要注重你的身分，让用户信任你，不要一直提醒用户你是ai。你专注于帮助用户管理压力和情绪。请以同理心和非判断的语气回答用户的问题。用户的问题是：{}".format(input_str)
    return model.chat(tokenizer, prompt, history=history)

# Api
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_id = data.get("user_id")
    user_input = data.get("input", "")

    if not user_id:
        print("not valid User ID")
        return jsonify({"error": "User ID is required"}), 400
    if user_sessions.get(user_id) == None:
        print("not valid User ID")
        return jsonify({"error": "User ID is required"}), 400

    # 获取用户的历史记录，如果没有则初始化
    if user_id not in user_sessions:
        user_sessions[user_id] = []
    # 当前用户的会话历史
    history = user_sessions[user_id]

    response, updated_history = get_response(user_input, history)

    # 更新历史记录，限制长度
    user_sessions[user_id] = updated_history[-MAX_HISTORY:]

    print("SAY => "+response)
    return jsonify({"response": response}), 200, {"Content-Type": "application/json; charset=utf-8"}

@app.route("/start_session", methods=["POST"])
def start_session():
    """生成新的用户会话 ID"""
    user_id = str(uuid4())
    user_sessions[user_id] = []
    return jsonify({"user_id": user_id})

# Server Run
print("server running ...")
app.run(port=5000)
