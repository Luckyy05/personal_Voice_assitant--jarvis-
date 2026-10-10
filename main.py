import speech_recognition as sr
import webbrowser
import memory
import time
import pywhatkit
from speech import speak
import musiclibrary
from news import get_news
from groqai import ask_ai # by using groq api key we are using function of ai model
from memory import remember, get_memories
from weather import get_weather

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.non_speaking_duration = 0.3


def processcommand(c):
    print("Command received:", c)
    if"open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://www.google.com")
    elif"open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://www.facebook.com")

    elif"open youtube" in c.lower():
        speak("opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif"open Linkedin" in c.lower():
        speak("opening Linkedin")
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith("play"):
        speak("yes sir")
        song = c[5:].strip()  # Remove "play " from the beginning
        if not song:
            speak("please tell me the song")
            return

        speak(f"searching for {song}")

        if song in musiclibrary.music:
            webbrowser.open(musiclibrary.music[song.lower()])

        else:
            try:
                pywhatkit.playonyt(song)

            except Exception as error:
                print("Music playback error:", error)
                speak("Sorry sir, I couldn't play that song.")

    elif "news" in c.lower():
            headlines = get_news()

            speak("Here are the top 3 news headlines")
            print("headlines")

            for headline in headlines:
                speak(headline)

    elif "remember" in c.lower():
        memory_text = c.lower().replace("remember","",1).strip()

        remember(memory_text)
        speak(f"Okay sir, I will remember that {memory_text}")

    elif "weather" in c.lower():
        location = c.lower().replace("weather","",1).strip()

        if location:
            print(f"Fetching weather for {location}...")
            weather_info = get_weather(location)
            print("jarvis:",weather_info)
            speak(weather_info)

        else:
            print("no location")
            speak("please tell me a location")
        

    elif "what is my" in c.lower():
        search_text = c.lower().replace("what is my", "", 1).strip()

        memories = get_memories()

        for memory in memories:
            if search_text in memory.lower():
                speak(memory)
                print("Memory found:", memory)
                return

        speak("Sorry sir, I don't remember that.")


     # If no normal command matches, ask the AI
    else:
        speak("Let me think about that")# here it can provide answer to any else question but it will take some time to response as it uses a free tier api key 
        print("Sending question to AI...")

        answer = ask_ai(c)

        print("Jarvis:", answer)
        speak(answer)           

        return
if __name__ == "__main__":
    speak("Initializing Jarvis....")

    with sr.Microphone() as source:
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Calibration complete.")

    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
         
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening for jarivs ...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            word = recognizer.recognize_google(audio, language="en-IN")# as this recognizer recognize english-US, so we added "en-IN" for tuning and eassy recognition
            if "jarvis" in word.lower():
                print("jarvis activated")
                speak("yes sir")
                time.sleep(0.5)
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio, language="en-IN")# as this recognizer recognize english-US, so we added "en-IN" for tuning and eassy recognition
                    print("Command received:", command)
                    processcommand(command)
                



        except Exception as e:
            print("Error type:", type(e).__name__)
            print("Error message:", e)