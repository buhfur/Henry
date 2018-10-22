#holocron is a massive program to help me when learning new subjects
#and topics in computer science
#more like a jarvis of learning
#he will have web scraping capabilities, storage
#and more importantly vocal capability
#also should be able to save and store files

#going to work on storage first
#also able to create project templates
#import Voice

""" Ryan McVicker """
import speech_recognition as sr
import win32com.client as wincl
from Voice import Talk



if __name__ == '__main__':
    while(True):
        talk = Talk()
        print("please say something")
        user_request = talk.listen()
        #pass in value returned by user_request
