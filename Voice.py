#first draft is going to use the windows 10 api

#Ryan McVicker
import speech_recognition as sr
import win32com.client as wincl
import json
import time
import sys
#from Email import Email
#from Storage import Storage
#from Web import Web
#feature: user says equation and it gives the answer gage underwood

class Talk:
    def __init__(self):
        #self.email = email()
        #self.storage = storage()
        self.user_speak = wincl.Dispatch("SAPI.SpVoice")
        self.r = sr.Recognizer()
        #self.web = web()


    def listen(self):
        with sr.Microphone() as source:
            self.audio = self.r.listen(source)
            self.text = self.r.recognize_google(self.audio)
            print(self.text)
            self.speak(self.text)

    def speak(self, request):
        #email requests
        if request == "Henry email" or request == "Henry I would like to send an email" or request == "Hey henry can I send an email":
            self.user_speak.Speak("okay, who would you like me to send it to?")
            self.email_user = self.listen()


        elif request == "Henry I would like to create a flask project" or request == "Hey i want to make a flask project":
            self.user_speak.Speak("sure, no problem!")
        #misc requests

        elif request == "who are you":
            self.user_speak.Speak("my name is henry, your personal assistant for learning computer science and software engineering.")

        elif request == "Henry who made you" or request == "who made you":
            self.user_speak.Speak("i was created by Ryan Michael McVicker on the date of october 22nd 2018")

        elif request == "what is your purpose" or request == "Henry what is your purpose" or request == "and your purpose" or "Henry state your purpose":
            self.user_speak.Speak("my purpose is to assist you in learning computer science. and software engineering")

        elif request == "Henry shut down" or request == "Henry turn off" or request == "shut down":
            self.user_speak.Speak("okay, good bye!")
            sys.exit()

        elif request == "what can you do" or request == "what sort of things can you do" or request == "what are your features" or request == "what are some of the things you can do":
            self.user_speak.Speak()

        elif request == "Henry" or request == "uh Henry" or request == "hey Henry":
            self.user_speak.Speak("yes? what can i do for you")

        else:
            self.user_speak.Speak("im sorry sir, but i couldent understand that")




        #else:
        #    self.user_speak.Speak("im sorry, i didnt understand that")
