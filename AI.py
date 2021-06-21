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

def main():
    while True:
        # command = Mic(mic)
        command = input("command :\t")
            
        if "bye" in command:
            engine("goodbye, freind")
            exit()
        elif "instagram" in command:
            insta.instagram()
        elif "messenger" in command:
            mess.messenger()
        elif "wikipedia" in command:
            wiki.Wikipedia(command, engine)

if __name__ == "__main__":
    main()
