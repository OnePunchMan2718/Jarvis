import os
import speech_recognition as sr

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.......")
            query = command.recognize_google(audio, language='en=in')
            print(f"You Said: {query}")

        except :
            return "none"
        
        return query.lower()
    
while True:
    Wake_Up = takecommand()
    if 'wake up' in Wake_Up:
        os.startfile('C:\\Users\\anjis\\Desktop\\Jarvis\\Jarvis.py')

    else:
        print("Nothing............")
        