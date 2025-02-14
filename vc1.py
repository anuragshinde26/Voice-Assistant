# Voice Assistant 

import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import google 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Global variable to store recognized command
global command

# Initialize speech recognition and text-to-speech
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set properties of the text-to-speech engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to make the assistant speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        print('Listening...')
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio).lower()
        print('You said:', command)
        text_area.insert(tk.END, 'You said: ' + command + '\n')
        # Call process_command() to handle the recognized command
        process_command(command)
    except sr.UnknownValueError:
        print('Sorry, could not understand audio.')
        text_area.insert(tk.END, 'Sorry, could not understand audio.\n')
    except sr.RequestError as e:
        print('Could not request results; {0}'.format(e))
        text_area.insert(tk.END, 'Could not request results.\n')

# Function to process the recognized command
def process_command(command):
    # Add your code here to process the recognized command
    text_area.insert(tk.END, 'Processing command...\n')
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache.')
    elif 'are you single' in command:
        talk('I am in a relationship with WiFi.')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif 'bye' in command or 'goodbye' in command:
        talk('Goodbye!')
        window.quit()
    else:
        talk('Please say the command again.')

# Function to handle button click event
def on_click():
    text_area.insert(tk.END, 'Button clicked...\n')
    threading.Thread(target=recognize_speech).start()

# Create main window
window = tk.Tk()
window.title('Voice Assistant')

# Create text area for displaying output
text_area = scrolledtext.ScrolledText(window, width=40, height=10)
text_area.pack(padx=10, pady=10)

# Create button for activating voice assistant
button = tk.Button(window, text='Start Listening', command=on_click)
button.pack(pady=5)

# Start the GUI event loop
window.mainloop()
