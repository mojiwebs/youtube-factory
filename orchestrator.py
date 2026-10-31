# orchestrator.py

from agents.viral_scout import viral_scout
from agents.idea_generator import idea_generator
from agents.script_writer import script_writer
import re


def extract_top_idea(ideas_text: str):
    try:
        title = re.search(r'"title":\s*"([^"]+)"', ideas_text)
        concept = re.search(r'"concept":\s*"([^"]+)"', ideas_text)
        edge = re.search(r'"edge_of_overstimulation_scene":\s*"([^"]+)"', ideas_text)

        return {
            "title": title.group(1) if title else "Alphabet Adventure",
            "concept": concept.group(1) if concept else "A fun letter adventure",
            "edge_of_overstimulation_scene": edge.group(1)
            if edge
            else "Bright exciting moment",
        }
    except:
        return {
            "title": "Alphabet Adventure: The Lost Letter",
            "concept": "A friendly animal looks for a missing letter",
            "edge_of_overstimulation_scene": "Bright colourful moment when the letter is found",
        }


def run_pipeline(channel: str = "kids"):
    print("\n" + "=" * 50)
    print("YOUTUBE FACTORY ORCHESTRATOR")
    print("=" * 50 + "\n")

    print("Step 1: Viral Scout...")
    scout = viral_scout(channel)

    print("Step 2: Idea Generator...")
    ideas = idea_generator(channel, scout)

    print("Step 3: Script Writer...")
    top_idea = extract_top_idea(ideas)
    print(f"Selected: {top_idea['title']}")
    script_writer(channel, top_idea)

    print("\nPipeline complete (Scout → Ideas → Script)")


if __name__ == "__main__":
    run_pipeline("kids")
