import os
from openai import OpenAI

OPENAI_KEY = "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"

# Initialize client
client = OpenAI(api_key=OPENAI_KEY)

# Create a chat completion
response = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-3.5-turbo"
    messages=[
        {"role": "user", "content": "Write a short poem about the ocean."}
    ]
)

print(response.choices[0].message.content)
