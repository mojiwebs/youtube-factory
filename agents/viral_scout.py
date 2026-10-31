# agents/viral_scout.py

import ollama


def viral_scout(channel: str, num_videos: int = 10):
    print(f"\n=== Viral Scout Agent started ===")
    print(f"Channel: {channel}")
    print(f"Analysing top {num_videos} videos...\n")

    if channel == "kids":
        prompt = f"""
You are researching top kids educational Shorts about letters and simple learning.
Return practical patterns in clean JSON with these keys:
top_hooks, common_structures, title_patterns, retention_tricks, thumbnail_patterns, notes.
Focus on what actually keeps toddlers watching.
"""
    else:
        prompt = f"""
You are researching clean finance Shorts.
Return practical patterns in clean JSON.
"""

    response = ollama.chat(
        model="llama3.2:1b", messages=[{"role": "user", "content": prompt}]
    )

    result = response["message"]["content"]
    print("=== Viral Scout Result ===")
    print(result)
    print("=== End of Scout ===\n")
    return result
