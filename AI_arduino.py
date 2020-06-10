#pip install pyttsx3
#pip insall SpeechRecognition
# python -m pip install pyaudio
# pip install pywin32
#pip install smtplib 
#pip install wikipedia 
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import time
import serial

now = time.asctime()
port = serial.Serial('COM4',9600)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def callme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        voice = r.recognize_google(audio, language='en-in')
        print("User said: {voice}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return voice


if __name__ == "__main__":
    callme()
    while True:
        
        voice = takeCommand().lower()
        if 'wikipedia' in voice:
            speak('Searching Wikipedia...')
            voice = voice.replace("wikipedia", "")
            results = wikipedia.summary(voice, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)



        elif 'play music' in voice:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in voice:
            speak("Sir, the time is ")
            speak(now)


        elif 'open code' in voice:
            codePath = "C:\\Users\\ANIKET\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif'songs' in voice:
            SongPath = "C:\\Users\\ANIKET\\Desktop\\Spotify"
            os.startfile(SongPath)


        elif 'hello' in voice:
            speak('Hello Sir')

        elif 'bye' in voice:
            speak('Bye Sir, have a good day.')
            sys.exit()

        
        elif'youtube' in voice:
            SearchyPath = "C:\\Users\\ANIKET\\Documents\\New folder\\dist\\youtube.exe"
            os.startfile(SearchyPath)


        elif'google' in voice:
            SearchgPath = "C:\\Users\\ANIKET\\Documents\\New folder\\dist\\google.exe"
            os.startfile(SearchgPath)


        elif'how are you' in voice:
            speak('fine! sir trying to update my salfe and ready to help you')

            
        elif'create folder' in voice:
            FolderPath = "C:\\ANIKET\\Documents\\New folder\\dist\\folder.exe"
            os.startfile(FolderPath)

