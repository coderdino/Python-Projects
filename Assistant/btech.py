#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vaibhav2
#
# Created:     10/04/2021
# Copyright:   (c) Vaibhav2 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
from datetime import date
import datetime
import webbrowser
import subprocess
import pyttsx3
import sys
import wikipedia
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 165)
engine.setProperty('volume', 10)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Starting all services")
    speak("Assistance Mode Activated")
    speak("btech.py Activated")
    speak("config.jrvis Started")
    speak("Starting...")
    speak("What is your name: ")
    name = input("What is your name: ")

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f'Good Morning {name}!')

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon {name}!")

    else:
        speak(f"Good Evening {name}!")

    speak("I am btech. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()

    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            q = input("Whom do you wanna search: ")
            query = query.replace("wikipedia", q)
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "stop" in query:
            speak("Stopping all services")
            speak("Assistance Mode deactivated")
            speak("btech.py Deactivated")
            speak("config.jrvis stopped")
            speak("Shutting down")
            sys.exit()

        elif "shut up" in query:
            speak("Stopping all services")
            speak("Assistance Mode deactivated")
            speak("btech.py Deactivated")
            speak("config.jrvis stopped")
            speak("Shutting down")
            sys.exit()

        elif "hi" in query:
            speak("hi")
            speak("Next command sir:")

        elif "calculate" in query:
            speak("Next command sir:")
            import Calculator

        elif "news" in query:
            speak("opening bbc news")
            webbrowser.open('https://www.bbc.co.uk/news')
            speak("Next command sir:")

        elif "game" in query:
            speak("Launching google games")
            webbrowser.open('https://www.google.com/search?safe=strict&sxsrf=ALeKk01Ezw6ov7NZVLJBvcsWLZrzXEmaCg%3A1586617746287&ei=kt2RXriPEeHA8gKOiavgCg&q=snake&oq=snake&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIECCMQJzIFCAAQkQIyBAgAEEMyBAgAEEMyBQgAEJECMgcIABCDARBDMgQIABBDMgQIABBDMgQIABBDOggIABCDARCRAjoFCAAQgwE6BwgAEBQQhwJKGAgXEhQwZzEyN2c3MmcxMDJnMTMyZzE3MEoPCBgSCzBnMWcxZzFnMWcxUIdcWMlnYMJqaABwAHgAgAGhAYgBogSSAQMyLjOYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwi4oKXZ0-DoAhVhoFwKHY7ECqwQ4dUDCAw&uact=5')
            speak("Next command sir:")

        elif "google maps" in query:
            speak("launching")
            speak("What do you want to search in google maps?")
            place = input()
            tabUrl = 'https://www.google.com/maps/search/';
            webbrowser.open(tabUrl + place)
            speak("Next command sir:")

        elif "date" in query:
            today = date.today()
            speak(today)
            print(today)
            speak("Next command sir:")

        elif "youtube" in query:
            speak("what do you want to search in youtube?")
            q = input()
            tabUrl = 'https://www.youtube.com/results?search_query=';
            webbrowser.open(tabUrl + q)
            speak("Next command sir:")

        elif "inbox" in query:
            n = input("Who's account is this?")

            if n == "school":
                speak("Launching school inbox.")
                webbrowser.open('https://outlook.office365.com/mail/inbox')
                speak("Next command sir:")

            elif n == "normal":
                speak("launching normal inbox")
                webbrowser.open('https://mail.google.com/mail/u/1/?ogbl#inbox')
                speak("Next command sir:")

        elif "translate" in query:
            speak("launching google translate")
            webbrowser.open('https://translate.google.co.uk/')
            speak("Next command sir:")

        elif "homeworks" in query:
            speak("opening google classroom")
            webbrowser.open('https://classroom.google.com/u/0/h')
            speak("Next command sir:")

        elif "see world" in query:
            speak("opening google earth")
            webbrowser.open("https://earth.google.com/web/@0,7.658201,0a,22251752d,35y,0h,0t,0r/data=KAE")
            speak("Next command sir:")

        elif "measure"  in query:
            speak("Launching unit converter")
            webbrowser.open('https://www.unitconverters.net/')
            speak("Next command sir:")

        elif "call" in query:
            speak("opening Skype")
            webbrowser.open("https://web.skype.com/")
            speak("Next command sir:")

        elif "message" in query:
            speak("opening whatsapp web")
            webbrowser.open("https://web.whatsapp.com/")
            speak("Next command sir:")

        elif "remind" in query:
            speak("What shall I remind you about?")
            text = str(input("What shall I remind you about?"))
            speak("In how many minutes?")
            local_time = float(input("In how many minutes?"))
            local_time = local_time * 60
            time.sleep(local_time)
            speak(text)
            speak("Next command sir:")

        elif "passwords" in query:
            speak("Sorry, I cannot do that because of security reasons")
            speak("Next command sir:")

        elif "thank you" in query:
            speak("I am always there for you!")
            speak("Next command sir:")

        elif "friend" in query:
            speak("You!")
            speak(name)
            speak("Next command sir:")

        elif "Hey" in query:
            speak(name)
            speak("What can I do for you?")
            speak("Next command sir:")

        else:
            speak("Opening result in google.")
            tabUrl = 'https://www.google.com/search?q=';
            webbrowser.open_new_tab(tabUrl)
            speak("Next command sir:")
