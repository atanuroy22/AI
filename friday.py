import pyttsx3
import speech_recognition as sr
from datetime import date
import time
import webbrowser
import datetime
from pynput.keyboard import Key, Controller
import pyautogui
import sys
import os
from os import listdir
from os.path import isfile, join
import smtplib
import wikipedia
#import Gesture_Controller
#import Gesture_Controller_Gloved as Gesture_Controller
import app
from threading import Thread
import pywhatkit
import keyboard
# -------------Object Initialization---------------
today = date.today()
r = sr.Recognizer()
keyboard = Controller()
engine = pyttsx3.init()

#For Girl Voice Disable Jarvis & Enable it----------------------

# engine = pyttsx3.init('sapi5')
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


# Get a list of voices & Finding Jarvis Voice--------------

voices = engine.getProperty('voices')
jarvis_voice = None
for voice in voices:
    if voice.name == "Jarvis":
        jarvis_voice = voice
        break
if jarvis_voice:
    engine.setProperty('voice', jarvis_voice.id)
engine.runAndWait()

# ----------------Variables------------------------
file_exp_status = False
files =[""]
path = ''
is_awake = True  #Bot status

# ------------------Functions----------------------
def reply(audio):
    app.ChatBot.addAppMsg(audio)

    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    time.sleep(2)
    reply(" Booting Up.!")
    time.sleep(1)
    reply("Please Wait....")
    time.sleep(0.5)
    
    
    if hour>=0 and hour<12:
        reply("Good Morning !")
    elif hour>=12 and hour<18:
        reply("Good Afternoon !")   
    else:
        reply("Good Evening !")  
    reply("Hey Welcome, I am friday!!")    
    reply("What can i do for you,,...!!!!!")

# Set Microphone parameters
with sr.Microphone() as source:
        r.energy_threshold = 500 
        r.dynamic_energy_threshold = False

# Audio to String
def record_audio():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        # pause after 0.8 secnd
        # r.pause_threshold = 0.8
        voice_data = ''
        audio = r.listen(source)
        #For time limit
        # audio = r.listen(source, phrase_time_limit=5)
        try:
            voice_data = r.recognize_google(audio)
        except sr.RequestError:
            reply('')
        except sr.UnknownValueError:
            # print('Dont Recognize')
            pass
        return voice_data.lower()


#Respond

    
def respond(voice_data):
    global file_exp_status, files, is_awake, path
    print(voice_data)
    voice_data.replace('friday','')
    app.eel.addUserMsg(voice_data)

    if is_awake==False:
        if 'wake up' in voice_data:
            is_awake = True
            wish()

    elif 'hello' in voice_data:
        wish()
    
    elif 'hey friday' in voice_data:
        reply('Hey Atanu Whats up!')

    elif 'date of birth' in voice_data:
        reply('Not set!')
        
    # elif 'my name' in voice_data:
    #     reply('your name is _____!')

    elif 'your name' in voice_data:
        reply('My name is friday i am build by Atanu!')
    
    elif 'i love you' in voice_data:
        reply('I  love you too Atanu!')
        
    elif 'are you in a relationship' in voice_data:
        reply('Yes i am in relationship with Your internet!') 

    elif 'will you marry' in voice_data:
        reply('No i can not,because i am an ai developed by Atanu!')

    elif 'date' in voice_data:
        reply(today.strftime("%B %d, %Y"))

    elif 'time' in voice_data:
        reply(str(datetime.datetime.now()).split(" ")[1].split('.')[0])
    
    elif 'chrome' in voice_data:
        reply('Opening ' + voice_data.split('chrome')[1])
        url = 'https://www.google.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'google' in voice_data:
        reply('Opening ' + voice_data.split('google')[1])
        url = 'https://www.google.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'youtube' in voice_data:
        reply('Opening ' + voice_data.split('youtube')[1])
        url = 'https://www.youtube.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'git hub' in voice_data:
        reply('Opening ' + voice_data.split('git hub')[1])
        url = 'https://github.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'whatsapp' in voice_data:
        reply('Opening ' + voice_data.split('whatsapp')[1])
        url = 'https://web.whatsapp.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'chat gpt' in voice_data:
        reply('Opening ' + voice_data.split('chat gpt')[1])
        url = 'https://chat.openai.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'facebook' in voice_data:
        reply('Opening ' + voice_data.split('facebook')[1])
        url = 'https://www.facebook.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'code pen' in voice_data:
        reply('Opening ' + voice_data.split('code pen')[1])
        url = 'https://codepen.io/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'cartoon' in voice_data:
        reply('Opening ' + voice_data.split('cartoon')[1])
        url = 'https://www.youtube.com/results?search_query=cartoon'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'play' in voice_data:
            voice_data = voice_data.replace('friday', '')
            song = voice_data.replace('play', '')
            reply('playing ' + song)
            pywhatkit.playonyt(song) 

    elif 'what is' in voice_data:
            person = voice_data.replace('friday', '')
            info = wikipedia.summary(person,2)
            print(info)
            reply(info)

    elif 'who' in voice_data:
            person = voice_data.replace('friday', '')
            info = wikipedia.summary(person,1)
            print(info)
            reply(info)

    elif 'code' in voice_data:
        reply('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('code')[1])
        a = voice_data.lstrip("friday ")
        search_query = a.replace(" ", "+")
        url = 'https://www.perplexity.ai/search?q=' + search_query
        try:
            webbrowser.get().open(url)
            reply('Wait a moment')
        except:
            reply('Please check your Internet')

    elif 'write' in voice_data:
        reply('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('write')[1])
        a = voice_data.lstrip("friday ")
        search_query = a.replace(" ", "+")
        url = 'https://www.perplexity.ai/search?q=' + search_query
        try:
            webbrowser.get().open(url)
            reply('Wait a moment')
        except:
            reply('Please check your Internet')
            
    elif 'give' in voice_data:
        reply('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('give')[1])
        a = voice_data.lstrip("friday ")
        search_query = a.replace(" ", "+")
        url = 'https://www.perplexity.ai/search?q=' + search_query
        try:
            webbrowser.get().open(url)
            reply('Wait a moment')
        except:
            reply('Please check your Internet')
            
    elif 'tell' in voice_data:
        reply('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('tell')[1])
        a = voice_data.lstrip("friday ")
        search_query = a.replace(" ", "+")
        url = 'https://www.perplexity.ai/search?q=' + search_query
        try:
            webbrowser.get().open(url)
            reply('Wait a moment')
        except:
            reply('Please check your Internet')

    elif 'telegram' in voice_data:
        reply('Opening ' + voice_data.split('telegram')[1])
        url = 'https://web.telegram.org/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'gmail' in voice_data:
        reply('Opening ' + voice_data.split('gmail')[1])
        url = 'https://mail.google.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')
    
    elif 'football' in voice_data:
        reply('Opening ' + voice_data.split('football')[1])
        url = 'https://www.goal.com/en-in/live-scores'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'cricket' in voice_data:
        reply('Opening ' + voice_data.split('cricket')[1])
        url = 'https://www.cricbuzz.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    

    elif 'news' in voice_data:
        reply('Opening ' + voice_data.split('news')[1])
        url = 'https://bengali.abplive.com/'
        try:
            webbrowser.get().open(url)
        except:
            reply('Please check your Internet')

    elif 'how are you' in voice_data:
        reply("I'm doing great, thank you!")

    elif 'inspire me' in voice_data or 'quote of the day' in voice_data:
        reply("Why don't scientists trust atoms? Because they make up everything!")
        
    elif 'thank you' in voice_data:
        reply("You're welcome! I'm here to help.")
    
    
    # for fun Only   # for fun Only    # for fun Only


    elif 'manu' in voice_data:
        reply("Manu , , He is a big Chutiya.")


    # java# java # java # java # java # java # java

    





    # Java Script Java Script  Java Script
 
    








    
    #python

    

    elif 'explain' in voice_data:
        reply('Opening ' + voice_data.split('explain')[1])
        url = 'https://www.perplexity.ai/'
        try:
            webbrowser.get().open(url) 
            reply('type what you want to explain and press Enter')
        except:
            reply('Please check your Internet')












    elif 'type' in voice_data:
        text = voice_data.replace('type', '')
        try:
            keyboard.type(text)
            reply("Text has been typed successfully!")
        except Exception as e:
            reply(f"Sorry, I am unable to type: {str(e)}")

    elif 'pause' in voice_data:
        # Simulate spacebar press to pause/play
        try:    
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            reply("Playback paused.")
        except:
            reply("I did not hear your voice.")   

    elif 'fast' in voice_data:
        # Simulate > key press to increase playback speed
        try:
            keyboard.press('>')
            keyboard.release('>')
            reply("Playback speed increased.")
        except:
            reply("I did not hear your voice.")

    elif 'slow' in voice_data:
        # Simulate < key press to decrease playback speed
        try:
            keyboard.press('<')
            keyboard.release('<')
            reply("Playback speed decreased.")
        except:
            reply("I did not hear your voice.")

    elif 'full' in voice_data:
        # Simulate f key press to toggle full screen
        try:
            keyboard.press('f')
            keyboard.release('f')
            reply("Toggled full screen.")
        except:
            reply("I did not hear your voice.")

    elif 'skip' in voice_data:
        # Simulate right arrow key press to skip forward
        try:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            reply("Skipped 5 seconds.")
        except:
            reply("I did not hear your voice.")

    elif 'skip ten' in voice_data:
        # Simulate l key press to skip forward by 10 seconds
        try:
            keyboard.press('l')
            keyboard.release('l')
            reply("Skipped 10 seconds.")
        except:
            reply("I did not hear your voice.")

    elif 'next' in voice_data:
        # Simulate shift + n key press to play next video
        try:
            keyboard.press(Key.shift)
            keyboard.press('n')
            keyboard.release(Key.shift)
            keyboard.release('n')
            reply("Playing next video.")
        except:
            reply("I did not hear your voice.")

    elif 'previous' in voice_data:
        # Simulate shift + p key press to play previous video
        try:
            keyboard.press(Key.shift)
            keyboard.press('p')
            keyboard.release(Key.shift)
            keyboard.release('p')
            reply("Playing previous video.")
        except:
            reply("I did not hear your voice.")

    elif 'mute' in voice_data:
        # Simulate m key press to mute/unmute video
        try:
            keyboard.press('m')
            keyboard.release('m')
            reply("Video muted.")
        except:
            reply("I did not hear your voice.")

    elif 'volume up' in voice_data:
        # Simulate up arrow key press to increase volume
        try:
            keyboard.press(Key.up)
            keyboard.release(Key.up)
            reply("Volume up.")
        except:
            reply("I did not hear your voice.")

    elif 'volume down' in voice_data:
        # Simulate down arrow key press to decrease volume
        try:
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            reply("Volume down.")
        except:
            reply("I did not hear your voice.")

    elif 'stop' in voice_data:
        # Simulate q key press to stop playback
        try:
            keyboard.press('q')
            keyboard.release('q')
            reply("Playback stopped.")
        except:
            reply("I did not hear your voice.")

    elif 'subtitle' in voice_data:
        # Simulate c key press to toggle subtitles
        try:
            keyboard.press('c')
            keyboard.release('c')
            reply("Toggled subtitles.")
        except:
            reply("I did not hear your voice.")

    elif 'mini' in voice_data:
        # Simulate i key press to enter/exit mini player mode
        try:
            keyboard.press('i')
            keyboard.release('i')
            reply("Entered/Exited mini player mode.")
        except:
            reply("I did not hear your voice.")

    elif 'screenshot' in voice_data:
        # Take a screenshot using pyautogui
        try:
                keyboard.press(Key.alt)
                keyboard.press(Key.print_screen)
                keyboard.release(Key.alt)
                keyboard.release(Key.print_screen)
                reply("Screenshot captured & Saved To Dexktop.")
        except:("i did not hear your voice")

    elif 'close this' in voice_data:
        # Close the active application
        try:
            keyboard.press(Key.alt)
            keyboard.press(Key.f4)
            keyboard.release(Key.alt)
            keyboard.release(Key.f4)
            reply("Application closed.")
        except:
            reply("I did not hear your voice.")

    elif 'shutdown' in voice_data:
        # Shut down the system
        try:
            reply("Shutting down the system.")
            os.system("shutdown /s /t 1")
        except:
            reply("I did not hear your voice.")

    elif 'search' in voice_data:
        # Search the web using pywhatkit
        query = voice_data.replace('search', '')
        try:
            pywhatkit.search(query)
            reply("Searching for " + query + ".")
        except:
            reply("I did not hear your voice.")

    elif 'location' in voice_data:
        # Search for a location on Google Maps
        reply("Which place are you looking for?")
        location = record_audio()
        if location:
            url = 'https://www.google.com/maps/search/' + location.replace(' ', '+')
            try:
                webbrowser.get().open(url)
                reply("Locating " + location + ".")
            except:
                reply("Please check your internet connection.")
        else:
            reply("I did not hear your voice.")

    elif 'copy' in voice_data:
        # Simulate Ctrl+C key press to copy
        try:
            keyboard.press(Key.ctrl)
            keyboard.press('c')
            keyboard.release(Key.ctrl)
            keyboard.release('c')
            reply("Copied.")
        except:
            reply("I did not hear your voice.")

    elif 'paste' in voice_data:
        # Simulate Ctrl+V key press to paste
        try:
            keyboard.press(Key.ctrl)
            keyboard.press('v')
            keyboard.release(Key.ctrl)
            keyboard.release('v')
            reply("Pasted.")
        except:
            reply("I did not hear your voice.")

            #open admin folder like Atanu roy 
    elif 'open folder' in voice_data:
            reply("Which folder or application in atanu folder?")
            try:
               application = record_audio()
               if application:
                   os.startfile(application)
                   reply(f"Opening {application}.")
               else:
                   reply("I'm sorry, I didn't catch the name.")
            except:
                reply("file not found")

    elif 'bye' in voice_data or 'goodbye' in voice_data:
        # Exit the program
        reply("Goodbye! Have a nice day.")
        exit()
    
   
    # File Navigation (Default Folder set to C://)
    elif 'list' in voice_data:
        counter = 0
        path = 'y://'
        files = listdir(path)
        filestr = ""
        for f in files:
            counter+=1
            print(str(counter) + ':  ' + f)
            filestr += str(counter) + ':  ' + f + '<br>'
        file_exp_status = True
        reply('These are the files in your root directory')
        app.ChatBot.addAppMsg(filestr)
        
    elif file_exp_status == True:
        counter = 0   
        if 'open' in voice_data:
            if isfile(join(path,files[int(voice_data.split(' ')[-1])-1])):
                os.startfile(path + files[int(voice_data.split(' ')[-1])-1])
                file_exp_status = False
            else:
                try:
                    path = path + files[int(voice_data.split(' ')[-1])-1] + '//'
                    files = listdir(path)
                    filestr = ""
                    for f in files:
                        counter+=1
                        filestr += str(counter) + ':  ' + f + '<br>'
                        print(str(counter) + ':  ' + f)
                    reply('Files are listed')
                    app.ChatBot.addAppMsg(filestr)
                    
                except:
                    reply('I do not have permission to access this folder')
                                    
        if 'back' in voice_data:
            filestr = ""
            if path == 'C://':
                reply('Sorry, this is the root directory')
            else:
                a = path.split('//')[:-2]
                path = '//'.join(a)
                path += '//'
                files = listdir(path)
                for f in files:
                    counter+=1
                    filestr += str(counter) + ':  ' + f + '<br>'
                    print(str(counter) + ':  ' + f)
                reply('ok')
                app.ChatBot.addAppMsg(filestr)
                   
    else: 
        reply("did not here your voice")
        reply("you cam Manually Type and search using ai")
    #Open Every Time (Error)    
    #     a = voice_data.lstrip("friday ")
    # search_query = a.replace(" ", "+")
    
    # search_url = 'https://www.perplexity.ai/search?q=' + search_query
    # webbrowser.open(search_url)
    
        
          
# ------------------Driver Code--------------------

t1 = Thread(target = app.ChatBot.start)
t1.start()

# Lock main thread until Chatbot has started
while not app.ChatBot.started:
    time.sleep(0.5)

wish()
voice_data = None
while True:
    if app.ChatBot.isUserInput():
        #take input from GUI
        voice_data = app.ChatBot.popUserInput()
    else:
        #take input from Voice
        voice_data = record_audio()

    #process voice_data
    if 'friday' in voice_data:
        try:
            #Handle sys.exit()
            respond(voice_data)
        except SystemExit:
            reply("Exit Successfull")
            break
        except:
            #some other exception got raised
            print("EXCEPTION raised while closing.") 
            break
        


