import pyttsx3
import speech_recognition as sr
import eel
import time
from engine.chat_module import chatBot
import traceback

## jo hum text denge wooh hmra virtual assistant bolega 
def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')  ## pata krne ke liye ki kitni voices hai 
    engine.setProperty('voice', voices[1].id) ## voice set krne ke liye
    engine.setProperty('rate', 174)   ## for setting voice rate aur voice ko thik karta hai  
    eel.displayMessage(text) ## yeah jo hmri query hai wooh siri wave ke upar  print krega 
    engine.say(text)
    eel.receiverText(text) ## jo  jarvis bolega wooh bhi chat history mein aaye 
    engine.runAndWait() ## eska mtlb hai jo bolega  wooh beech beech mein ruk ruk ke bolega 

    ## yeah speak function ka mtlb hai ki wooh ek arguement lega (text) aur ussi ko hi say bolega 

## for speech recognition
def takecommand():
    r = sr.Recognizer() ## humne speech recognizier object bnaya hai (r) speech recgoniziation lib se
    with sr.Microphone() as source: ## hum microphone ko source bana rahe hai 
        print("I am listeninng now Please Speak Now ")
        eel.displayMessage("I am listeninng Speak Now ") ## yeah message hum apne frontent ko bej rahe hai 
        r.pause_threshold = 1 ## mtlb agr hum 1 sec bhi chup rahe toh wooh listen krna band krdega  
        r.adjust_for_ambient_noise(source) ## yeah background ke useless awaz ko hata dega  

        audio = r.listen(source, 10, 6) ## eska mtlb hai ki humhe 10 sec ke andar bolna hai aur jo bolna hai wooh 6 sec tak khtm krna hai 
        try:
            print('recognizing')
            eel.displayMessage('recognizing')
            query = r.recognize_google(audio, language='en-in') ## yeah audio ko text mein convert krta hai using Google’s free speech recognition API.
            print(f"user said: {query}") ## yeah jo bola hai terminal pe print krega 
            eel.displayMessage(query) ## query ko frontend pe dega 
        except Exception as e:
            return ""  ## error aane par khali string return hoga

        return query.lower()    

## for window open feature and youtube (mtlb hum v.a ko bole ki jaise notepad ko karo open toh wohh kare)
@eel.expose
def allCommands(message=1):
    try:
        # 🎤 Step 1: Get voice or text input
        if message == 1:
            query = takecommand()
            print(f"[DEBUG] Voice query: '{query}'")
            eel.senderText(query)
        else:
            query = message
            print(f"[DEBUG] Text query: '{query}'")
            eel.senderText(query)

        # ❌ If nothing was spoken or sent
        if not query.strip():
            speak("I didn't hear anything. Please try again.")
            eel.ShowHood()
            return

        # 🧠 Step 2: Check for built-in commands
        if 'open' in query:
            print("[INFO] Running open command")
            from engine.features import openCommand
            openCommand(query)

        elif 'on youtube' in query:
            print("[INFO] Running YouTube command")
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if contact_no != 0:
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")

                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)
            else:
                speak("I couldn't find the contact you mentioned.")
                eel.ShowHood()

        # 💬 Step 3: Fallback to AI ChatBot
        else:
            print("[INFO] No matching command. Using ChatBot.")
            reply = chatBot(query)
            print("[INFO] Bot Reply:", reply)
            speak(reply)
            eel.receiverText(reply)
            eel.ShowHood()

    except Exception as e:
        print("❌ An error occurred:")
        traceback.print_exc()
        speak("An error occurred while processing your command.")
        eel.ShowHood()
