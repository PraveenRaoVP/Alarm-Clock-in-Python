# import the required modules
import playsound
import datetime
import sys
import os
import msvcrt
import winsound
from tkinter import *

#this function is for the button to set the time and wait for the alarm, take the code from the before made project 
def setAlarmClock(setHour,setMin):
	while(True):
		if(datetime.datetime.now().hour == setHour and datetime.datetime.now().minute == setMin):	
			while(msvcrt.kbhit()):
                #playsound is not working wtf
                playsound.playsound("D:\Games\ProjectsFolder\Alarm-Clock-in-Python-main\Alarm Clock sound.mp3")
			Label(clock,text="Wake up").place(x=300,y=500)
			return False

	

#initialize tk() object window
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("700x700")

time_format = Label(clock, text = "Enter the time in 24 hr format:-", bg ="white",fg = "black", font = "Arial 12")
#define StringVar() objects
tkvar1 = StringVar(clock)
tkvar2 = StringVar(clock)
tkvar3 = StringVar(clock)

#current time
nowHour = datetime.datetime.now().hour
nowMinute = datetime.datetime.now().minute

#dropdown option for hour
#tkvar1.set(nowHour)
choicesHr = range(0,13)
popUpMenuHr = OptionMenu(clock, tkvar1, *choicesHr) 
popUpMenuHr.place(x=200,y=200)

#dropdown option for minute
choicesMin = range(0,61)
#tkvar2.set(nowMinute)
popUpMenuMin = OptionMenu(clock,tkvar2,*choicesMin)
popUpMenuMin.place(x=300,y=200)

#determine am or pm
amOrPm = ['AM','PM']
#if pm then add hour by 12 (24 hr format)
ci =False
if(nowHour>12):
	tkvar3.set(amOrPm[1])
	ci = True
else:
	tkvar3.set(amOrPm[0])

popUpMenuAmPm = OptionMenu(clock,tkvar3,*amOrPm)
popUpMenuAmPm.place(x=400,y=200)


#button
Button = Button(clock, text="Set Alarm", bg="white", fg="black", command=lambda:setAlarmClock(int(tkvar1.get())+12 if(ci) else int(tkvar1.get()),int(tkvar2.get())), height=3, width=6)
Button.place(x=350, y=350)

clock.mainloop()
