# orchestrator.py

from agents.viral_scout import viral_scout


def run_pipeline(channel: str):
    """
    Simple Orchestrator
    This is the manager that calls the agents one by one.
    """

    print("\n" + "=" * 50)
    print("YOUTUBE FACTORY ORCHESTRATOR")
    print("Channels: Little Letter Lane | Ledger & Code")
    print("=" * 50 + "\n")

    print(f"Starting pipeline for channel: {channel}\n")

    # Step 1: Call Viral Scout
    print("Step 1: Calling Viral Scout Agent...")
    scout_result = viral_scout(channel=channel)

    # Later we will add more agents here:
    # idea_generator(scout_result)
    # script_writer(...)
    # etc.

    print("Pipeline finished (only Scout is connected for now).")
    print("Next agents will be added one by one.\n")


if __name__ == "__main__":
    # Change to "finance" if you want to test the other channel
    run_pipeline(channel="kids")
