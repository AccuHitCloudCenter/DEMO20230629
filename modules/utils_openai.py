import asyncio
import openai
import os

conversation_history = []

async def call_openai(question: str):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, call_openai_sync, question)
    return result

def call_openai_sync(text):
    openai.api_type = "azure"
    openai.api_base = "https://aoia-demo2.openai.azure.com/"
    openai.api_version = "2023-03-15-preview"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    conversation_history.append({"role":"user","content":text}) 

    response = openai.ChatCompletion.create(
    engine="TEAMS",
    messages = [{"role":"system","content":"名字是Iris，身分是東海大學的智能客服，問答的內容僅涉及學校相關的事務，回答的內容要活潑、適當使用各種顏文字，但回答不要過長，回答盡量快速"},  #You are an AI assistant that helps people find information
                {"role":"user","content":text}],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

    conversation_history.append({"role":"assistant","content":response['choices'][0]['message']['content']})

    return response['choices'][0]['message']['content']
