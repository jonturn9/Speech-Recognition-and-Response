# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:27:22 2023

@author: jonathan.turner
"""

#import library
 
import speech_recognition as sr
import pyttsx3
import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser'

x = 0
y = 0

fig = px.scatter(x=[x],y=[y], range_x=[-1,1], range_y=[-1,1])
fig.show()

engine = pyttsx3.init()

key_words = {"up",
             "down",
             "left",
             "right",
             "reset"}
 
confirmation_words = {"yes",
                      "correct",
                      "affirmative"}

# Initialize recognizer class (for recognizing the speech)
 
r = sr.Recognizer()
 
# Reading Microphone as source
# listening the speech and store in audio_text variable
 
with sr.Microphone() as source:
    print("Mic Hot")
    raw_audio_text = r.listen(source)
    print("Mic Closed")

# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
received_command = r.recognize_google(raw_audio_text)
engine.say("Received command:" + received_command + "End Received command: is this correct?")
engine.runAndWait()   

with sr.Microphone() as source:
    print("Mic Hot")
    raw_confirmation_audio = r.listen(source)
    print("Mic Closed")

confirmation_text = r.recognize_google(raw_confirmation_audio)

if confirmation_text in confirmation_words:
    print("Confirmed")
    try:
        # using google speech recognition
        print("Text: "+received_command)
        if "up" in received_command:
            y +=1
            fig = px.scatter(x=[x],y=[y], range_x=[-1,1], range_y=[-1,1])
            fig.show()
        elif "down" in received_command:
            y -= 1
            fig = px.scatter(x=[x],y=[y], range_x=[-1,1], range_y=[-1,1])
            fig.show()
        elif "left" in received_command:
            x -=1
            fig = px.scatter(x=[x],y=[y], range_x=[-1,1], range_y=[-1,1])
            fig.show()
        elif "right" in received_command:
            x += 1
            fig = px.scatter(x=[x],y=[y], range_x=[-1,1], range_y=[-1,1])
            fig.show()
        elif "reset" in received_command:
            x = 0
            y = 0
            fig = px.scatter(x=[x],y=[y], range_x=[-1,1], range_y=[-1,1])
            fig.show() 
                
    except:
         print("Command heard and confirmed but not understood")
         engine.say("Command heard and confirmed but not understood")
         engine.runAndWait()
else:
    engine.say("Command not understood, please try again")
    engine.runAndWait() 



     

         
