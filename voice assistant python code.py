import pyttsx3
import speech_recognition as sr
import os
import datetime
import wikipedia
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

def speak(audio):
    """Make the assistant speak the given text."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    
    speak("I am your assistant. How can I help you today?")

def takeCommand():
    """Take voice input from the user and return the recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, could not understand. Please say that again.")
        return "None"
    return query.lower()

def main():
    """Main function to run the assistant."""
    wishMe()
    while True:
        query = takeCommand()

        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry, I could not find any results.")
        
        elif 'open notepad' in query:
            speak("Opening Notepad")
            os.system("notepad")
        
        elif 'open calculator' in query:
            speak("Opening Calculator")
            os.system("calc")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {strTime}")
        
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break
        
        else:
            speak("I didn't understand that. Could you please repeat?")

if __name__ == "__main__":
    main()
