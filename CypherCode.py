'''
    Project Cypher - Desktop Assistant with Voice Integration

        * @Filename : AssistantCypher.py
        * @author   : Team Cypher (Pradyumn Joshi, Milind Dalakoti, Mukul Manav)
        * @brief    : A desktop assistant which eases user's day-to-day job. A minor project which is converted now to a major project in version 2.0
        * @Timeline : October 2021 - April 2022
        * @version  : 2.0.0

    (C) All Rights Reserved 2022 - Team Cypher
'''

#Importing libraries
#GUI Libraries
from base64 import standard_b64decode
from tkinter import *
import tkinter
import customtkinter
from PIL import  ImageTk, Image
from tkinter import Canvas
from cv2 import split

#Backend Libraries
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import ctypes
import pyautogui
import sounddevice as sd
from scipy.io.wavfile import write
import datetime
import random
import cv2 
import pytesseract
from PIL import Image
import numpy as np
import winshell
import pandas as pd
from googlesearch import search
import tweepy
from screen_recorder_sdk import screen_recorder
from config.definitions import ROOT_DIR

#GUI Objects Initialization
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
root_tk.geometry("450x600")
root_tk.title("Cypher")

#TTS Objects Initialization
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)
#chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome %s'


def speak(text):
    '''
    When called will traslate text to speech
    
    Args:
    text(str) : text to be translated
    '''
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    '''
    takes command whenever user input needed

    Returns:
    (string):statement : user input
    '''

    #print("Listening...")
    ChatHistory.config(state=NORMAL)
    ChatHistory.insert('end', "Bot: Listening.... \n")
    ChatHistory.config(state=DISABLED)
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)       
    try:
        statement=r.recognize_google(audio,language='en-in') 
        ChatHistory.config(state=NORMAL)
        ChatHistory.insert('end', "User: "+statement+"\n")
        ChatHistory.config(state=DISABLED)
        print(f"user said:{statement}\n")

    except Exception as e:
        ChatHistory.config(state=NORMAL)
        ChatHistory.insert('end', "User: Pardon me, I cannot understand \n")
        ChatHistory.config(state=DISABLED)
        print("Pardon me, I cannot understand")
        return "None"

    return statement


def get_latest_image(dirpath, valid_extensions=('jpg','jpeg','png')):
    '''
    takes command whenever user input needed

    Args:
        dirpath(string) : path of directory

    Returns:
    (string):latest file name with its path
    '''

    # get filepaths of all files and dirs in the given dir
    valid_files = [os.path.join(dirpath, filename) for filename in os.listdir(dirpath)]
    # filter out directories, no-extension, and wrong extension files
    valid_files = [f for f in valid_files if '.' in f and \
        f.rsplit('.',1)[-1] in valid_extensions and os.path.isfile(f)]

    if not valid_files:
        raise ValueError("No valid images in %s" % dirpath)

    return max(valid_files, key=os.path.getmtime) 


def f_help(f_obj):
    index_path= os.path.join(ROOT_DIR, 'website', 'index.html')
    webbrowser.get('windows-default').open(index_path)
    #speak("Please follow the link opened on webbrowser")
    return "Please follow the link opened on webbrowser"

def f_greeting(f_obj):
    answers=['Hi','Holla','Namastee','Sasrikal','Hello','Bonjour','Olá']
    r_answer = random.choice(answers)
    #speak(r_answer)
    return r_answer

def f_greeting1(f_obj):
    answers=['I am good, thanks!', 'All good','Feeling better after hearing you','Doing just fine']
    r_answer = random.choice(answers)
    #speak(r_answer)
    return r_answer

def f_introduction(f_obj):
    #speak('I am Cypher version 2.O your persoanl desktop assistant. I am programmed to minor tasks like'
    #            'opening youtube,google chrome, etc')
    return ("I am Cypher version 2.O your persoanl desktop assistant. I am programmed to minor tasks like opening youtube,google chrome, etc")

def f_aknowledgement(f_obj):
    #speak("I was built by Team Cypher")
    return "I was built by Team Cypher"

def f_website(f_obj):
    index_path= os.path.join(ROOT_DIR, 'website', 'index.html')
    webbrowser.get('windows-default').open(index_path)
    return 'Opened Cypher Website'

def f_time(f_obj):
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    #speak(f"the time is {strTime}")
    return f"the time is {strTime}"

def f_youtube(f_obj):
    webbrowser.get('windows-default').open("https://www.youtube.com")
    #speak("Opening Youtube")
    return 'Opened Youtube'

def f_browser(f_obj):
    webbrowser.get('windows-default').open("https://www.google.com")
    #speak("Opening Google Chrome")
    return 'Opened Google'

def f_gmail(f_obj):
    webbrowser.get('windows-default').open("https://mail.google.com/mail/u/0/#inbox")
    #speak("Opening GMail")
    return "Opened GMail"

def f_vscode(f_obj):
    subprocess.Popen("D:\\ProgramFiles\\VSCode\\Microsoft VS Code\\Code.exe")
    return "Opened VS Code"

def f_classroom(f_obj):
    webbrowser.get('windows-default').open("https://classroom.google.com/u/2/h")
    #speak("Opening Google Classroom")
    return "Opened Classroom"

def f_netflix(f_obj):
    webbrowser.get('windows-default').open("https://www.netflix.com/browse")        
    #speak("Opening Netflix")
    return "Opened Netflix"

def f_stackoverflow(f_obj):
    webbrowser.get('windows-default').open("https://stackoverflow.com/login")
    #speak("Opened Stackoverflow")
    return "Opened Stackoverflow"

def f_hackerrank(f_obj):
    webbrowser.get('windows-default').open("https://www.hackerrank.com/dashboard")
    #speak("Opened Hackerrank, Enjoy Solving Problems! \n All the best")
    return "Opened Hackerrank, Enjoy Solving Problems! \n All the best"

def f_github(f_obj):
    webbrowser.get('windows-default').open("https://github.com/")
    #speak("Opened Github, Build software better and together. ")
    return "Opened Github, Build software better and together."

def f_twitter(f_obj):
    webbrowser.get('windows-default').open("https://twitter.com/")
    #speak("Opened Twitter")
    return "Opened Twitter"

def f_music(f_obj):
    webbrowser.get('windows-default').open("https://open.spotify.com/")
    return "Opened Spotify on webbrowser"

def f_text(f_obj):
    f_screenshot(f_obj)
    path=get_latest_image("./screenshots")
    img = cv2.imread(path)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img=cv2.threshold( img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img=cv2.medianBlur(img, 5)
    pytesseract.pytesseract.tesseract_cmd =r'D:\ProgramFiles\pytess\tesseract.exe'
    text = pytesseract.image_to_string(img) 
    print(text)
    return(text)

def f_object(f_obj):
    '''
    detects object in frame using screenshot function

    Returns:
    (string):Identified objects image
    '''
    ss=f_screenshot(f_obj)
    path=get_latest_image("./screenshots")
    image = Image.open(path)
    div=image.size[0]/500
    path_coco = os.path.join(ROOT_DIR, 'yoloFolder', 'coco.names')
    path_weight = os.path.join(ROOT_DIR, 'yoloFolder', 'yolov3.weights')
    path_cfg = os.path.join(ROOT_DIR, 'yoloFolder', 'yolov3.cfg')
    path_img = os.path.join(ROOT_DIR, 'yoloFolder', 'yolov3.cfg')
    resized_image = image.resize((round(image.size[0]/div),round(image.size[1]/div)))
    resized_image.save('C:\\Users\milin\\Desktop\\Cypher\\yoloFolder\\images\\na.png')
    classes_names=['person','bicycle','car','motorbike','aeroplane','bus','train','truck','boat','traffic light','fire hydrant','stop sign','parking meter','bench','bird','cat','dog','horse','sheep','cow','elephant','bear','zebra','giraffe','backpack','umbrella','handbag','tie','suitcase','frisbee','skis','snowboard','sports ball','kite','baseball bat','baseball glove','skateboard','surfboard','tennis racket','bottle','wine glass','cup','fork','knife','spoon','bowl','banana','apple','sandwich','orange','broccoli','carrot','hot dog','pizza','donut','cake','chair','sofa','pottedplant','bed','diningtable','toilet','tvmonitor','laptop','mouse','remote','keyboard','cell phone','microwave','oven','toaster','sink','refrigerator','book','clock','vase','scissors','teddy bear','hair drier','toothbrush']
    model=cv2.dnn.readNet(path_weight,path_cfg)
    layer_names = model.getLayerNames()
    output_layers=[layer_names[i-1]for i in model.getUnconnectedOutLayers()]
    image=cv2.imread('C:\\Users\milin\\Desktop\\Cypher\\yoloFolder\\images\\na.png')
    height, width, channels = image.shape
    blob=cv2.dnn.blobFromImage(image, 0.00392, (416,416), (0,0,0), True, crop=False)
    model.setInput(blob)
    outputs= model.forward(output_layers)
    class_ids = []
    confidences = []
    boxes = []
    for output in outputs:
        for identi in output:
            scores = identi[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.8:
                # Object detected
                centerx = int(identi[0] * width)
                centery = int(identi[1] * height)
                w = int(identi[2] * width)
                h = int(identi[3] * height)
                # Rectangle coordinates
                x = int(centerx - w / 2)
                y = int(centery - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_COMPLEX
    colors = np.random.uniform(0, 255, size=(len(classes_names), 3))
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            confidence = str("{:.2f}".format(confidences[i]))
            label = str(classes_names[class_ids[i]]+confidence)
            color = colors[i]

            cv2.rectangle(image, (x, y), (x + w, y + h), color, 1)
            cv2.putText(image, label,(x, y + 20), font, 1, color, 2)

    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return "image is saved"    

def f_news(f_obj):
    news = webbrowser.get('windows-default').open("https://timesofindia.indiatimes.com/home/headlines")
    speak('Here are some headlines from the Times of India,Happy reading')
    return "News is displayed on browser"

def f_google(f_obj):
    query=f_obj
    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
        webbrowser.open("https://google.com/search?q=%s" % query)
    
    #speak("Check webbrowser for result")
    return "Check webbrowser for result"

def f_question(f_obj):
    #speak('I can answer to computational and geographical questions and what question do you want to ask now')
    question=f_obj
    app_id="R2K75H-7ELALHR35X"
    client = wolframalpha.Client('R2K75H-7ELALHR35X')
    res = client.query(question)
    answer = next(res.results).text
    #speak(answer)
    return answer  

def f_weather(f_obj):
    api_key="8ef61edcf1c576d65d836254e11ea420"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    #speak("What city are you looking for!")
    city_name=f_obj
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_temperature=round(current_temperature-273.15)
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        #speak("Temperature is "+str(current_temperature)+"Celcius and humidity is"+
        #        str(current_humidity)+"in"+city_name)
        return(" Temperature in kelvin unit = " +
                str(current_temperature) +
                "\n humidity (in percentage) = " +
                str(current_humidity) +
                "\n description = " +
                str(weather_description)+ " in "+city_name)

    else:
        #speak("City Not Found")
        return("City Not Found")

def f_study_profile(f_obj):
    '''
    user profile function 

    Args:
    a_profile : Type of user profile

    Returns:
    (string):User Profile Activated
    '''
    webbrowser.get('windows-default').open("https://mail.google.com/mail/u/0/#inbox")
    webbrowser.get('windows-default').open("https://stackoverflow.com/login")
    subprocess.Popen("D:\\ProgramFiles\\VSCode\\Microsoft VS Code\\Code.exe")
    webbrowser.get('windows-default').open("https://www.hackerrank.com/dashboard")
    webbrowser.get('windows-default').open("https://classroom.google.com/u/2/h")
    subprocess.Popen("C:\\Users\\milin\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
    #speak("Started Profile Study, All the best Studying!")
    return "Started Profile Study, All the best Studying!"

def f_enjoy_profile(f_obj):
    webbrowser.get('windows-default').open("https://www.youtube.com")
    webbrowser.get('windows-default').open("https://open.spotify.com/")
    webbrowser.get('windows-default').open("https://www.netflix.com/browse")        
    subprocess.Popen("C:\\Users\\milin\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
    #speak("Started Profile Chill! Enjoy Sir!")
    return "Started Profile Chill! Enjoy Sir!"

def f_game_profile(f_obj):
    #subprocess.Popen("E:\\Program Files\\Valorant\\Riot Games\\Riot Client\\RiotClientServices.exe")
    subprocess.Popen("C:\\Users\\milin\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
    #speak("Started Profile Game! Enjoy Gaming, dont mald!")
    return "Started Profile Game! Enjoy Gaming, dont mald!"


def f_camera(f_obj):
    camera = cv2.VideoCapture(0)
    while(True):
        if not camera.isOpened():
            print('Unable to load camera.')
        else:
            return_value, image = camera.read()
            cv2.imshow("live feed",image)
            if cv2.waitKey(1) & 0xFF == ord(' '):
                d=datetime.datetime.now()
                a = str(d.date())
                b=str(datetime.datetime.now().strftime("%H-%M"))
                cv2.imwrite("./captures/"+a+"_"+b+".jpg", image)
                cv2.destroyWindow("live feed")
                cv2.imshow("img", image)
                cv2.waitKey(0)
                break
            
    camera.release()
    cv2.destroyAllWindows()
    #speak("Clicked you picture, saved in captures folder")
    return "Clicked you picture, saved in captures folder"
#check
def f_recycle(f_obj):
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        return "Emptied Recycle Bin"
    except:
        return "Recycle Bin already empty"
        

def f_joke(f_obj):
    data = pd.read_csv("./files/jokes1.csv")
    jok=random.choice(data["Joke"])
    #speak(jok)
    return jok 

def f_background(f_obj):
    webbrowser.get('windows-default').open("https://www.pexels.com/")
    #speak("The best place to get good backgrounds is opened in browser")
    return "The best place to get good backgrounds is opened in browser"

def f_note1(f_obj):
    file = open('notes.txt', 'w')
    file.write(f_obj)
    return "written note"

def f_note2(f_obj):
    #speak("Showing Notes")
    file = open("notes.txt", "r")
    #speak(file.read(6))
    return (file.read())

def f_screenshot(f_obj):
    im = pyautogui.screenshot()
    d=datetime.datetime.now()
    a = str(d.date())
    b=str(datetime.datetime.now().strftime("%H-%M"))
    if os.path.exists('./screenshots')==False:
        os.mkdir("screenshots")
    im.save("./screenshots/"+a+"_"+b+".jpg")
    #return "./screenshots/"+a+"_"+b+".jpg"
    #speak("Screenshot Taken")
    return ('screenshot is saved in screenshots folder')

def f_screen(f_obj):
    '''
    Records screen for particular time period

    Args:
    seconds(int) : time in seconds

    Returns:
    (string):Screen Recording
    '''
    d=datetime.datetime.now()
    a = str(d.date())
    b=str(datetime.datetime.now().strftime("%H-%M"))
    seconds = int(f_obj)
    screen_recorder.enable_dev_log ()
    params = screen_recorder.RecorderParams ()
    screen_recorder.init_resources (params)
    #screen_recorder.get_screenshot (5).save ("./screen_Recordings/"+a+"_"+b+".png")
    #print('Screenshot taken')
    #print('Video Started')
    screen_recorder.start_video_recording("./screen_Recordings/"+a+"_"+b+".mp4", 30, 8000000, True)
    time.sleep(seconds)
    screen_recorder.stop_video_recording()
    screen_recorder.free_resources()
    print('Video Stopped')
    return "Screen Recorded and saved in screen_recordings folder"

def f_audio(f_obj):
    freq = 44100
    #speak("Please specify the duration in seconds")
    duration = int(f_obj)
    #speak("Recording Audio")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)  
    sd.wait()
    #speak("Audio Recorded")
    d=datetime.datetime.now()
    a = str(d.date())
    b=str(datetime.datetime.now().strftime("%H-%M"))
    if os.path.exists('./recordings')==False:
        os.mkdir("recordings")
    write("./recordings/"+a+"_"+b+".wav", freq, recording)
    return "Audio is recorded and saved in recordings folder"

def f_wiki(f_obj):
    #speak('Searching Wikipedia..')
    #f_obj =f_obj.replace("wikipedia", "")
    results = wikipedia.summary(f_obj, sentences=3)
    #speak("According to Wikipedia")
    #speak(results)
    return results

def f_lock(f_obj):
    #speak("locking the device")
    ctypes.windll.user32.LockWorkStation()
    time.sleep(2)
    return "Locking PC"

def f_shutdown(f_obj):
    #speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
    subprocess.call(["shutdown", "/l"])
    time.sleep(10)
    return "Your pc will log off in 10 sec make sure you exit from all applications" 

def f_close(f_obj):
    #speak("Cypher is shutting down, Good Bye")
    root_tk.destroy()
    return 'Cypher is shutting down,Good bye'

def f_clear(f_obj):
    ChatHistory.delete("1.0","end")
    return None

def f_commands(f_obj):
    if f_obj in ["show commands","help","show command"]:
        f_obj="commands"
    
    elif f_obj in ["hello","hi"] :
        f_obj="greetings1"
    
    elif f_obj in ["website","about you"]:
        f_obj="website"

    else:
        f_obj=f_obj

    d_commands = {
        "commands" : f_help,
        "greetings1" : f_greeting,
        #"greetings2" : f_greeting1,
        #"introduction" : f_introduction,
        #"aknowledgement" : f_aknowledgement,
        "website" : f_website,
        "time" : f_time,
        "open youtube" : f_youtube,
        "open browser" : f_browser,
        "open gmail" : f_gmail,
        "open vscode" : f_vscode,
        "open classroom" : f_classroom,
        "open netflix" : f_netflix,
        "open stackoverflow" : f_stackoverflow,
        "open hackerrank" : f_hackerrank,
        "open github" : f_github,
        "open twitter" : f_twitter,
        "play music" : f_music,
        "get text" : f_text,
        "get object" : f_object,
        "news" : f_news,
        "google" : f_google,
        "question" : f_question,
        "weather" : f_weather,
        "profile study" : f_study_profile,
        "profile enjoy" : f_enjoy_profile,
        "profile game" : f_game_profile,
        "click picture" : f_camera,
        "empty recycle bin" : f_recycle,
        "tell joke" : f_joke,
        "show backgrounds" : f_background,
        #change the logic
        "write note" : f_note1,
        "show note" : f_note2,
        "screenshot" : f_screenshot,
        #"record screen" : f_screen,
        #"record audio" : f_audio,
        #"wikipedia" : f_wiki,
        "lock window" : f_lock,
        "shutdown" : f_shutdown,
        "close" : f_close,
        "clear" : f_clear,
        "bye" : f_close
    }
    ans=d_commands.get(f_obj,'not a command')
    print(ans)
    #print(ans(f_obj))
    return ans

#a=f_commands("hi")
#print(a)

def getResponse(msg):
    statement = msg.lower()
    split_statement = statement.split()
    print(split_statement)
    if "weather" in split_statement[0]:
        statement = statement.replace("weather", "")
        output = f_weather(statement)
        print(output)
        return output

    elif "question" in split_statement[0]:
        statement = statement.replace("question", "")
        output = f_question(statement)
        print(output)
        return output

    elif "google" in split_statement[0]:
        statement = statement.replace("google", "")
        output = f_google(statement)
        print(output)
        return output

    elif statement.lower() in ["how are you","how you doing","how are you?","wassup?","wassup"]:
        output = f_greeting1(statement)
        print(output)
        return output
    
    elif  statement.lower() in ['who are you?','what can you do?','whats your name?','who are you','what can you do','whats your name']:
        output = f_introduction(statement)
        print(output)
        return output
    
    elif  statement.lower() in ["who made you" ,"who created you" , "who discovered you","who made you?" ,"who created you?" , "who discovered you?"]:
        output = f_aknowledgement(statement)
        print(output)
        return output

    elif "record" in split_statement[0]:
        if "audio" in split_statement[1]:
            output=f_audio(split_statement[2])
            print(output)
            return output
        else :
            output=f_screen(split_statement[2])
            print(output)
            return output

    elif "wikipedia" in split_statement[0]:
        statement = statement.replace("wikipedia", "")
        output = f_wiki(statement)
        print(output)
        return output

    elif "write note" in statement:
        statement = statement.replace("write note", "")
        output = f_note1(statement)
        print(output)
        return output

    else:
        answer = f_commands(statement)
        output = answer(statement)
        print(output)
        return output

def chatbot_response(msg):
    out = getResponse(msg)
    speak(out)
    #msg1 = "Loading Cypher!"
    return out

def send():
    msg = TextEntryBox.get("1.0", 'end-1c').strip()
    TextEntryBox.delete('1.0', 'end')
    #!= ''
    if msg and msg.strip() :
        print("Not Null values")
        ChatHistory.config(state=NORMAL)
        ChatHistory.insert('end', "You: " + msg + "\n")
        
        res = chatbot_response(msg)
        ChatHistory.insert('end', "Bot: " + res+ "\n")
        ChatHistory.config(state=DISABLED)
        ChatHistory.yview('end')
    else:
        ChatHistory.config(state=NORMAL)
        ChatHistory.insert('end', "Bot: Listening... \n")
        ChatHistory.config(state=DISABLED)
        ChatHistory.yview('end')
        inpt = takeCommand()
        out = chatbot_response(inpt)
        ChatHistory.config(state=NORMAL)
        ChatHistory.insert('end', "Bot: " + out+ "\n")
        ChatHistory.config(state=DISABLED)
        ChatHistory.yview('end')
        return out


#:::::::::::::::::::::::::CHAT HISTORY::::::::::::::::::::::::::::::::::::::::::
ChatHistory = Text(root_tk,bd=0, bg='#141414',fg='white', font='Arial')
ChatHistory.config(state=DISABLED)
ChatHistory.place(height=395, width=445)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#logo = tkinter.PhotoImage(file="./logo.png")
image = Image.open('logo.png')
# The (450, 350) is (height, width)
image = image.resize((160, 100), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)



# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, text='', command=send, image=my_img, bg_color='#3b3b3b',fg_color = '#1b1a1b',height=90, width=160)
button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

#:::::::::::::::::::::::::::::TEXT FIELD::::::::::::::::::::::::::::::::::::::::
TextEntryBox = Text(root_tk, bd=0, bg='#212121',fg='white', font='Arial')
TextEntryBox.place(x=10, y=400, height=80, width=432)

#::::::::::::::::::::::::LABEL::::::::::::::::::::::::::::::
ChatHistory.config(state=NORMAL)
ChatHistory.insert('end', "Loading Cypher!! \n")
ChatHistory.config(state=DISABLED)
ChatHistory.yview('end')

def wishMe():
    '''
    Wishes user
    '''
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        #print("Hello,Good Morning")
        ChatHistory.config(state=NORMAL)
        ChatHistory.insert('end', "Bot: "+"Hello,Good Morning!! \n")
        ChatHistory.config(state=DISABLED)
        ChatHistory.yview('end')
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
        ChatHistory.config(state=NORMAL)
        ChatHistory.insert('end', "Bot: "+"Hello,Good Afternoon!! \n")
        ChatHistory.config(state=DISABLED)
        ChatHistory.yview('end')
    else:
        speak("Hello,Good Evening")
        #print("Hello,Good Evening")
        ChatHistory.config(state=NORMAL)
        ChatHistory.insert('end', "Bot: "+"Hello,Good Evening!! \n")
        ChatHistory.config(state=DISABLED)
        ChatHistory.yview('end')

def callback():
    wishMe()
    speak("To see commands ask show commands")
    #print("Hey! How can I help you? \n type help for commands")
    ChatHistory.config(state=NORMAL)
    ChatHistory.insert('end', "Hey! How can I help you? \n type help for commands \n")
    ChatHistory.config(state=DISABLED)
    ChatHistory.yview('end')


root_tk.after_idle(callback)
root_tk.mainloop()
            