import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Speed of speech (default is ~200)
    engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

    voices = engine.getProperty("voices")  # Get available voices
    engine.setProperty("voice", voices[1].id)  # Choose a voice (0: Male, 1: Female)

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! I am your voice assistant.")