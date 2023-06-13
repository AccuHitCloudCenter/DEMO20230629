'''
Author: Shawn
Date: 2023-06-09 17:12:47
LastEditors: Shawn
LastEditTime: 2023-06-13 17:58:47
FilePath: /CloudArchitectures/linebot_openai/demo/linechatbot_api.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *



uid = event.joined.members[0].user_id
gid = event.source.group_id
profile = line_bot_api.get_group_member_profile(gid, uid)
name = profile.display_name
message = TextSendMessage(text=f'{name}歡迎加入')
line_bot_api.reply_message(event.reply_token, message)