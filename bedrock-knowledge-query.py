import boto3
import botocore.exceptions
import json

# Set up the session with both profile and region at once
boto3.setup_default_session(profile_name='watchelm', region_name='eu-west-1')

try:
    # First, get available models to find the correct ARN
    print("Fetching available models...")
    bedrock_agent_runtime = boto3.client('bedrock-agent-runtime')
    
    # Now try the retrieve_and_generate call
    response = bedrock_agent_runtime.retrieve_and_generate(
        input={
            "text": "What is Java?"
        },
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": "OF7DAWCHHW",
                "modelArn": "arn:aws:bedrock:eu-west-1::foundation-model/anthropic.claude-3-haiku-20240307-v1:0",
                "retrievalConfiguration": {
                    "vectorSearchConfiguration": {
                        "numberOfResults": 5
                    }
                },
                "generationConfiguration": {
                    "promptTemplate": {
                        "textPromptTemplate": "Human: Use the following pieces of context to answer the question. If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\nContext:\n$search_results$\n\nQuestion: What is Java?\n\nAssistant:"
                    },
                    "inferenceConfig": {
                        "textInferenceConfig": {
                            "temperature": 0.7,
                            "topP": 0.9,
                            "maxTokens": 1000
                        }
                    }
                }
            }
        }
    )
    
    print("\nResponse from Bedrock:")
    print(response['output']['text'])
    
except botocore.exceptions.ClientError as e:
    print(f"Error: {e}")
    