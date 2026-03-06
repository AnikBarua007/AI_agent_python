import argparse
import os
from dotenv import load_dotenv
from google import genai
from prompts import  system_prompt
from functions.call_function import available_functions, call_function
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")
client = genai.Client(api_key=api_key)
def model_list():
    print(client.models.list())
def main():
    print("Hello from python-ai-agent-scratch!")
    print(client.models.list())
    # List available models to verify the API key is working
    # print("Available models:")
    # for model in client.models.list():
    # print(f"- {model.name}")
    #- models/imagen-4.0-fast-generate-001
    # - models/veo-2.0-generate-001
    # - models/veo-3.0-generate-001
    # - models/veo-3.0-fast-generate-001
    # - models/veo-3.1-generate-preview
    # - models/veo-3.1-fast-generate-preview
    # - models/gemini-2.5-flash-native-audio-latest
    # - models/gemini-2.5-flash-native-audio-preview-09-2025
    # - models/gemini-2.5-flash-native-audio-preview-12-2025
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    from google.genai import types

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    # Now we can access `args.user_prompt`
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=messages,
        config=types.GenerateContentConfig( tools=[available_functions],system_instruction=system_prompt,
                                           temperature=0)

    )
    
    print(f"Prompt token: {response.usage_metadata.total_token_count}")
    print(f"Request token: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    function_results = []
    function_calls =response.function_calls
    if function_calls!=None:
        for function_call in function_calls:
            function_call_result = call_function(function_call, verbose=args.verbose)
            # print(function_call_result)
            list_parts=function_call_result.parts
            if list_parts==None:
                raise Exception(f"Unexpected function call result format: {function_call_result}")
            if list_parts[0].function_response == None:
                raise Exception(f"Unexpected function call result format: {function_call_result}")
            function_results.append(list_parts[0])
            response_call = list_parts[0].function_response.response
            if response_call==None:
                raise Exception(f"Unexpected function call result format: {function_call_result}")
            # print(f"Function call result for {function_call.name}: {response_call}")
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            
    
    else :
        print(response.text)
if __name__ == "__main__":
    main()
