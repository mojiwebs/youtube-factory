# agents/idea_generator.py

import ollama


def idea_generator(channel: str, scout_result: str, num_ideas: int = 5):
    print(f"\n=== Idea Generator Agent started ===")
    print(f"Channel: {channel}")
    print(f"Generating {num_ideas} ideas...\n")

    prompt = f"""
You are the Idea Generator for Little Letter Lane (kids channel).

Create a mixture of:
- Single letter ideas (Letter A, Letter B...)
- Mini-story Alphabet Adventure ideas

Rules:
- Age 1-5
- Cute 2D cartoon, darker-skinned character
- Must include one almost-overstimulating exciting moment that returns to calm

Scout patterns:
{scout_result}

Return {num_ideas} ideas in clean JSON with rank, title, concept, why_it_should_work, edge_of_overstimulation_scene.
"""

    response = ollama.chat(
        model="llama3.2:1b", messages=[{"role": "user", "content": prompt}]
    )

    result = response["message"]["content"]
    print("=== Idea Generator Result ===")
    print(result)
    print("=== End of Ideas ===\n")
    return result
