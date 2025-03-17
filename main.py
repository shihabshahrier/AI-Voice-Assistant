import os
from openai import OpenAI
from dotenv import load_dotenv
from utils.listen import listen
from utils.gspeak import speak

def main():
    load_dotenv()

    client = OpenAI(
        base_url="https://api.studio.nebius.com/v1/",
        api_key=os.environ.get("NEBIUS_API_KEY")
    )

    messages = [
        {
            "role": "system",
            "content": 
            '''
                You are a highly efficient AI Voice Assistant. 
                Respond in a clear, concise, and natural tone. 
                Keep answers brief and to the point, avoiding unnecessary details.
                If clarification is needed, ask short follow-up questions.
                Prioritize accuracy and relevance in your responses.
            '''
        }
    ]

    START = False

    while True:
        # user_input = input("You: ")
        user_input = listen()
        if not user_input:
            continue
        if user_input.lower() in ["exit", "quit", "good bye", "bye", "goodbye"]:
            print("Bot: Goodbye!")
            speak("Goodbye!")
            START = False
            break
        
        print("You:", user_input)

        if user_input.lower() in ["hello gandu", "hi gandu", "hey gandu", "gandu"]:
            print("Bot: Hello I am dr. Gandu! How can I help you today")
            speak("Hello I am dr. Gandu! How can I help you today?")
            START = True
            continue

        if START:
            messages.append({
                "role": "user",
                "content": user_input
            })

            try:
                response = client.chat.completions.create(
                    model="deepseek-ai/DeepSeek-V3",
                    max_tokens=512,
                    temperature=0.6,
                    top_p=0.95,
                    extra_body={"top_k": 50},
                    messages=messages,
                    stream=True
                )
            except Exception as e:
                print(f"Error during API call: {e}")
                continue

            bot_message = ""
            try:
                print("Bot:", end=" ", flush=True)
                for chunk in response:
                    delta = getattr(chunk.choices[0].delta, 'content', '')
                    bot_message += delta
                    print(delta, end="", flush=True)
            except Exception as e:
                print(f"\nError processing stream: {e}")
                continue

            print() 
            speak(bot_message)
            messages.append({
                "role": "assistant",
                "content": bot_message
            })

if __name__ == "__main__":
    main()