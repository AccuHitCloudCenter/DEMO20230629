'''
Author: Shawn
Date: 2023-06-13 20:14:08
LastEditors: Shawn
LastEditTime: 2023-06-13 20:22:44
FilePath: /CloudArchitectures/linebot_openai/app.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.exceptions import InvalidSignatureError
from flask import Flask, request, abort
from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

# 获取环境变量的值
channel_access_token = os.getenv("CHANNEL_ACCESS_TOKEN")
channel_secret = os.getenv("CHANNEL_SECRET")

# 在 Line Developers 上获取的 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

app = Flask(__name__)

# 处理 Line 的 Webhook 请求
@app.route("/callback", methods=["POST"])
def callback():
    # 获取请求的签名、负载和事件
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

# 处理文本消息的函数
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    reply_text = "你发送了：{}".format(text)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))

if __name__ == "__main__":
    app.run()
