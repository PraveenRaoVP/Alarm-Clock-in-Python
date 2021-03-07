import playsound
import datetime
import os
import sys

import msvcrt
     
#frequency=300 if I wanted a beep sound to be my alarm,
#duration=15000 i would use the module playsound.Beep(frequency,duration)

alarmHour = int(input("Set the hour of alarm(24 hr HH format) : "))
alarmMinute= int(input("Set the minute of the alarm (MM format): "))
if(alarmHour>24 or alarmMinute>59):
    print("There are only 24 hours in a day and only 60 minutes. Choose a valid time ")
else:
    while(True):
        if(alarmHour==datetime.datetime.now().hour and 
            alarmMinute==datetime.datetime.now().minute):
            print(f"The time is now {alarmHour}:{alarmMinute}")
            while(msvcrt.kbhit()):
                playsound.playsound("D:\Games\Projects Folder\Alarm Clock Python\Alarm sound effect.mp3")
            break
print("Alarm executed")