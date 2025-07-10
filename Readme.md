Virtual Assistant For  Desktop:-

It is a smart and customizable desktop assistant built using Python, Eel, HTML/CSS, and JavaScript. It helps you control your PC and mobile with simple voice or typed commands.And also include chat history between user and the Virtual Assistant .
 
 ✨ Features

- 🎙️ **Voice & Text Control** – Interact via speech or typing.
- 💻 **Launch Desktop Applications** – Open apps like Chrome, VS Code, or Notepad.
- 🌐 **Open Websites** – Instantly visit your favorite URLs (YouTube, Google, etc.).
- 📞 **Android Phone Call Control** – Make and receive calls using ADB.
- 📲 **WhatsApp Messaging & Calls** – Send WhatsApp messages and initiate calls.
- 📔 **Built-in Contact Book** – Store and manage contact details.
- 🙋 **Personal Info Storage** – Save and reuse your name, age, preferences, etc.
- 🤖 **AI Chat Interaction** – Smart chatbot fallback for unknown queries.
- 🎵 **Play Media** – Play songs or videos on YouTube
- 🔐 **Face Recognition (Optional)** – Secure login with face unlock.


---

## 🛠️ Tech Stack

- **Python** (Backend logic & voice control)
- **Eel** (Python + Web frontend bridge)
- **HTML/CSS/JavaScript** (Frontend UI)
- **SpeechRecognition**, **Pyttsx3**, **pvporcupine** (Voice input/output & wake word)
- **ADB (Android Debug Bridge)** – For controlling Android phones
- **SQLite** – For storing contact and personal data
- **OpenCV** – Optional face recognition feature
- **pywhatkit**, **pyautogui**, **webbrowser**, and more.

 ##Install Dependencies:-
Create a virtual environment:
python -m venv env
env\Scripts\activate  # On Windows

Required Libraries:-
eel
pyttsx3
speechrecognition
pyaudio
pywhatkit
pyautogui
opencv-python
opencv-contrib-python
requests
pillow
flask
pvporcupine

##Set Up ADB for Android Control:-
Install ADB 
Enable USB Debugging on your Android phone.
Connect via USB and run:
 command:- adb devices


## 📁 Project Structure
VIRTUAL ASSISTANT/
│
├── engine/ # Core backend engine
│ ├── auth/ # Face recognition module
│ ├── chat_module.py # AI Chatbot logic
│ ├── command.py # Command processing logic
│ ├── config.py # Global settings
│ ├── cookies.json # Chatbot cookies or tokens
│ ├── Db.py # DB operations for contacts etc.
│ ├── features.py # Feature implementations
│ └── helpers.py # Utility/helper functions
│
├── env.Deepa/ # Python virtual environment (optional)
│
├── Frontend/ # Web-based UI using Eel
│ ├── controller.js
│ ├── index.html
│ ├── Main.js
│ ├── script.js
│ └── style.css
│
├── photos/ # Photos used for face recognition
│
├── contacts.csv # Phonebook data (CSV)
├── Deepa.db # SQLite database (contacts, history)
├── device.bat # Batch file to launch assistant
├── Main.py # Might be older or alternative entry point
├── run.py # 🔥 Main script to start Jarvis
├── test.py # Script for testing features
├── whatsappTest.py # Standalone WhatsApp testing
├── .gitignore # Ignore venv, pycache, etc.
└── README.md # Project documentation (this file)



📱 Android Control Features:-
To use phone features:
Connect Android phone via USB
Enable Developer Options > USB Debugging
Run adb devices to confirm the device is detected

Supported Actions
📞 Make a phone call
✅ Accept or disconnect incoming calls
💬 Send WhatsApp messages
🔗 Mobile interaction from desktop

🧠 How Virtual Assistant Works
Hotword Detection using Porcupine (e.g., “Jarvis”)
Speech Recognition via Google Speech API
Command Matching using regex or keyword mapping
Action Execution using Python modules or browser calls
Fallback Chat to AI-based interaction when no match is found

 Run the Assistant:-
 command:-python run.py

 


