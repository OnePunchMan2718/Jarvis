import pyttsx3
import pyaudio
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import keyboard
import pyjokes
import datetime
import requests
import speedtest

from PyDictionary import PyDictionary as Dictionary
from playsound import playsound
from googletrans import Translator
from bs4 import BeautifulSoup
from pywikihow import search_wikihow

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',190)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()

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

def TaskExe():

    Speak("Hello, I Am Jarvis Sir!")
    Speak("How Can I Help You Sir?")

    def Music():
        Speak("Tell Me The Name Of The Song!!")
        musicname = takecommand()

        if 'fairytale' in musicname:
            os.startfile('[path]')

        else:
            pywhatkit.playonyt(musicname)

        Speak("Your Song Has Been Started! , Enjoy Sir!!")

    def Whatsapp():
        Speak("Tell Me The Name Of The Person!")
        name = takecommand()

        if '[Name]' in name:
            Speak("Tell Me The Message!")
            msg = takecommand()
            Speak("Tell Me The Time Sir!!")
            Speak("Time In Hour!")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91[Nummber]",msg,hour,min,20)
            Speak("Okay Sir! , Sending Whatsapp Message!!")

        elif '[Name]' in name:
            Speak("Tell Me The Message!")
            msg = takecommand()
            Speak("Tell Me The Time Sir!!")
            Speak("Time In Hour!")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91[Number]",msg,hour,min,20)
            Speak("Okay Sir! , Sending Whatsapp Message!!")

        elif '[Name]' in name:
            Speak("Tell Me The Message!")
            msg = takecommand()
            Speak("Tell Me The Time Sir!!")
            Speak("Time In Hour!")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91[Number]",msg,hour,min,20)
            Speak("Okay Sir! , Sending Whatsapp Message!!")

        else:
            Speak("Tell Me The Phone Number!")
            phone = int(takecommand())
            ph = '+91' + phone
            msg = takecommand()
            Speak("Tell Me The Time Sir!!")
            Speak("Time In Hour!")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            Speak("Okay Sir! , Sending Whatsapp Message!!")

    def OpenApps():
        Speak("Okay Sir! , Wait A Second!")
        
        if 'visual studio code' in query:
            os.startfile("[Path]")

        elif 'chrome' in query:
            os.startfile("[Path]")

        elif 'whatsapp app' in query:
            webbrowser.open('https://web.whatsapp.com/')

        elif 'insta' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Your Command Has Been Completely Executed!")

    def CloseApps():
        Speak("Okay Sir! , Wait A Second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'visual studio code' in query:
            os.system("TASKKILL /F /im Code.exe")

        elif 'whatsapp app' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'insta' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")

        Speak("Your Command Has Been Completely Executed!")

    def YoutubeAutomation():
        Speak("What is your command?")
        comm = takecommand()
        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'flim mode' in comm:
            keyboard.press('t')
        
        elif 'exit full mode' in comm:
            keyboard.press('esc')

        Speak("Done Sir!")

    def ChromeAutomation():
        Speak("What is your command?")
        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')

    def Dict():
        Speak("Activated Dictionary")
        Speak("Tell Me The Word Sir!")
        prob = takecommand()

        if 'meaning' in prob:
            prob = prob.replace("what is the meaning of","")
            result = Dictionary.meaning(prob)
            Speak(f"The Meaning For {prob} is {result}")

        elif 'synonym' in prob:
            prob = prob.replace("what is the synonym of","")
            result = Dictionary.synonym(prob)
            Speak(f"The Synonym For {prob} is {result}")

        elif 'antonym' in prob:
            prob = prob.replace("what is the antonym of","")
            result = Dictionary.antonym(prob)
            Speak(f"The Antonym For {prob} is {result}")

        Speak("Exited Dictionary Sir!")
            
    def screenshot():
        Speak("Okay Sir! , What Should I Name That File ?")
        path = takecommand()
        path1name = path + ".png"
        path1 = '[Path]' + path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile('[Path]')
        Speak("Here Is Your Screenshot")

    def TakeTran():
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

    def Tran():
        Speak("Tell Me The Line! Sir!")
        line = TakeTran()
        traslate = Translator()
        result = traslate.translate(line)
        Text = result.text
        Speak("The Translation For This Line Is: " + Text)

    def Temp():
        search = "Temperature Of Kolkata"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_ = "BNeawe").text
        Speak(f"The Temperature Outside Is {temperature} celcius")
        
    def SpeedTest():
        
        Speak("Cheaking speed........")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctUpload = int(uploading/800000)

        if 'uploading' in query:
            Speak(f"The Uploading Speed Is {correctUpload} mbp/s")

        elif 'downloading' in query:
            Speak(f"The Downloading Speed Is {correctDown} mbp/s")

        else:
            Speak(f"The Downloading Speed Is {correctDown} mbp/s & Uploading Speed Is {correctUpload} mbp/s")

    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir!!, I am Jarvis.")
            Speak("Your Personal AI Assistant!")
            Speak("How May I Help You?")
        
        elif 'how are you' in query:
            Speak("I am Fine Sir!")
            Speak("What's About You?")

        elif 'i am fine' in query:
            Speak("That's Good To Hear Sir!")
            Speak("How Can I Help You Sir?")

        elif 'go to sleep' in query:
            Speak("Ok Sir!, You can Call Me Anytime!")
            Speak("Just Say Wake Up Jarvis!")
            break

        elif 'youtube search' in query:
            Speak("Okay Sir, This Is What I Found For Your Search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!!")

        elif 'google search' in query:
            Speak("This Is What I Found For Your Search Sir!!")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done Sir!!")

        elif 'website' in query:
            Speak("Okay Sir, Launching....... ")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!!")

        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!!")
            name = takecommand()
            web = 'https://www.' + web + '.com'
            webbrowser.open(web)
            Speak("Done Sir!!")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia ..........")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'whatsapp message' in query:
            Whatsapp()

        elif 'screenshot' in query:
            screenshot()

        elif 'open visual studio code' in query:
            OpenApps()
        
        elif 'open brave' in query:
            OpenApps()
        
        elif 'open whatsapp app' in query:
            OpenApps()
        
        elif 'open insta' in query:
            OpenApps()
        
        elif 'open maps' in query:
            OpenApps()
            
        elif 'open youtube' in query:
            OpenApps()

        elif 'close visual studio code' in query:
            CloseApps()
        
        elif 'close brave' in query:
            CloseApps()
        
        elif 'close whatsapp app' in query:
            CloseApps()
        
        elif 'close insta' in query:
            CloseApps()
        
        elif 'close maps' in query:
            CloseApps()
            
        elif 'close youtube' in query:
            CloseApps()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'flim mode' in query:
            keyboard.press('t')
        
        elif 'exit full mode' in query:
            keyboard.press('esc')

        elif 'youtube tool' in query:
            YoutubeAutomation()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'brave automation' in query:
            ChromeAutomation()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my word' in query:
            Speak("Listening Your Words Carefully Sir!")
            jj = takecommand()
            Speak(f"You Said : {jj}")

        elif 'my location' in query:
            Speak("Okay Sir! Wait A Seacond Sir!")
            webbrowser.open('https://www.google.com/maps/')

        elif 'dictionary' in query:
            Dict()
        
        elif 'alarm' in query:
            Speak("Enter The Time! Sir!")
            Speak("In 24h Format")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time To Wake Up Sir!")
                    playsound('.External/Alarm.mp3')
                    Speak("Alarm Closed!")

                elif now>time:
                    break

        elif 'translator' in query:
            Tran()

        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("jarvis","")
            Speak("You Told Me To Remind You That : " + rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query:
            remember = open('data.txt','r')
            Speak("You Told Me To Remember That " + remember.read())

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("what is","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This What I Found On The Web Sir!!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable Data Available")

        elif 'temperature' in query:
            Temp()

        elif 'internet speed' in query:
            SpeedTest()

        elif 'uploading speed' in query:
            SpeedTest()

        elif 'downloading speed' in query:
            SpeedTest()

        elif 'how to' in query:
            Speak("Getting Data From The Internet, Sir!")
            op = query.replace("jarvvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

TaskExe()  