from gtts import gTTS
import os

def speak(text, n=0):
    tts = gTTS(text=text, lang="en")  # Change 'en' to another language if needed
    tts.save(f"outputs/output{n}.mp3")  # Save as a file
    os.system(f"afplay outputs/output{n}.mp3") # for macOS and for Linux use "mpg321 output.mp3"

if __name__ == "__main__":
    speak("Hello! I am your AI voice assistant.")
