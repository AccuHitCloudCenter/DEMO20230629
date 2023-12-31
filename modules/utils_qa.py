'''
Author: Shawn
Date: 2023-06-16 14:24:49
LastEditors: Shawn
LastEditTime: 2023-06-16 14:58:16
FilePath: /CloudArchitectures/linebot_openai/modules/utils_qa.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import asyncio
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient


load_dotenv()


async def call_qa(question: str):
    endpoint = os.environ["AZURE_QUESTIONANSWERING_ENDPOINT"]
    key = os.environ["AZURE_QUESTIONANSWERING_KEY"]
    client = QuestionAnsweringClient(endpoint, AzureKeyCredential(key))

    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, call_qa_sync, client, question)
    if result:
        max_confidence = max(result, key=lambda x: x[0])
        if max_confidence[0] > 0.1:
            print(max_confidence[0])
            return max_confidence[1]
        else:
            return ""
    else:
        return ""
 

def call_qa_sync(client, question):
    output = client.get_answers(
        question=question,
        project_name="demo20230621",
        deployment_name="production"
    )

    results = []
    for candidate in output.answers:
        results.append((candidate.confidence, candidate.answer, candidate.source))

    return results
