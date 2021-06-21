import pyaudio
import wave
import speech_recognition as sr
import psycopg2
import pyttsx3

connection = psycopg2.connect(
    database="ai",
    user="AI",
    password="securep@ss1234",
    host="localhost",
    port=5432
)

speech = sr.Recognizer()
mic = sr.Microphone(device_index=0)

def engine(speak):
    Engine = pyttsx3.init()
    Engine.say(speak)
    Engine.runAndWait()

def Mic(mic):
    try:
        with mic as source:
            print("listening..... ")
            speech.pause_threshold = 1
            audio = speech.listen(source, timeout=2, phrase_time_limit=3)
            command = speech.recognize_google(audio, language='en-in')
            command = command.lower()
        return command
    except:
        return "Sorry, could'nt recognize ..."


def main():
    while True:
        command = Mic(mic)
        print(command)
        engine(command)
        
        if command == "exit":
            engine("goodbye, freind")
            exit()
        elif command == "instagram":
            from scraping import instagram
        elif command == "messenger":
            from scraping import messenger
        


if __name__ == "__main__":
    main()
