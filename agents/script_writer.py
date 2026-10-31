# agents/script_writer.py

import ollama


def script_writer(channel: str, idea: dict):
    print(f"\n=== Script Writer Agent started ===")
    print(f"Writing script for: {idea.get('title')}\n")

    prompt = f"""
You are the Script Writer for Little Letter Lane (kids YouTube Shorts).

Write a short, fun script between 18 and 45 seconds maximum.

Hard rules:
- Very simple language a 2-4 year old can enjoy
- Cute and playful tone
- Must have ONE exciting moment that is almost overstimulating, then quickly returns to calm
- Do not make the whole video chaotic
- Clear scene-by-scene format

Idea to turn into a script:
Title: {idea.get("title")}
Concept: {idea.get("concept")}
Exciting moment idea: {idea.get("edge_of_overstimulation_scene")}

Use this exact format:

Scene 1 (0-3s):
Visual: 
Voiceover: 
On-screen text: 

Scene 2 (3-7s):
Visual: 
Voiceover: 
On-screen text: 

(continue with more scenes)

At the end write:
Total length: Xs
"""

    response = ollama.chat(
        model="llama3.2:1b", messages=[{"role": "user", "content": prompt}]
    )

    result = response["message"]["content"]
    print("=== Script Writer Result ===")
    print(result)
    print("=== End of Script ===\n")
    return result
