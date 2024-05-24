
import os

from groq import Groq

client = Groq(
    api_key="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",
)

while(True):
    in_put = input("YOU: ")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":in_put,
            }
        ],
        model="llama3-8b-8192",
    )
    print("AI: ",chat_completion.choices[0].message.content)

    if(in_put=="exit"):
        break