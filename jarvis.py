import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import requests
from bs4 import BeautifulSoup
import socket
import subprocess
import time
import psutil
import pyautogui
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis Please tell me how can i help you")

def cpu():
    usage = psutil.cpu_percent()
    speak("CPU is at " + str(usage) + "%")
    print(usage)
    battery = str(psutil.sensors_battery())
    speak("Battery is at " + battery)
    print(battery)


import speech_recognition as sr


def takeCommand():
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
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            webbrowser.open("google.com")  
             

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code'in query:
            codePath = "C:\\Users\\shrut\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

        
        elif 'send message' in query:
            pywhatkit.sendwhatmsg("+918296279546","hii how r u?",8,34)


        elif 'play songs on youtube' in query:
            pywhatkit.playonyt("Perfect")


        elif 'temperature' in query:
            search = 'temperature in belgavi'
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        elif 'ip'in query:
            host = socket.gethostname()
            ip = socket.gethostbyname(host)
            print(ip)
            speak("your ip address is" +ip)

        elif 'bmi' in query:
            speak("please tell your height in centimeters")
            height = takeCommand()
            speak("Please tell your weight in kilograms")
            weight = takeCommand()         
            if weight and weight.strip().replace('.', '', 1).isdigit():
                weight = float(weight)
            if height and height.strip().replace('.', '', 1).isdigit():
                height = float(height) / 100 
                BMI = weight / (height * height)
                print(f"BMI: {BMI}")
            else:
                print("Invalid input. Please enter a numeric value for height.")
                speak("Your body mass index is")
            if(BMI>0):
                if(BMI<=16):
                    speak("you are severly underweight")
                elif(BMI<=18.5):
                    speak("you are underweight")
                elif(BMI<=25):
                    speak("you are healthy ")
                elif(BMI<=30):
                    speak("you are overweight")
                else:
                    speak("your overweight")
            else:
                speak("enter valid details")

        elif 'shutdown' in query or 'turnoff' in query:
            speak('Hold on a second sir! Your system is on a way to shutdown')
            speak('Make sure all of your applications are closed')
            time.sleep(5)
            subprocess.call(['shutdown','/s'])
        
        elif 'restart' in query:
             subprocess.call(['shutdown','/r'])
        
        elif 'switch window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(5)
            pyautogui.keyUp('alt')

        elif 'cpu status' in query:
            cpu()

        

        elif 'exit' in query:
            speak("Thankyou for using me sir, have a good day")
            sys.exit()

        

        


     



        

        




       

        
        

