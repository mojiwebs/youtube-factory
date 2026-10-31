# agents/metadata_agent.py

import ollama

def metadata_agent(channel: str, idea: dict, script: str):
    print(f"\n=== Metadata Agent started ===")

    prompt = f"""
You are the Metadata Agent for Little Letter Lane.

Create YouTube packaging for this video.

Idea title: {idea.get('title')}
Concept: {idea.get('concept')}

Script summary:
{script[:600]}

Return in this format:

Title: 
Description: 
Tags: 
Thumbnail concept: 
"""

    response = ollama.chat(model="llama3.2", messages=[
        {"role": "user", "content": prompt}
    ])

    result = response['message']['content']
    print("=== Metadata Result ===")
    print(result)
    print("=== End of Metadata ===\n")
    return result