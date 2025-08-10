import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

def process_command(command, talk):
    """Handle recognized commands."""

    if 'play' in command:
        song = command.replace('play', '')
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {current_time}")

    elif 'who is' in command:
        try:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
        except:
            talk("Sorry, I couldn't find information.")

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif 'google' in command:
        query = command.replace('google', '')
        talk(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif 'youtube' in command:
        query = command.replace('youtube', '')
        talk(f"Searching YouTube for {query}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    elif 'bye' in command or 'exit' in command:
        talk("Goodbye! Have a nice day.")
        quit()

    else:
        talk("I didn't understand that. Please try again.")
