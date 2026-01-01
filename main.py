"""
AudioCheff Entry Point.

Handles command-line arguments and initializes the main application loop.
"""

import argparse
import sys
import time
from src.core.app import AudioCheffApp

def parse_arguments() -> argparse.Namespace:
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(
        description="AudioCheff: Sonic Sous-Chef CLI"
    )
    parser.add_argument(
        "--version", 
        action="version", 
        version="AudioCheff v0.1.0-mvp"
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run in simulation mode with pre-defined audio events"
    )
    return parser.parse_args()

def main() -> None:
    """Main execution function."""
    args = parse_arguments()
    app = AudioCheffApp()

    print("\U0001f373 Starting AudioCheff: Sonic Sous-Chef...")
    
    if args.demo:
        print("\U0001f50a Running in DEMO simulation mode...")
        # Simulate a cooking session
        events = ["boiling", "chopping", "searing", "silence", "timer_alarm"]
        for event in events:
            print(f"\n... Simulating environment sound: '{event}'")
            app.process_audio_frame(mock_signature=event)
            time.sleep(0.5)
    else:
        print("\U0001f399  Listening for acoustic signatures (Press Ctrl+C to stop)...")
        try:
            # In a real edge-ai scenario, this would loop over a microphone stream
            while True:
                # Placeholder for live audio stream processing
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\U0001f6d1 Stopping AudioCheff.")
            sys.exit(0)

if __name__ == "__main__":
    main()