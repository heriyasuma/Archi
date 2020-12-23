import speech_recognition as sr
import os
import pyttsx3
import datetime
import warnings
import calendar
import random
import wikipedia
import pyautogui
import time

def closeWindow():
    pyautogui.hotkey('winleft','shift','c')

def openTerm():
    pyautogui.hotkey('winleft','enter')

def openFirefox():
    pass

def workspace1():
    pyautogui.hotkey('winleft','1')

def openDmenu(command):
    pyautogui.hotkey('winleft','shift','enter')
    time.sleep(1)
    pyautogui.write('firefox')

def wakeWord(text):
    WAKE_WORDS = ['hey eve ', 'okay eve', 'eve'] 
    text = text.lower()    
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True  
        return False

# Function to return a random greeting response
def greeting(text):
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'wassup', 'hello']
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'    # If no greeting was detected then return an empty string
        return ''
# Function to get a person first and last name
def getPerson(text):
    wordList = text.split()# Split the text into a list of words     
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]

while True:
    # Record the audio
    #text = recordAudio()
    text = input("command : ")
    response = '' #Empty response string
    action = ''
     
    # Checking for the wake word/phrase
    if (wakeWord(text) == True):
        # Check for greetings by the user
        response = response + greeting(text)
                       
        # Check to see if the user said 'who is'
        if ("term" in text):
            time.sleep(1)
            openTerm()
            response = response + ' ' + "opening Terminal"
       
       # Assistant Audio Response
        print(response)



