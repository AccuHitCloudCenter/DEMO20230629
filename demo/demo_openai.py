'''
Author: Shawn
Date: 2023-06-13 20:43:35
LastEditors: Shawn
LastEditTime: 2023-06-13 21:13:31
FilePath: /CloudArchitectures/linebot_openai/demo_openai.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = "https://product-cdp-open-ai-dev-01.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.ChatCompletion.create(
  engine="gpt-35-turbo",
  messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},
              {"role":"user","content":"列出三個常見的程式語言的名稱即可，不用加上其他說明。"}],
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

text = response['choices'][0]['message']['content']
print(text)



breakpoint()