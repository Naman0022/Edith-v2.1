import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import vlc
import pafy
import urllib.request
import urllib.parse
import re
# from ecapture import ecapture as ec
import wolframalpha
import json
import requests
from englisttohindi.englisttohindi import EngtoHindi
from gtts import gTTS
from playsound import playsound
import keyboard
import pyautogui
import os.path


print("Loading packages...")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
speed = 180
engine.setProperty('rate', speed)
ask=0
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")

    else:
        speak("Good Evening")
        print("Good Evening")

    speak("How may I help you now")

def takeCommand():
    r=sr.Recognizer()
    #r.energy_threshold = 4000
    r.dynamic_energy_threshold = True
    r.pause_threshold = 1.0
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            print('Recognising...')
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry could not hear you. please say that again")
            return "None"

        audio=r.listen(source)
        return statement
def duringMusic():
    r = sr.Recognizer()
    # r.energy_threshold = 4000
    r.dynamic_energy_threshold = True
    r.pause_threshold = 1.0
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            print('Recognising...')
            statement = r.recognize_google(audio, language='hi-in')
            print(f"user said:{statement}\n")


        except Exception as e:
            return "None"

        audio = r.listen(source)
        return statement


print("Initialising...")
time.sleep(1)
speak("Hello")
speed = 180
engine.setProperty('rate', speed)
speak("I am Jarvis 2 point o")
speak("your personal assistant")
speed = 180
engine.setProperty('rate', speed)
wishMe()

if __name__=='__main__':

    while True:
        print('Initiate me using Initiate Command')
        start = takeCommand().lower()

        while 'jarvis' in start:
            speak('yes sir')
            statement=takeCommand().lower()

    # Interactive Commands
            if 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                query = statement.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2, auto_suggest=False)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'news' in statement:
                news = webbrowser.get(chrome_path).open_new("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)

            elif "where is" in statement:
                # data = statement.split(" ")
                stopwords = ['what', 'is', 'search', 'find', 'close friend', 'where', 'tell', 'dude']
                querywords = statement.split()
                resultwords = [word for word in querywords if word.lower() not in stopwords]
                statement = '+'.join(resultwords)
                stopwords = ['.']
                querywords = statement.split()
                resultwords = [word for word in querywords if word.lower() not in stopwords]
                statement1 = ''.join(resultwords)
                location = statement
                speak('here is' + location)

                webbrowser.get(chrome_path).open_new("https://www.google.nl/maps/search/" + location + "/&amp;/data=!3m1!1e3")
                # webbrowser.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;data=!3m1!1e3")
                time.sleep(5)
                # os.system("chrome-browser https://www.google.nl/maps/place/" + location + "/&amp;")

            elif "developer" in statement or "mode change" in statement:
                print("Developer Mode on...")
                speak("Developer Mode onn")
                def file_lengthy(fname):
                    with open(fname) as f:
                        for i, l in enumerate(f):
                            pass 
                    return i + 1

                tot = file_lengthy("assistant_(eng).py")
                print("Number of lines in the file: ", tot)
                time.sleep(0.5)
                speak('Please speak the condition')
                condition='none'
                while condition=='none':
                    condition = takeCommand().lower()
                speak('Please speak the Output of the following condition')
                output = takeCommand().lower()
                code = '''\n        elif '%s' in statement :\n            speak('%s!')\n\n''' % (condition, output)
                with open("assistant_(eng).py") as f:
                    lines = f.readlines()

                with open("assistant_(eng).py", "w") as f:
                    lines.insert(tot - 9, code)
                    f.write("".join(lines))
                    speak('code successfully updated')
                time.sleep(2)
                speak("do you want to restart project to save changes made")
                confirm = takeCommand().lower()
                if 'yes' in confirm or 'yep' in confirm:
                    speak("restarting project. please wait")
                    os.system('python assistant_(eng).py')
                    break
                else:
                    speak('the changes will be made on next rerun of the project')
                    speak("if you wish to rerun program then speak reload or restart in next input")

            elif 'ask' in statement:
                speak('I can answer to computational and geographical questions and what question do you want to ask now')
                question=takeCommand()
                app_id="R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)

            elif "weather" in statement:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                # speak("whats the city name")
                # city_name=takeCommand()
                city_name='ludhiana'
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()

                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    Celsius = current_temperature - 271
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in celsius unit is " +
                          str(round(Celsius,2)) + "°C"+
                          "\n humidity in percentage is " +
                          str(current_humidiy) +
                          "\n description  " +
                          str(weather_description))
                    print(" Temperature in celsius unit is " +
                          str(round(Celsius,2)) + "°C"+
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))

                else:
                    speak(" City Not Found ")

            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'play music' in statement or 'play song' in statement or 'play a song' in statement or 'play me a song' in statement:
                speak('please tell me name of any song you want me to play')
                s_name='none'
                while s_name=='none':
                    s_name = takeCommand().lower()
                print("Song name :",s_name)
                query_string = urllib.parse.urlencode({"search_query": s_name})
                html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query_string)
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                y_link = "https://www.youtube.com/watch?v=" + video_ids[0]
                print('YouTube link : ',y_link)
                url = y_link
                video = pafy.new(url)
                v_len = video.length
                best = video.getbest()
                playurl = best.url
                ins = vlc.Instance()
                player = ins.media_player_new()
                Media = ins.media_new(playurl)
                Media.get_mrl()
                player.set_media(Media)
                player.play()

                while True:
                    if keyboard.is_pressed('k'):
                        player.pause()
                        time.sleep(0.3)
                        if keyboard.is_pressed('k'):
                            player.play()
                            time.sleep(0.3)

                    elif keyboard.is_pressed('esc') or keyboard.is_pressed('q'):
                        player.stop()
                        time.sleep(1)
                        break

            elif "screenshot" in statement:
                while True:
                    # print(' first while loop started')
                    speak('please press "s" key when you want me to take a screen shot...')
                    speak('and press escape key when you want to exit screenshot mode...')
                    # screen_in=takeCommand().lower()
                    if keyboard.is_pressed('s'):
                        # print('if s started')
                        screenshot = pyautogui.screenshot()
                        file_name = 1
                        while True:
                            checkFile = "C:\\Users\\Admin\\Pictures\\Screenshots\\Screenshot (" + str(
                                file_name) + ").png"
                            if os.path.isfile(checkFile):
                                print("C:\\Users\\Admin\\Pictures\\Screenshots\\Screenshot (" + str(
                                    file_name) + ").png exists")
                                file_name = file_name + 1
                            else:
                                print('do not exists ' + str(file_name))
                                screenshot.save(
                                    "C:\\Users\\Admin\\Pictures\\Screenshots\\Screenshot (" + str(file_name) + ").png")
                                print("screenshot saved as Screenshot (" + str(file_name) + ").png")
                                break
                    elif keyboard.is_pressed('esc'):
                        break

            elif "reload" in statement or 'restart' in statement:
                speak("restarting project. please wait")
                os.system('python assistant_(eng).py')
                break
    # Open Commands

            elif 'open' in statement:
                if 'open youtube' in statement:
                    webbrowser.get(chrome_path).open_new("https://www.youtube.com")
                    # webbrowser.open_new_tab("https://www.youtube.com")
                    speak("youtube is open now")
                    time.sleep(5)

                elif 'open google' in statement:
                    # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
                    webbrowser.get(chrome_path).open_new("https://www.google.com")
                    # webbrowser.open_new_tab("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(5)

                elif 'open gmail' in statement:
                    webbrowser.get(chrome_path).open_new("gmail.com")
                    # webbrowser.open_new_tab("gmail.com")
                    speak("Google Mail open now")
                    time.sleep(5)

                elif "open stackoverflow" in statement:
                    webbrowser.get(chrome_path).open_new("https://stackoverflow.com/login")
                    speak("Here is stackoverflow")

    # Casual Commands

            elif 'thank you' in statement:
                speak('your welcome')
                print('☺')

            elif '2 point o' in statement or 'version 2' in statement or 'version 1' in statement :
                speak('I am the recreation of original assistant made by my creators')
                speak('the original creation was destroyed due to some issues i dont know about')

            elif "close" in statement or "quit" in statement or "stop" in statement:
                speak('your assistant Jarvis is shutting down')
                speak('Good bye')
                print('Good bye ☺')
                break

            elif 'what can you do' in statement:
                speak('I can tell you weather forecast today')
                speak('or open any application')
                speak('or can just talk to you as your friend')

            elif 'who are you' in statement:
                speak('I am Jarvis version 2 point o . At your service')
                print()

            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by my creator Naman")
                print('''
                    Name: Naman Punj
                    Currently at: Studying in Class 12
                    Date: 
                    ''')

            elif "how are you" in statement :
                speak('i am fine sir thankyou!')
                print('☺')

            elif 'feel happy' in statement :
                speak('me too. its an excellent day!')

            elif 'feel lonely' in statement :
                speak('i am here for you!')

            elif 'i am sad' in statement :
                speak('dont be. i can make you laugh with my jokes .or you can sing music along with me!')

            elif "search"  in statement:
                statement = statement.replace("search", "")
                webbrowser.get(chrome_path).open_new(statement)
                time.sleep(5)

            elif "none" in statement:
                ask=ask+1
                if ask==4:
                    True
                else:
                    break

    # Windows Commands
            elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "shut down my pc" in statement or "shutdown my pc" in statement or "shut down pc" in statement or "shutdown this pc" in statement or "shut down" in statement:
                speak("Ok , your pc will shot down in 30 sec .Make sure you exit from all applications before leaving")
                os.system('shutdown /p /f')

            elif "restart my pc" in statement or "restart pc" in statement or "restart this pc" in statement:
                speak("Ok , your pc will shot down in 30 sec .Make sure you exit from all applications before leaving")
                os.system("shutdown /r")

time.sleep(3)