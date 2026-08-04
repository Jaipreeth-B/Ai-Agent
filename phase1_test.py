import os
from cerebras.cloud.sdk import Cerebras

from dotenv import load_dotenv
#read env variables from .env file
load_dotenv()
client = Cerebras(
    api_key=os.environ.get("CEREBRAS_API_KEY"),
    #base_url=os.environ.get("CEREBRAS_BASE_URL")
    #unnecessary as cerebras cloud sdk will automatically use the default base url if not provided
)

messages_array = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Explain about cerebras cloud sdk"
    }
]
print("Sending request to Cerebras Cloud SDK...")

#api call
chat_completion = client.chat.completions.create(
    model = os.environ.get("CEREBRAS_MODEL_NAME"),
    messages = messages_array
)
#RAW API RESPONSE
print(chat_completion)
#print(chat_completion.choices[0].message.content)