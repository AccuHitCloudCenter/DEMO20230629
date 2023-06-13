'''
Author: Shawn
Date: 2023-06-08 17:55:47
LastEditors: Shawn
LastEditTime: 2023-06-09 17:47:19
FilePath: /CloudArchitectures/linebot_openai/demo/openai_api.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import os 
from dotenv import load_dotenv
import openai
load_dotenv()


OPENAI_API_KEY="897121ee655846be8b4801140acdc207"
# # OPENAI API Key初始化設定
# openai.api_key = os.getenv('OPENAI_API_KEY')
# text = "如何經營Line OA?"
# response = openai.Completion.create(model="gpt-35-turbo", prompt=text, temperature=0.5, max_tokens=500)
# print(response)
# # 重組回應
# answer = response['choices'][0]['text'].replace('。','')
# breakpoint()



import os
import openai
openai.api_type = "azure"
openai.api_base = "https://product-cdp-open-ai-dev-01.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "897121ee655846be8b4801140acdc207"# os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   engine="gpt-35-turbo",
#   prompt="如何經營line oa",
#   temperature=1,
#   max_tokens=100,
#   top_p=0.5,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stop=None)
# breakpoint()


# import openai

# openai.api_type = "azure"
# openai.api_key = YOUR_API_KEY
# openai.api_base = "https://YOUR_RESOURCE_NAME.openai.azure.com"
# openai.api_version = "2023-05-15"

response = openai.Embedding.create(
    input="Your text string goes here",
    engine="YOUR_DEPLOYMENT_NAME"
)
embeddings = response['data'][0]['embedding']
print(embeddings)
