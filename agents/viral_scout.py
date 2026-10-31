# agents/viral_scout.py

from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")


def viral_scout(channel: str, num_videos: int = 10):
    """
    Viral Scout Agent - Improved version
    Extracts practical, reusable patterns for the given channel.
    """

    print(f"\n=== Viral Scout Agent started ===")
    print(f"Channel: {channel}")
    print(f"Analysing top {num_videos} videos...\n")

    if channel == "kids":
        system_prompt = """
You are an expert YouTube Shorts researcher focused on kids and toddler educational content.

Your job is to extract clear, practical, and reusable patterns that actually work for high-retention kids Shorts.

Focus only on patterns that help with:
- Getting attention in the first 1-3 seconds
- Keeping toddlers watching
- Making the video feel fun and entertaining while still teaching
- Creating a moment that is exciting but never overstimulating

Be specific and concrete. Avoid vague answers.
"""
        user_prompt = f"""
Analyse the style of top-performing kids educational Shorts (letters, numbers, colours, simple concepts).

Return ONLY valid JSON in this exact format:

{{
  "niche": "kids",
  "top_hooks": [
    "specific hook example 1",
    "specific hook example 2",
    "specific hook example 3"
  ],
  "common_structures": [
    "structure example 1 (with rough timing)",
    "structure example 2"
  ],
  "title_patterns": [
    "title pattern 1",
    "title pattern 2"
  ],
  "retention_tricks": [
    "specific retention trick 1",
    "specific retention trick 2",
    "how to create an exciting moment that does not overstimulate"
  ],
  "thumbnail_patterns": [
    "thumbnail pattern 1",
    "thumbnail pattern 2"
  ],
  "notes": "any extra practical advice"
}}
"""
    else:
        system_prompt = """
You are an expert YouTube researcher focused on clean finance and practical money/tech explainers.

Your job is to extract clear, practical patterns that work for high-retention finance Shorts with minimal visuals.
"""
        user_prompt = f"""
Analyse the style of top-performing clean finance Shorts.

Return ONLY valid JSON in this exact format:

{{
  "niche": "finance",
  "top_hooks": [],
  "common_structures": [],
  "title_patterns": [],
  "retention_tricks": [],
  "thumbnail_patterns": [],
  "notes": ""
}}
"""

    response = client.chat.completions.create(
        model="llama3.2",  # change this if your model name is different
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.4,
    )

    result = response.choices[0].message.content
    print("=== Viral Scout Result ===")
    print(result)
    print("=== End of Scout ===\n")

    return result


if __name__ == "__main__":
    viral_scout(channel="kids")
