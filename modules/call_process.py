import asyncio
from linebot_openai.modules.utils_openai import call_openai
from linebot_openai.modules.utils_qa import call_qa
import random

async def reply_message_sync(text):
    # Create tasks for the two API calls
    qa_task = asyncio.create_task(call_qa(text))
    openai_task = None

    start = asyncio.get_event_loop().time()
    while True:
        # Check if qa_task is done, if it is, get the result
        if qa_task.done():
            qa_result = qa_task.result()
            if (qa_result!= "") & (qa_result is not None) :
                # aq做完了，且有結果
                return qa_result
            else:
                # qa做完了，且有結果但是空字串
                # qa沒做完
                if openai_task is not None and openai_task.done():  # Check if OpenAI task has a result
                    return openai_task.result()
                # continue
        
        # If 3 seconds has passed and openai_task has not been started, start it
        if (asyncio.get_event_loop().time() - start) >= 3 and openai_task is None:
            openai_task = asyncio.create_task(call_openai(text))
        
        # If total time has passed 9 seconds, break the loop
        if (asyncio.get_event_loop().time() - start) >= 9:
            break

        await asyncio.sleep(0.01)  # sleep for a bit before next iteration of the loop

    if openai_task and openai_task.done():
        openai_result = openai_task.result()
        return openai_result

    answers = [
            "很抱歉，我無法提供正確的回答，你能提供更多細節嗎？",
            "對不起，我的知識有限，你能給我更多相關資訊嗎？",
            "非常抱歉，我需要更多的上下文來回答你的問題，你方便提供更多訊息嗎？",
            "對不起，我需要更多背景資料才能回答你，你能提供更多相關的訊息嗎？",
            "很抱歉，我無法做出準確的回應，你能提供更多詳細的資料嗎？"
        ]

    random_answer = random.choice(answers)

    return random_answer

def reply_message(text):
    return asyncio.run(reply_message(text))