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
    messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},
                {"role":"user","content":text}],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

    return response['choices'][0]['message']['content']