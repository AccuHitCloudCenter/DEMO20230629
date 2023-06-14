'''
Author: Shawn
Date: 2023-06-14 09:53:09
LastEditors: Shawn
LastEditTime: 2023-06-14 11:47:46
FilePath: /CloudArchitectures/linebot_openai/demo/demo_questionanswering.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

"""
Reference:
https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-language-questionanswering/1.1.0/index.html#create-a-new-project
"""

import os
from dotenv import load_dotenv
load_dotenv()
from azure.core.credentials import AzureKeyCredential

from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.ai.language.questionanswering.authoring import AuthoringClient
from azure.ai.language.questionanswering import models



endpoint = os.environ["AZURE_QUESTIONANSWERING_ENDPOINT"]
key = os.environ["AZURE_QUESTIONANSWERING_KEY"]



def ask_a_question():
    """ 
    The only input required to ask a question using a knowledge base is just the question itself.
    You can set additional keyword options to limit the number of answers, specify a minimum confidence score, and more.
    """
    # from azure.ai.language.questionanswering import QuestionAnsweringClient
    client = QuestionAnsweringClient(endpoint, AzureKeyCredential(key))

    output = client.get_answers(
        question="愛酷什麼時候創立?",
        project_name="test-exp-20230608",#"IssacNewton",
        deployment_name="production"
    )
    for candidate in output.answers:
        print("({}) {}".format(candidate.confidence, candidate.answer))
        print("Source: {}".format(candidate.source))    


def ask_a_followup_question(previous_answer):
    """ 
    If your knowledge base is configured for chit-chat, 
    the answers from the knowledge base may include suggested prompts for follow-up questions to initiate a conversation. 
    You can ask a follow-up question by providing the ID of your chosen answer as the context for the continued conversation.
    """
    # from azure.ai.language.questionanswering import QuestionAnsweringClient
    # from azure.ai.language.questionanswering import models
    endpoint = os.environ["AZURE_QUESTIONANSWERING_ENDPOINT"]
    key = os.environ["AZURE_QUESTIONANSWERING_KEY"]

    client = QuestionAnsweringClient(endpoint, AzureKeyCredential(key))

    output = client.get_answers(
        question="How long should charging take?",
        answer_context=models.KnowledgeBaseAnswerContext(
            previous_qna_id=previous_answer.qna_id
        ),
        project_name="FAQ",
        deployment_name="live"
    )
    for candidate in output.answers:
        print("({}) {}".format(candidate.confidence, candidate.answer))
        print("Source: {}".format(candidate.source))

    
def create_a_new_project():
    # from azure.ai.language.questionanswering.authoring import AuthoringClient
    client = AuthoringClient(endpoint, AzureKeyCredential(key))
    with client:
    # create project
        project_name = "IssacNewton"
        project = client.create_project(
            project_name=project_name,
            options={
                "description": "biography of Sir Issac Newton",
                "language": "en",
                "multilingualResource": True,
                "settings": {
                    "defaultAnswer": "no answer"
                }
            })

        print("view created project info:")
        print("\tname: {}".format(project["projectName"]))
        print("\tlanguage: {}".format(project["language"]))
        print("\tdescription: {}".format(project["description"]))
        


def add_a_knowledge_source():
    from azure.ai.language.questionanswering.authoring import AuthoringClient

    # get service secrets
    endpoint = os.environ["AZURE_QUESTIONANSWERING_ENDPOINT"]
    key = os.environ["AZURE_QUESTIONANSWERING_KEY"]

    # create client
    client = AuthoringClient(endpoint, AzureKeyCredential(key))

    project_name = "IssacNewton"
    update_sources_poller = client.begin_update_sources(
        project_name=project_name,
        sources=[
            {
                "op": "add",
                "value": {
                    "displayName": "Issac Newton Bio",
                    "sourceUri": "https://wikipedia.org/wiki/Isaac_Newton",
                    "sourceKind": "url"
                }
            }
        ]
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
    


def deploy_your_project():
    # from azure.ai.language.questionanswering.authoring import AuthoringClient

    # create client
    client = AuthoringClient(endpoint, AzureKeyCredential(key))

    project_name = "IssacNewton"

    # deploy project
    deployment_poller = client.begin_deploy_project(
        project_name=project_name,
        deployment_name="production"
    )
    deployment_poller.result()

    # list all deployments
    deployments = client.list_deployments(
        project_name=project_name
    )

    print("view project deployments")
    for d in deployments:
        print(d)



if __name__ == "__main__":
    
    ask_a_question()
    # create_a_new_project()
    # ask_a_followup_question()
    # add_a_knowledge_source()
    # deploy_your_project()







# output = client.get_answers(
#     question="How long should my Surface battery last?",
#     project_name="FAQ",
#     deployment_name="test"
# )
# for candidate in output.answers:
#     print("({}) {}".format(candidate.confidence, candidate.answer))
#     print("Source: {}".format(candidate.source))
