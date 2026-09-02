import speech_recognition as sr
import webbrowser
from speech import speak
import musiclibrary
from news import get_news

recognizer = sr.Recognizer()
def processcommand(c):
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
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
            headlines = get_news()

            speak("Here are the top 3 news headlines")
            print("headlines")

            for headline in headlines:
                speak(headline)

            return
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer() 
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)# by chatgpt(Calibrate for background noise)
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio, language="en-IN")# as this recognizer recognize english-US, so we added "en-IN" for tuning and eassy recognition
            if "jarvis" in word.lower():
                print("jarvis activated")
                speak("yes sir")
                # Listen for command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)# by chatgpt(Calibrate for background noise)
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio, language="en-IN")# as this recognizer recognize english-US, so we added "en-IN" for tuning and eassy recognition
                    processcommand(command)
                



        except Exception as e:
            print("Error type:", type(e).__name__)
            print("Error message:", e)