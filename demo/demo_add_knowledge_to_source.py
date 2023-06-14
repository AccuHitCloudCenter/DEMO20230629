'''
Author: Shawn
Date: 2023-06-14 11:50:34
LastEditors: Shawn
LastEditTime: 2023-06-14 11:58:29
FilePath: /CloudArchitectures/linebot_openai/demo/demo_add_knowledge_to_source.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import os
from dotenv import load_dotenv
load_dotenv()
from azure.core.credentials import AzureKeyCredential

from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.ai.language.questionanswering.authoring import AuthoringClient
from azure.ai.language.questionanswering import models

def add_a_knowledge_source(sources):
    from azure.ai.language.questionanswering.authoring import AuthoringClient

    # get service secrets
    endpoint = os.environ["AZURE_QUESTIONANSWERING_ENDPOINT"]
    key = os.environ["AZURE_QUESTIONANSWERING_KEY"]

    # create client
    client = AuthoringClient(endpoint, AzureKeyCredential(key))

    project_name = "IssacNewton"
    update_sources_poller = client.begin_update_sources(
        project_name=project_name,
        sources=sources
    )
    update_sources_poller.result()

    # list sources
    print("list project sources")
    sources = client.list_sources(
        project_name=project_name
    )
    for source in sources:
        print("project: {}".format(source["displayName"]))
        print("\tsource: {}".format(source["source"]))
        print("\tsource Uri: {}".format(source["sourceUri"]))
        print("\tsource kind: {}".format(source["sourceKind"]))    
    

if __name__ == "__main__":
    breakpoint()
    sources = [
            {
                "op": "add",
                "value": {
                    "displayName": "Issac Newton Bio",
                    "sourceUri": "https://wikipedia.org/wiki/Isaac_Newton",
                    "sourceKind": "url"
                }
            }
        ]
    add_a_knowledge_source(sources)
