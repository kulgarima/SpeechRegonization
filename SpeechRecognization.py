import speech_recognition as sr
import webbrowser
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("you said...",text)
        webbrowser.open('https://www.google.co.in/search?q='+text)
    except:
        print("Could not understand")
