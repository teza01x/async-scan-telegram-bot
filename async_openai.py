import aiohttp
from config import *


async def text_answer_request(text):
    ### openAI API url
    url = 'https://api.openai.com/v1/chat/completions'


    ### headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_key}',
    }

    ### requested data
    data = {
        "model": f"{model}",
        "messages": [{"role": "user", "content": f"{gpt_prompt}"
                                                 f"{text}"}],
        "temperature": temperature
    }

    ### get response
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            data = await response.json()

    return data['choices'][0]['message']['content']
