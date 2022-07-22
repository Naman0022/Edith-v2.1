from langdetect import detect
import pyttsx3
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 180)


""" 
# _______________Voice Modulation____________________
voiceChange()
# ___________________________________________________


"""
"""
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
  
# the text to be transliterated

  
# printing the transliterated text
statement = transliterate(statement, sanscript.ITRANS, sanscript.DEVANAGARI)
print(statement)
from googletrans import Translator
translator = Translator()
result =translator.translate(statement)

print(result.text)
"""

def voiceChange():
    speak("I have 3 voices")
    engine.setProperty('voice',voices[0].id)
    speak("David's voice")
    engine.setProperty('voice',voices[1].id)
    speak("Hazel's voice")
    engine.setProperty('voice',voices[2].id)
    speak("Zira's voice")
    engine.setProperty('voice',voices[0].id)
    speak("which voice did you like the most")
    a=input()
    engine.setProperty('voice',voices[int(a)].id)
    speak("Oh you like my voice. Thanks")

def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    r.energy_threshold = 4000
    r.dynamic_energy_threshold = True
    r.pause_threshold = 1.0
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            print('Recognising...')
            statement= r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry could not hear you. please say that again")
            return "None"

        audio=r.listen(source)
        return statement
        
while True:
    statement=takeCommand().lower()

    if statement == "voice":
        voiceChange()
    elif statement == "how are you":
        speak("I am fine")
    elif statement == "quit" or statement =="close":
        break



























# class SpeechRec:
#     #https://techwithtim.net/tutorials/voice-assistant/wake-keyword/
#     def record(self, lang='en'):
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             audio = r.listen(source)
#             said = ""

#             try:
#                 #can I detect the language?
#                 if (lang == 'en') :
#                     said = r.recognize_google(audio, language='en-US')
#                 elif (lang == 'es') :
#                     said = r.recognize_google(audio, language="es") 

#                 print(said)
#             except Exception as e:
#                 if (str(e) != ""):
#                     print("Exception: " + str(e))

#         return said.lower()

""" 
py -m pip install "googletrans==3.1.0a0"
googletrans==3.1.0a0
"""