import boto3
import botocore.exceptions
import json

# Set up the session with both profile and region at once
boto3.setup_default_session(profile_name='watchelm', region_name='eu-west-1')

try:
    # Create the Bedrock client
    bedrock = boto3.client('bedrock')
    
    # List all foundation models
    print("Listing all foundation models...")
    response = bedrock.list_foundation_models()
    
    # Print the full response for debugging
    print("\nFull API Response:")
    print(json.dumps(response, indent=2, default=str))
    
    # Extract and print model information in a more readable format
    print("\n=== Available Foundation Models ===")
    for model in response.get('modelSummaries', []):
        model_id = model.get('modelId', 'Unknown')
        model_arn = model.get('modelArn', 'Unknown')
        provider_name = model.get('providerName', 'Unknown')
        
        print(f"\nModel ID: {model_id}")
        print(f"Model ARN: {model_arn}")
        print(f"Provider: {provider_name}")
        print("-" * 50)
    
    # Also try to list knowledge bases
    print("\n\n=== Knowledge Bases ===")
    bedrock_agent = boto3.client('bedrock-agent')
    kb_response = bedrock_agent.list_knowledge_bases()
    
    print("\nKnowledge Bases:")
    print(json.dumps(kb_response, indent=2, default=str))
    
except botocore.exceptions.ClientError as e:
    print(f"Error: {e}")
    print("\nDetailed error information:")
    if hasattr(e, 'response') and 'Error' in e.response:
        print(f"Error Code: {e.response['Error'].get('Code', 'Unknown')}")
        print(f"Error Message: {e.response['Error'].get('Message', 'Unknown')}")
    else:
        print("No detailed error information available")
    
    # If it's a service not available error
    if hasattr(e, 'response') and e.response.get('Error', {}).get('Code') == 'UnrecognizedClientException':
        print("\nThe Bedrock service might not be available in your region or your account might not have access to it.")
        print("Please verify the following:")
        print("1. You have enabled Amazon Bedrock in your AWS account")
        print("2. Your IAM role/user has the necessary permissions")
        print("3. The service is available in the eu-west-1 region")