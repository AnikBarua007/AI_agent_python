import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")
client = genai.Client(api_key=api_key)
def model_list():
    for model in client.models.list():
        print(model.name)
if __name__ == "__main__":
    model_list()