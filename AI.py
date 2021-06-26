import pyaudio
import wave
import psycopg2
import pyttsx3
import wikipedia
import multiprocessing
import scraping.instagram as insta
import scraping.messenger as mess
import wiki

connection = psycopg2.connect(
    database="ai",
    user="AI",
    password="securep@ss1234",
    host="localhost",
    port=5432
)


def engine(speak):
    Engine = pyttsx3.init()
    Engine.setProperty('rate', 125)
    Engine.setProperty('volume',2.0) 
    Engine.say(speak)
    Engine.runAndWait()

def Process(task):
    branch = multiprocessing.Process(target=task)
    branch.start()
    branch.join()    

def main():
    while True:
        # command = Mic(mic)
        command = input("command :\t")
            
        if "bye" in command:
            Process(engine("goodbye, freind"))
            exit()
        elif "instagram" in command:
            Process(insta.instagram(engine))
        elif "messenger" in command:
            Process(mess.messenger())
        elif "wikipedia" in command:
            Process(wiki.Wikipedia(command, engine))

if __name__ == "__main__":
    Process(main())
