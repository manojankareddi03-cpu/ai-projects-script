Step 1: Project Create Cheyyi
jarvis-v2/
│── main.py
│── config.py
│── requirements.txt
│
├── brain/
│   ├── llm.py
│   ├── memory.py
│
├── voice/
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│
├── automation/
│   ├── browser.py
│   ├── system.py
│
└── data/
    └── memory.json
Step 2: requirements.txt
openai
speechrecognition
pyttsx3
pyaudio
python-dotenv
Install:
pip install -r requirements.txt
Step 3: main.py
from voice.speech_to_text import listen
from voice.text_to_speech import speak

print("Jarvis Started...")

while True:
    command = listen()

    if command is None:
        continue

    print("You:", command)

    if "exit" in command.lower():
        speak("Goodbye Sir")
        break

    speak(f"You said {command}")
Step 4: voice/speech_to_text.py
import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text
    except:
        return None
Step 5: voice/text_to_speech.py
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
Output
Listening...
You: Hello Jarvis
Jarvis: You said Hello Jarvis
