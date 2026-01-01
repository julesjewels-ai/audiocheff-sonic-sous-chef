"""
Unit tests for the core application logic.
"""

import pytest
from src.core.app import AudioCheffApp

@pytest.fixture
def app():
    """Fixture to provide a fresh app instance."""
    return AudioCheffApp()

def test_initial_state(app):
    """Ensure app starts in correct initial state."""
    assert app.is_active is True
    assert app.current_recipe_step == 0
    assert len(app.detected_events) == 0

def test_audio_recognition_logic(app):
    """Test that known signatures trigger the correct logic."""
    # Simulate detecting a boiling sound
    response = app.process_audio_frame("boiling")
    
    assert "[MATCH] BOILING" in response
    assert "boiling" in app.detected_events
    assert app.current_recipe_step == 1

def test_unknown_audio_ignored(app):
    """Test that unknown sounds do not trigger step advancement logic."""
    initial_step = app.current_recipe_step
    response = app.process_audio_frame("dog_barking")
    
    assert "[NO MATCH]" in response
    assert "dog_barking" not in app.detected_events
    assert app.current_recipe_step == initial_step

def test_whisking_recognition(app):
    """Test that the 'whisking' sound is recognized."""
    response = app.process_audio_frame("whisking")
    assert "[MATCH] WHISKING" in response
    assert "whisking" in app.detected_events
    assert app.current_recipe_step == 1
