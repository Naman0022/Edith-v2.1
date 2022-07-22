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
import wolframalpha
import requests
import smtplib
import keyboard
# language change
from gtts import gTTS
from deep_translator import GoogleTranslator
from playsound import playsound

print("Loading packages...")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')


speed = 180
engine.setProperty('rate', speed)
language = 'hi'

def speak(t_text):
    translated = GoogleTranslator(source='auto', target='hi').translate(t_text)
    gTTS(text=translated, lang=language, slow=False).save("welcome.mp3")
    playsound("welcome.mp3")
    os.remove("welcome.mp3")

def speak_e(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        t_text="Good Morning"

    elif hour>=12 and hour<18:
        t_text="Good Afternoon"

    else:
        t_text="Good Evening"

    translated = GoogleTranslator(source='auto', target='hi').translate(t_text)
    print(translated)
    speak(t_text)

    speak("how do i help")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('namanpunj1947@gmail.com', 'n4e616d616e')
    server.sendmail('namanpunj1947@gmail.com', to, content)
    server.close()

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
            statement1=r.recognize_google(audio,language='hi-in')
            print(f"user said:{statement1}\n")
            statement = GoogleTranslator(source='auto', target='en').translate(statement1).lower()
            print(statement)

        except Exception as e:
            speak("Sorry i can not hear you. please say that again")
            return "None"

        audio=r.listen(source)
        return statement

def takeCommand1():
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
            statement1 = r.recognize_google(audio, language='hi-in')
            print(f"user said:{statement1}\n")
            statement = GoogleTranslator(source='auto', target='en').translate(statement1)

        except Exception as e:
            return "None"

        audio = r.listen(source)
        return statement


print("Initialising...")
time.sleep(1)
speak("Hello")
speak("my name is Zorru")
speak("your personal assistant")
wishMe()

if __name__=='__main__':

    while True:
        statement = takeCommand().lower()

# search Commands
        if 'wikipedia' in statement:
            stopwords = ['what', 'who', 'is', 'search','find','close friend','on']
            querywords = statement.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            statement = ' '.join(resultwords)
            speak('Searching in Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2, auto_suggest=False)
            speak("According to Wikipedia")
            speak(results)
            translated = GoogleTranslator(source='auto', target='hi').translate(results)
            print(translated)

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India')
            time.sleep(6)

        elif 'play music' in statement or 'play song' in statement or 'play a song' in statement or 'play me a song' in statement:
            speak('tell me name of any song')
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
            time.sleep(2)

            while player.is_playing():
                if keyboard.is_pressed('k'):
                    player.pause()
                    if keyboard.is_pressed('k'):
                        player.play()

                elif keyboard.is_pressed('esc') or keyboard.is_pressed('q'):
                    player.stop()
                    time.sleep(1)
                    break

# Open commands
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            speak("Google chrome is opening now")
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            speak("Google Mail opening now")
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "open stackoverflow" in statement:
            speak("stackoverflow is opening")
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

# Interactive commands
        elif 'ask' in statement or 'calculate' in statement:
            speak('I can answer to computational and geographical questions ')
            speak('what question do you want to ask now')
            question=takeCommand1()
            stopwords = ['what', 'who', 'is', 'search', 'find', 'close friend']
            querywords = statement.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            statement = ' '.join(resultwords)
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak_e(answer)
            print(answer)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what's your city name")
            city_name=takeCommand1()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                Celsius =current_temperature - 271
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(round(Celsius,2)) + "°C."+
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in °C unit = " +
                      str(Celsius) + "°C" +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak("your City Not Found ")

        elif "developer" in statement or "mode change" in statement:
            print("Developer Mode on...")
            speak_e("Developer Mode onn")
            def file_lengthy(fname):
                with open(fname) as f:
                    for i, l in enumerate(f):
                        pass
                return i + 1
            tot = file_lengthy("assistant_(hin).py")
            print("Number of lines in the file: ", tot)
            time.sleep(0.5)
            speak_e('Please speak the condition')
            condition='none'
            while condition=='none':
                condition = takeCommand().lower()
            speak_e('Please speak the Output of the following condition')
            output = takeCommand().lower()
            code = '''\n        elif '%s' in statement :\n            speak('%s!')\n\n''' % (condition, output)
            with open("assistant_(hin).py") as f:
                lines = f.readlines()
            with open("assistant_(hin).py", "w") as f:
                lines.insert(tot - 22, code)
                f.write("".join(lines))
                speak('code successfully updated')
            time.sleep(2)
            speak_e("do you want to restart project to save changes made")
            confirm = takeCommand().lower()
            if 'yes' in confirm or 'yep' in confirm:
                speak("project is starting again. please wait")
                os.system('python assistant_(hin).py')
                break
            else:
                speak('the changes will be made on next rerun of the project')
                speak("if you wish to rerun program then speak reload or restart in next input")

        elif "where is" in statement:
            #data = statement.split(" ")
            stopwords = ['what', 'is', 'search', 'find', 'close friend', 'where','tell','dude']
            querywords = statement.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            statement = '+'.join(resultwords)
            stopwords = ['.']
            querywords = statement.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            statement1 = ''.join(resultwords)
            location = statement

            speak_e('here is' + location )
            webbrowser.open_new_tab("https://www.google.nl/maps/search/" + location + "/&amp;/data=!3m1!1e3")
            # webbrowser.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;data=!3m1!1e3")
            time.sleep(5)
            # os.system("chrome-browser https://www.google.nl/maps/place/" + location + "/&amp;")

        elif "reload" in statement or 'restart' in statement:
            speak("project is starting again. please wait")
            os.system('python assistant_(hin).py')
            break

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Now time is"+strTime)


# Casual Talks
        elif 'who are you' in statement:
            speak('I am Zoru version 2 . At your service')
            print()

        elif 'thank you' in statement:
            speak('no problem')
            speak('this is my work')
            print('☺')

        elif '2 point o' in statement or 'version 2' in statement or 'version 1' in statement :
            speak('I am the recreation of original assistant made by my creators')
            speak('the original assistant was destroyed due to some issues i dont know about')

        elif 'what can you do' in statement or 'what will you do' in statement:
            speak('I can tell you weather forecast today')
            speak('or open any application')
            speak('or can just talk to you as your friend')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by my creator Naman")
            print('''
                Name: Naman Punj
                Currently at: Studying in Class 12
                Date: 
                ''')

        elif "how are you" in statement :
            speak('i am fine sir thank you!')

        elif 'feel happy' in statement or 'i\'m happy' in statement:
            speak('i am also very happy. its an excellent day!')

        elif 'feel lonely' in statement or 'i\'m lonely' in statement:
            speak('i am here for you!')

        elif 'i\'m sad' in statement :
            speak('dont be. i can make you laugh with my jokes .or you can sing music along with me!')

# Ending
        elif 'search' in statement or 'what' in statement or 'who is' in statement or 'find' in statement:
            stopwords = ['what', 'who', 'is', 'search', 'find', 'close friend', 'on']
            querywords = statement.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            statement = ' '.join(resultwords)
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif "close" in statement or "quit" in statement or "stop" in statement:
            speak('your personal assistant Zorru is shutting down')
            speak('Good bye')
            print('Good bye ☺')
            break

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

time.sleep(3)