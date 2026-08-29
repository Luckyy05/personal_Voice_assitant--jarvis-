import speech_recognition as sr
import webbrowser
from speech import speak


recognizer = sr.Recognizer()
def processcommand(c):
    if"open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://www.google.com")
        



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer() 
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=4, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                print("jarvis activated")
                speak("yes sir, jarvis is activated , what can i do for you ")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)
                



        except Exception as e:
            print("Error; {0}".format(e))