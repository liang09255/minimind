import httpx
from openai import OpenAI
client = OpenAI(
    base_url="https://localhost:8801/v1",
    api_key="token-liang09255",
    http_client=httpx.Client(verify=False)
)


completion = client.chat.completions.create(
    model="minimind",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)


print(completion.choices[0].message)