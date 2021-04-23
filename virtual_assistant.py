import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
# import pyaudio
import pyjokes
import pywhatkit
engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)#changing index, changes voices. 1 for female

def talk(text):

    engine.say(text)
    engine.runAndWait()

listener= sr.Recognizer() # assistent who is listening
def take_command():
    try:
     with sr.Microphone() as source:
        print("Listening.....")
        voice= listener.listen(source) #to listen the source voice
        command= listener.recognize_google(voice) #recognize the voice with google api
        if 'Liza' in command:
            command=command.replace('Liza','')

    except:
        pass
    return  command
def run_liza():
    command = take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+ song)
        print('playing')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I%M %p')
        talk('Now the time is' + time )
    elif 'what the thing is' in command:
        text=command.replace('what the thing is','')
        info= wikipedia.summary(text,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have an issue')
    elif 'single' in command:
        talk('No i have an relationship with DEV')
    elif 'joke' in command:
        tell=talk(pyjokes.get_joke())
    elif 'you are so sweet'in command:
        talk('Thanks, you too')
    else:
        talk('please say one more time, I did not understand what did you say')

while(True):
    run_liza()
