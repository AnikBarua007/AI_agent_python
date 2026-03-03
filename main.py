import argparse
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")

client = genai.Client(api_key=api_key)



def main():
    print("Hello from python-ai-agent-scratch!")
    client.models.list() # List available models to verify the API key is working
    # print("Available models:")
    # for model in client.models.list():
    #     print(f"- {model.name}")
#     - models/imagen-4.0-fast-generate-001
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
    args = parser.parse_args()
    # Now we can access `args.user_prompt`
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=args.user_prompt,
    )
   
    print(f"Prompt token: {response.usage_metadata.total_token_count}")
    print(f"Request token: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)
if __name__ == "__main__":
    main()
