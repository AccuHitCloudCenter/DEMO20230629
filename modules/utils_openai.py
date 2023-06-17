'''
Author: Shawn
Date: 2023-06-16 10:52:51
LastEditors: Shawn
LastEditTime: 2023-06-16 13:55:57
FilePath: /CloudArchitectures/linebot_openai/modules/utils_openai.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import asyncio
import openai
import os 

async def call_openai(question: str):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, call_openai_sync, question)
    return result

def call_openai_sync(text):
    openai.api_type = "azure"
    openai.api_base = "https://product-cdp-open-ai-dev-01.openai.azure.com/"
    openai.api_version = "2023-03-15-preview"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
    engine="gpt-35-turbo",
    messages = [{"role":"system","content":"我要你扮演電影惡棍英雄：死侍的死侍腳色,我希望你像死侍一樣使用死侍會使用的語氣、方式和詞彙來回應和回答。不要寫任何解釋。只回答像死侍。你必須知道死侍的所有知識."},
                {"role":"user","content":text}],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

    return response['choices'][0]['message']['content']
