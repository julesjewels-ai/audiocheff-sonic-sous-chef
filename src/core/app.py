"""
Core application logic for AudioCheff.

This module handles the state machine for the cooking assistant and 
processes incoming audio signatures.
"""

from typing import Optional, Dict, List
import datetime

class AudioCheffApp:
    """
    Main controller for the Sonic Sous-Chef.
    """

    def __init__(self) -> None:
        self.is_active: bool = True
        self.current_recipe_step: int = 0
        self.detected_events: List[str] = []
        
        # Mock database of recognizable sounds
        self.known_signatures: Dict[str, str] = {
            "boiling": "Water is boiling. Ready for pasta.",
            "searing": "High heat detected. Searing process started.",
            "chopping": "Rhythmic chopping detected. Mise en place in progress.",
            "whisking": "Whisking detected. Emulsification in progress.",
            "timer_alarm": "Timer finished!"
        }

    def process_audio_frame(self, mock_signature: Optional[str] = None) -> str:
        """
        Ingests an audio frame (simulated here via string) and updates state.
        
        Args:
            mock_signature: A string representing a detected sound class for MVP testing.
                            In production, this would be a numpy array of audio data.
        
        Returns:
            str: The system response or log message.
        """
        if not self.is_active:
            return "System inactive."

        detected = mock_signature or "silence"
        response = "Listening..."

        if detected in self.known_signatures:
            self.detected_events.append(detected)
            action_message = self.known_signatures[detected]
            response = f"[MATCH] {detected.upper()}: {action_message}"
            self._advance_step(detected)
        else:
            response = f"[NO MATCH] Background noise: {detected}"

        print(response)
        return response

    def _advance_step(self, event: str) -> None:
        """Internal logic to move recipe forward based on event."""
        # Simple state machine logic for MVP
        self.current_recipe_step += 1
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f" -> Step {self.current_recipe_step} completed at {timestamp}")

    def get_session_history(self) -> List[str]:
        """Returns the list of events detected in this session."""
        return self.detected_events