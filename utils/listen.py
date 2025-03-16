from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError

def listen():
    recognizer = Recognizer()
    microphone = Microphone()
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except UnknownValueError:
        print("Could not understand audio")
    except RequestError as e:
        print("Could not request results; {0}".format(e))
    return ""

def main():
    while True:
        user_input = listen()
        if not user_input:
            continue
        print("You:", user_input)

if __name__ == "__main__":
    main()