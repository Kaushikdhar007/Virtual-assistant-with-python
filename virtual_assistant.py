import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import smtplib

# import pyaudio
import pyjokes
import pywhatkit
import webbrowser
from email.message import EmailMessage
def send_email(command5,command6,command7):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('kaushikdhar90@gmail.com','somadhar')
    email= EmailMessage()
    email['From'] = 'kaushikdhar90@gmail.com'
    email['To']=  command5
    email['Subject']= command7
    email.set_content(command6)

    server.send_message(email)
engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)#changing index, changes voices. 1 for female

email_list={'red': 'kaushikdhar210@gmail.com',
            'blue': 'kaushikdhar63@gmail.com',
            'green': 'dharkaushik147@gmail.com',
            'yellow': 'bwubec18001@brainwareuniversity.ac.in'}

def send_email_command():
    command2 = take_command()
    reciever = email_list[command2]
    print(reciever)
    talk('What is the massage do you want to send')
    command3 = take_command()
    print(command3)
    talk('What is the subject of your mail')
    command4 = take_command()
    talk('It will be sent to that email. Please wait.....')
    send_email(reciever, command3, command4)
    talk('email has been sent')

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
        command = command.lower()
        if 'liza' in command:
            command=command.replace('liza','')
            print(command)
    except:
        pass
    return  command
def run_liza():
    command = take_command()
    if 'play' in command:
        print(command)
        song=command.replace('play','')
        talk('playing'+ song)
        print('playing')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        print(command)
        time = datetime.datetime.now().strftime('%I%M %p')
        talk('Now the time is' + time )
    elif 'what the thing is' in command:
        print(command)
        text=command.replace('what the thing is','')
        info= wikipedia.summary(text,1)
        print(info)
        talk(info)
    elif 'date' in command:
        print(command)
        talk('sorry, I have an issue')
    elif 'single' in command:
        print(command)
        talk('No i have an relationship with DEV')
    elif 'joke' in command:
        print(command)
        talk(pyjokes.get_joke())
    elif 'you are so sweet'in command:
        print(command)
        talk('Thanks, you too')
    elif 'sent email' in command:
        print(command)
        talk('whom do you want to send an email')
        send_email_command()
    elif 'open amazon' in command:
        print(command)
        say= command.replace('open','')
        talk('opening'+ say)
        webbrowser.open('amazon.com')
    elif 'open google' in command:
        print(command)
        say=command.replace('open','')
        talk('opening'+ say)
        webbrowser.open('google.com')
    elif 'open flipkart' in command:
        print(command)
        say=command.replace('open','')
        talk('opening'+ say)
        webbrowser.open('flipkart.com')
    elif 'are you there' in command:
        print(command)
        talk('yes i am here and i am waiting for your command')
    elif 'open whatsapp' in command:
        print(command)
        say=command.replace('open','')
        talk('opening'+say)
        webbrowser.open('web.whatsapp.com')
    else:
        talk('please say one more time, I did not understand what did you say')

while(True):
    run_liza()


