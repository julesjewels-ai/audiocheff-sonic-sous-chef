# AudioCheff: Sonic Sous-Chef

A hands-free culinary application that utilizes edge-AI audio recognition to track cooking progress. Instead of relying solely on voice commands or touching a messy screen, AudioCheff listens for specific acoustic signatures—like the hiss of searing meat, the rumble of boiling water, or the rhythmic chopping of vegetables—to automatically check off steps, start timers, and guide the user through complex recipes.

## Tech Stack

- React Native
- TensorFlow Lite
- Python (FastAPI)
- PostgreSQL
- WebAudio API

## Features

- Acoustic Event Detection (boiling, searing, chopping)
- Hands-free step navigation
- Smart Timers triggered by sound intensity
- Recipe editor with audio checkpoints
- Offline mode for privacy and latency

## Quick Start

```bash
# Clone and setup
git clone <repo-url>
cd audiocheff:-sonic-sous-chef
make install

# Run the application
make run
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
make install && make run
```

## Development

```bash
make install  # Create venv and install dependencies
make run      # Run the application
make test     # Run tests
make clean    # Remove cache files
```

## Testing

```bash
pytest tests/ -v
```
