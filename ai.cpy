import mysql.connector as mysql
import pyttsx3
from datetime import datetime
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init("sapi5")

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def database():
    global mysqldb
    mysqldb = mysql.connect(host = "localhost", user =  "hacker07", passwd =  "admin1234", db = "ai")

def execute(query):
    cursor = mysqldb.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def master():
    global username 
    username = execute("select name from ai.ai_account;")
    for i in range(2):
        username = username[0]

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    database()
    master()
    if hour <= 12:
        speak(f"Good morning {username}")
    elif hour > 12 and hour < 18:
        speak(f"Good afternoon {username}")
    else :
        speak(f"Good night {username}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        speech = r.recognize_google(audio, language="en-in")
        print(f"User said {query}\n")
    
    except Exception as err:
        # print(err)
        speak("Say that again plz.....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    query = takecommand().lower()

    if 'open google' in query:
        webbrowser.open("google.com")