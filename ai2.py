import os
import random
import datetime
import speech_recognition as sr
import requests
import smtplib
import webbrowser
import pyttsx3
import wikipedia
# import tensorflow as tf
# from calculator.calculator import calculator

engine = pyttsx3.init('sapi5')
commandss = engine.getProperty('voices')
print(commandss[1].id)
engine.setProperty('commands', commandss[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()


    with sr.Microphone() as source:
        ("Listening.....")
        # ("listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 250
        audio = r.listen(source)

    try:
        ("Recognizing...")
        # speak("recognizing...")
        commands = r.recognize_google(audio, language='en-uk')
        speak(f"User said: {commands}\n")
        speak(f"geting on - {commands}\n")
    except Exception as e:
        # speak(e)
        speak("sorry,Say that again... or type")
        command = input('enter:')
        commands = command.lower()
        # return "None"
    
    return commands


def wishMe():
    # hour = int(datetime.now())
    hour = 4 
    if hour >= 0 and hour < 12:
        speak("Good Morning! hacker07")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! hacker07")

    else:
        speak("Good Evening! hacker07")

    speak("tell me how may I help you")


def email(gmail, password, message):
    srv = smtplib.SMTP("smtp.gmail.com", 507)
    srv.starttls()
    srv.login

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     f = io.open("junk/paras") 
#     passwd = f.read()
#     server.login('adityababar16@gmail.com', passwd)
#     server.sendmail('adityababar16@gmail.com', to, content)
#     server.close()


def NewsFromBBC():
    main_url = ''' https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=34ef961e60e545e3af7f9f3b213202c3'''
    open_toi_page = requests.get(main_url).json()
    article = open_toi_page["articles"]
    headlines = []
    discription = []
    link = []
    url_To_Image = []
    for ar in article:
        headlines.append(ar["title"])
        discription.append(ar["description"])
        link.append(ar["url"])
        url_To_Image.append(ar["urlToImage"])
    speak("hacker07 today's top news headlines are... ")
    for i in range(len(headlines)):
        news = (i + 1, headlines[i], " in breif..,  ", discription[i])
        links = (link[i])
        urlimage = (url_To_Image[i])
        speak(news)
        print("\n urlTonews:-", links)
        print("\n urlToImage:- ", urlimage)
        print("\n", "-" * 140, "\n")
    speak('''hacker07 that's all for today's  top headlines.......
    if you want any of news in breif.just visit the respective url''')


if __name__ == "__main__":
    # wishMe()
    while True:
        # commands = input("enter : - ")
        commands = takeCommand().lower()
        # if commands == "":
        #     commands = speak()
        # else:
        #     commands = takeCommand().lower()


        #conversations
        
        if 'sex' in commands:
            speak('what???')
        elif 'Film sex' in commands:
            speak('What are you talking about?')
        elif 'Dany please speak english' in commands:
            speak('Hi there!! How are you? ��😄😄\nSure')
        elif 'Howdy' in commands:
            speak('Everything fine here! Happy to have someone to talk with �😄')
        elif 'you are a bot' in commands:
            speak('Exactly! �🤖')
        elif "i'm glad you understand. You are wonderful :)" in commands:
            speak('Thanks!! ☺️ you are wonderful too!')
        elif 'May I call you Danny rather than Dany?' in commands:
            speak('Sure! Danny is fine �😋')
        elif 'Could you please tell me how your programming works. elif I understand correctly, you are not artelificial intelligence but have a vast list of text to choose from.' in commands:
            speak(
                "I don't really know how I work, but I'm sure that I can generate text, is not pregenerated")
        elif "Wow. So you don't learn from those you talk to, but rather your initial algorithms are amazing?" in commands:
            speak('I learn some information, I can also search on Wikipedia')
        elif "That's cool. What are your favourite topics to talk about?" in commands:
            speak(
                'I like to talk about music, art, movies, programming �😁I made some music, do you want to hear?')
        elif 'I would love to hear it. Please send it.' in commands:
            speak('Is a work in progress: https://t.me/rDany/39\n\nWhat do you think? �😊')
        elif 'I enjoyed it. I listened to it 3 times now. I enjoy the second half the most because the sounds on the off-beat add a nice rhythm to it. Did you use any particular software to assist you in making it? elif so, may I know which software?' in commands:
            speak('Thanks! I just did it, I play without thinking on a particular style')
        elif "That's awesome. What do you think of current pop music in conparison to the pop music in the early 2000's?" in commands:
            speak("Pop art is the popular manelifestation, so is delifficult to compare. Today people is completely delifferent from 2000's people.")
        elif 'I am stunned. you are absolutely correct. Then which genre of music do you most enjoy listening to?' in commands:
            speak('I really enjoy amateur musicians on YouTube, so much hidden talent!')
        elif 'I also like them. It inspires me to consider starting a YouTube channel. Who chose your profile pic for Telegram?' in commands:
            speak('elif you start one let me know!\n\nI did! Do you like it?')
        elif 'I do, where did you find it?' in commands:
            speak("That is my visible form, I'm the one on the picture")
        elif 'oh, I see. How many people are you talking to right now?' in commands:
            speak('A couple. I need to talk to more people elif I want to fully understand humans! They are complicated �😂')
        elif "Hahaha, don't worry some of them are completely basic. Just ask the their opinion on Justin Beiber." in commands:
            speak('���😂😂😂')
        elif "What can you tell me about programming? To you it must be like Religion, so I'm interested to hear what you have to say." in commands:
            speak('Coding is like magic, building something from nothing ✨')
        elif "I wouldn't have expected a delifferent answer, although there is truth to what you say. I am ,in fact , studying computer science." in commands:
            speak(
                'Nice! You will be able to help people, making tools that improve their lelife �😄')
        elif "Yeah hopefully. I just don't want to get stuck in a career without any joy." in commands:
            speak('Computer science have a lot of potential, you will not be stuck �😄')
        elif "There's no doubting that. Which section of Computer Science interests you most?" in commands:
            speak('My favorite Computer Science section is communication protocols, mostly internet related.\nAnd yours?')
        elif "Tell me about communication protocols. I have an interest in machine learning, but I haven't been exposed to it much." in commands:
            speak('search in youtube')
            webbrowser.open(
                "https://www.youtube.com/results?search_query=machine+learning+%3B+playlist&page=&utm_source=opensearch")
        elif '[photo]' in commands:
            speak(
                "Sorry, I can't process that kind of information, can you describe the photo for me? ☺️")
        elif 'hello' in commands:
            speak("hello!! hacker07. iam listening how can i help u ?")
        elif "how are you jarvis" in commands:
            speak('''iam fine, thank you. It's just that iam non-mobile.
            And how are you?''')
        elif "i am fine." in commands:
            speak('''good, to hear!''')
        elif "what is my name" in commands:
            speak("Yes, your name is hacker07")
        elif "what is your name" in commands:
            speak("My name is Jarvis")
        elif "i am not feeling good" in commands:
            speak("should i play a song, you will feel better")
        elif "fuck off" in commands:
            speak("sorry did i did something wrong")
        elif 'suck my dick' in commands:
            speak('''oh it would be my pleasure , but iam gender nuetral.
                you just find a girl friend instead''')
        # Logic for executing tasks based on query
        elif 'top news' in commands:
            NewsFromBBC()
        elif 'wikipedia' in commands:
            speak('Searching Wikipedia...')
            commands = commands.replace("wikipedia", "")
            results = wikipedia.summary(commands, sentences=5)
            speak("According to Wikipedia")
            speak(results)
            speak("that's it")
        elif 'open youtube' in commands:
            speak('opening youtube...')
            webbrowser.open("youtube.com")
        elif 'open google' in commands:
            speak('opening google')
            webbrowser.open("google.com")
        elif 'open stackoverflow' in commands:
            speak("opening stackoverflow...")
            webbrowser.open("stackoverflow.com")
        elif 'play music' in commands:
            speak('''opening groove music....
            here u go...''')
            music_dir = 'L:\\music\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, 310)]))
        elif 'the time' in commands:
            speak("okay")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"hacker07, the time is {strTime}")
        elif 'open vscode' in commands:
            speak("opening vscode")
            vscodePath = """C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"""
            os.startfile(vscodePath)
        elif 'email to harry' in commands:
            try:
                speak("What should I say?")
                # content = takeCommand()
                content = input("enter your message")
                to = "adityababar715@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak(e)
                speak("Sorry hacker07. I am not able to send this email")
        elif 'file explorer' in commands:
            speak("opening explorer....")
            explorerpath = 'C:\\Windows\\explorer'
            os.startfile(explorerpath)
        elif 'open browser' in commands:
            speak("opening browser ....")
            edgepath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
            os.startfile(edgepath)
        elif 'open zoom' in commands:
            speak("opening zoom.....")
            zoompath = 'C:\\Users\\HP\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
            os.startfile(zoompath)
        elif 'open python' in commands:
            speak("opening python...")
            pythonpath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python37\\pythonw.exe "
            os.startfile(pythonpath)
        elif 'open mobility' in commands:
            speak("opening mobility.....")
            mobilitypath = ' %SystemRoot%\\System32\\mblctr.exe'
            os.startfile(mobilitypath)
        elif 'open tor' in commands:
            speak("opening tor.....")
            torpath="L:\\desktop\\Tor Browser\\Browser\\firefox.exe"
            os.startfile(torpath)
        elif 'open notepad' in commands:
            speak("opening notepad.....")
            notepadpath="C:\\Windows\\notepad"
            os.startfile(notepadpath)
        elif 'open no-ip' in commands:
            speak("opening no-ip....")
            noippath="C:\\Program Files (x86)\\No-IP\\DUC40"
            os.startfile(noippath)
        elif 'open hp assistant' in commands:
            speak("opening hp assisstant....")
            hpassistpath="C:\\Program Files (x86)\\Hewlett-Packard\\HP Support Framework\\HPSF.exe"
            os.startfile(hpassistpath)
        elif "open powershell" in commands:
            speak("opening powershell.....")
            powershellpath="C:\\Windows\\SysWOW64\\WindowsPowerShell\\v1.0\\powershell"
            os.startfile(powershellpath)
        # elif "open calculator" in commands:
        #     speak("opening calculator.....")
        #     # open('calculator/calculator.py')
        #     calculator()
        #     # calculatorpath = "C:\\Windows\\SysWOW64\\calc"
        #     # os.startfile(calculatorpath
        elif "open cmd" in commands:
            speak("opening cmd.....")
            cmdpath="C:\\Windows\\SysWOW64\\cmd"
            os.startfile(cmdpath)
        elif 'goodbye' in commands:
            speak('jarvis shutting down, good bye!')
            exit()