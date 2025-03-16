import os
from openai import OpenAI
from dotenv import load_dotenv
from listen import listen
from speak import speak

def main():
    load_dotenv()

    client = OpenAI(
        base_url="https://api.studio.nebius.com/v1/",
        api_key=os.environ.get("NEBIUS_API_KEY")
    )

    messages = [
        {
            "role": "system",
            "content": "You are an AI Voice Assistant. So keep everthing short, clean and simple."
        }
    ]

    while True:
        # user_input = input("You: ")
        user_input = listen()
        if not user_input:
            continue
        print("You:", user_input)
        messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            response = client.chat.completions.create(
                model="meta-llama/Meta-Llama-3.1-70B-Instruct",
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