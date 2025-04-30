import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get your key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Set it in your .env file or terminal.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def query_openai(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Respond clearly."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content