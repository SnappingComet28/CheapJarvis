from time import sleep
import pyttsx3
engine = pyttsx3.init()
timedict = {}
with open("timedata.txt","rt") as file:
    for line in file:
        key,value = line.strip().split("!")
        timedict[key] = value
with open("timedata.txt","wt")as f:
    f.write("<null>")
def reminderMain():
    sleep(int(timedict["time"])*60)
    abc = timedict["msg"]
    for i in range(5):
        engine.say(f"Reminder Triggered! {abc}")
        engine.runAndWait()
reminderMain()