import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_persona(content_blocks):
    prompt = (
        "You're an AI that analyzes Reddit content to build a user persona. "
        "Below are posts and comments made by the user:\n\n"
        + "\n\n".join(content_blocks[:30]) +
        "\n\n---\n\n"
        "Based on the above, provide a detailed user persona including:\n"
        "- Name (fictitious)\n- Age range\n- Occupation\n- Interests\n"
        "- Personality traits\n- Beliefs/values\n- Writing style\n"
        "For each characteristic, cite the post/comment that led to it.\n"
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']
