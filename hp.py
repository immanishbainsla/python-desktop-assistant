import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
from datetime import datetime 
import wikipedia # pip install wikipedia
import pyaudio # pip install pyAudio
import webbrowser
import os
import smtplib
# import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.now().hour)
    if hour == 0 and hour < 12:
        speak('Good Morning sir!')
    
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon sir!')

    else:
        speak('Good Evening sir!')

    speak('I am HP sir, your Desktop Assisstant. How may i help you sir?')



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\n\nListening...')
        r.pause_threshold = 1
        # r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'Recognized: {query}\n')

    except Exception as e:
        # Error
        print(e)
        print('Say that again Please 🙏.\n')
        return "None"

    return query


def sendEmail(to, content):
    # SMTPLIB
    # less secured apps in gmail '45:30'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # email and password for email login
    server.login('myemail@gmail.com', 'your-password-here')
    server.sendmail('friendsemail@gmail.com', to, content)
    server.close()












if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia: ')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open twitter' in query:
            webbrowser.open('twitter.com')

        elif 'open my portfolio' in query:
            webbrowser.open('immanishbainsla.github.io')

        elif 'play music' in query:
            music_dir = "C:\\Users\\ManishBainsla\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strTime}')
        
        elif 'open code' in query:
            code_path = "C:\\Users\\ManishBainsla\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'open whatsapp' in query:
            wa_path = "C:\\Users\\ManishBainsla\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(wa_path)

        elif 'open idle' in query:
            idle_path = "C:\\Users\\ManishBainsla\\AppData\\Local\\Programs\\Python\\Python36-32\\pythonw.exe"
            os.startfile(idle_path)

        elif 'open google chrome':
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)

        # create a dictionary to save name and emails
        elif 'send email to' in query:
            try:
                speak('What should i say?')
                content = takeCommand()
                to = 'myemail@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent.')

            except Exception as e:
                print(e)
                speak('Sorry sir, i am not able to send this Email.')

        elif 'quit' in query:
            quit()

        else:
            continue