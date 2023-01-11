from sqlite3.dbapi2 import _Statement
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess 
import ecapture as ec
import wolframalpha as wo
import json
import requests
import pyaudio
import audio as a
import speekmodule as sm
from ui_mygui  import play_gif
import pyautogui 
import psutil  
import PyPDF2
from PyQt5 import QtGui 
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow, QApplication,MainThread
import sys
import Speek 
import threading
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import winshell
import win32com.client as wincl


         

engine=pyttsx3.init('sapi5')  
voices=engine.getProperty('voices')
print("voices[0].id")
engine.setProperty('voice', 'voices[0].id')




def speak():
    engine.say('hello i am vrains ,i am what you call a visionary responsive artificial intelligence necessary system. now how can a help you')
    engine.runAndWait




def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
         speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening!")


 



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("i didnt hear you, please say that again")
            return "none"
        return statement

speak("")
wishMe()



if __name__=='__main__':

    while True:
        speak("what can i do for you?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "turn off" in statement:
            speak ('see you later!')
            break


        if 'wikipedia' in statement:
            speak('Searching the wiki')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=1000)
            speak("according to the wiki")
            speak(results)
        

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://youtube.com")
            speak("youtube is now open")
            time.sleep(3)
            





        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is open now")
            time.sleep(5)

            
        elif 'open github' in statement:
            webbrowser.open_new_tab("https://www.github.com")
            speak("Github is open now")
            time.sleep(5)


            
        elif 'open spotify' in statement:
            webbrowser.open_new_tab("https://www.spotify.com/")
            speak("spotify is open now")
            time.sleep(5)

if 'features' in statement:  
print('well my  features are i can open google chrome,i can open websites,a can tell you the date,i can check the cpu,i can use wikipedia to share information, i can lock window,i can empty the recycle bin  ')
speak('well my  features are i can open google chrome,i can open websites,a can tell you the date,i can check the cpu,i can use wikipedia to share information, i can lock window,i can empty the recycle bin,i can take a photo,i can also restart system, i can hibernate . ')


def cpu():
    
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()

    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    speak("battery is at ")
    speak(percent + "% | " + plugged)



    if 'open chrome' in statement:
        os.system('C://ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome.lnk')
        speak("Opening chrome")
    if 'close chrome' in statement:
        os.system('C://ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome.lnk')
        sys.exit
        speak("Closing chrome")


   
      
           
if 'lock window' in statement:
 speak("locking the device")
 ctypes.windll.user32.LockWorkStation()

elif 'shutdown system' in statement:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

elif 'empty recycle bin' in statement:
 winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
speak("Recycle Bin Recycled") 

elif "camera" in statement or "take a photo" in statement:
ec.capture(0, "vrains Camera ", "img.jpg")

elif "restart" in statement:
subprocess.call(["shutdown", "/r"])

if "hibernate" in statement or "sleep" in statement:
            speak("Hibernating")
            subprocess.call("shutdown / h")

