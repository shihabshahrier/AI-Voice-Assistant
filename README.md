# AI Voice Assistant

This project is an AI-powered voice assistant that uses speech recognition and text-to-speech functionalities. It leverages different TTS engines available via Python libraries.

## Features
- Voice interaction using pyttsx3 and gTTS
- Speech recognition support
- Integration with OpenAI for chat completions

## Requirements
- Python 3.x
- Dependencies (install via pip):
  - pyttsx3
  - gTTS
  - SpeechRecognition
  - python-dotenv
  - openai

## Setup
1. Clone the repository.
2. Create a virtual environment and install the required packages.
3. Create a `.env` file based on `.env.example` and add your `NEBIUS_API_KEY`.

```bash
pip install -r requirements.txt
```

## Usage
Run the main script to start the voice assistant:

```bash
python main.py
```

## Project Structure
- `main.py`: Entry point for the application.
- `utils/`
  - `speak.py`: Uses pyttsx3 for voice output.
  - `listen.py`: Handles speech recognition.
  - `gspeak.py`: Uses gTTS for voice output.
- `.env.example`: Environment variable template.
