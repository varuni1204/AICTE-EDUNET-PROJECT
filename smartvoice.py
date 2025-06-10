import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Voice properties
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, service is down.")
        return ""

def process_command(command):
    # Time & Date
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    # Joke
    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    # Open Websites
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        speak("Opening Gmail.")

    # Wikipedia
    elif "who is" in command or "what is" in command:
        topic = command.replace("who is", "").replace("what is", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        except:
            speak("Sorry, I couldn't find that.")

    # Exit
    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye! Stay safe.")
        return False

    # Fallback
    else:
        speak("Sorry, I don't understand that command yet.")
    
    return True

# Greet user
speak("Hello! I'm SmartVoice. How can I help you today?")

# Loop
while True:
    user_input = listen_command()
    if user_input:
        if not process_command(user_input):
            break
