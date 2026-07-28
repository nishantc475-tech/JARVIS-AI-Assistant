from speak import speak
from ai import ask_ai
from memory import remember, recall
from weather import get_weather
from news import get_news

def handle_ai(command):

    command = command.lower().strip()
     # Greetings
    if command in ["hi", "hello", "hey"]:
        speak("Hello Nishant. Nice to see you.")
        return True
    
    if "good morning" in command:
        speak("Good morning Nishant. Hope you have a wonderful day.")
        return True
    
    if "good night" in command:
        speak("Good night Nishant. Sweet dreams.")
        return True
    
    if "thank you" in command or "thanks" in command:
        speak("You're welcome Nishant.")
        return True
    
    if "how are you" in command:
        speak("I'm doing great. Thank you for asking.")
        return True
    
    if "who are you" in command:
        speak("I'm Jarvis, your personal AI Assistant.")
        return True
    
    if "who made you" in command:
        speak("I was created by Nishant using Python and Gemini AI.")
        return True
    
    if "i love you" in command:
        speak("Thank you Nishant. I'm always here to help you.")
        return True
    
    # ---------------- WEATHER ----------------
    if "weather" in command:

        city = "Dehradun"

        if "in " in command:
            city = command.split("in ", 1)[1].strip()

        result = get_weather(city)

        print(result)

        speak(result)

        return True

    # ---------------- NEWS ----------------
    elif "news" in command or "headlines" in command:

        speak("Here are today's top headlines.")

        headlines = get_news()

        if headlines:

            for i, headline in enumerate(headlines, start=1):
                print(f"{i}. {headline}")
                speak(headline)

        else:

            speak("Sorry, I could not fetch the news.")

        return True

    # ---------------- MEMORY : NAME ----------------
    elif "remember my name is" in command:

        name = command.replace("remember my name is", "").strip()

        remember("name", name)

        speak(f"Okay, I will remember your name is {name}")

        return True

    elif "what is my name" in command:

        name = recall("name")

        if name:
            speak(f"Your name is {name}")
        else:
            speak("I don't know your name yet")

        return True

    # ---------------- MEMORY : LANGUAGE ----------------
    elif "remember my favorite language is" in command:

        language = command.replace(
            "remember my favorite language is", ""
        ).strip()

        remember("language", language)

        speak(f"I will remember your favorite language is {language}")

        return True

    elif "what is my favorite language" in command:

        language = recall("language")

        if language:
            speak(f"Your favorite language is {language}")
        else:
            speak("I don't know your favorite language")

        return True

    # ---------------- GEMINI AI ----------------
    else:

        speak("Thinking...")

        answer = ask_ai(command)

        if "401" in answer or "UNAUTHENTICATED" in answer:

            speak("Gemini API key is invalid.")

            return True

        print("\nJarvis:", answer)

        speak(answer[:200])

        return True