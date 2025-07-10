from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
import os 
from engine.command import speak
import re 
import pywhatkit as kit
import sqlite3
import webbrowser
from engine.helpers import  extract_yt_term
import pvporcupine
import pyaudio
import struct   ## esse hum different data types ko ek variables mein laa skte hai yaar 
import time 
from engine.helpers import remove_words
from urllib.parse import quote
import subprocess
import pyautogui
from hugchat import hugchat
import google.generativeai as genai
from huggingface_hub import InferenceClient
## opening sound laane ke liye v.a mein function and eel for frontend  ke access ke liye
@eel.expose
def playAssistantSound():
    music_dir = "C:\\Users\\agast\\OneDrive\\Desktop\\Ai projects\\virtual assistant\\photos\\audio.mp3"
    playsound(music_dir)  

## for open function mtlb jo bola hai ki open karo woooh open krega 

# connect to the database (assuming the DB file is in the same folder, change path if not)
conn = sqlite3.connect("Deepa.db")  
cursor = conn.cursor()

def openCommand(query):
    query = query.replace(ASSISTANT_NAME,"") ## humne jaise jo apne v.a  ka naam rakha hai  usse replace krega jaise deepa  open notepad bola  wooh bas open notepad krega  
    query = query.replace("open","") ## yeah open ko replace  krega jaise open notepad yeah sirf notepad krega open hata dega  
    query = query.lower() ## jo bola wooh small mein print aayega 
    query = query.strip()
    
    # Remove characters that break PowerShell
    query = re.sub(r"[&|><]", "", query)

    app_name = query.replace(" ", "").replace("-", "")## esmein hum query ko app name mein store kr rahe  hai strip krke query 

    if app_name != "": ## agar hmri  query khaali nhi  hogi toh 

        try:
            cursor.execute(
                'SELECT path FROM deepa_virtual_assistant  WHERE LOWER(name)=?', (app_name.lower(),)) 
            results = cursor.fetchall()
            ## agar hmri app_name match krta hai name se hmri table mein toh result ek variable hai jo saare match kre database se wooh store krta hai 

            if len(results) != 0: ##  eska mtlb hai result empty nhi hue hai toh mtlb match hua hai app_name aur db mein 
                speak("Opening " + query)  ##  yeah hmri v.a bolega 
                
                # ✅ FIX STARTS HERE
                path = results[0][0]
                if path.startswith("start "):
                    os.system(path)
                else:
                    os.startfile(path)
                # ✅ FIX ENDS HERE

            elif len(results) == 0:  ## agr results empty hai toh hum db web_command mein search krenge
                cursor.execute(
                    'SELECT URL FROM web_command WHERE LOWER(name)=?', (app_name.lower(),))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening " + query) ## agr hmri query dono hi db mein nhi milti toh mtln wooh app jo command prompt hia wooh os khulega jaise open notepad wooh open krega 
                    try:
                        os.system('start ' + query)
                    except:
                        speak("not found")
        except:  ## agar query kahi nhi milega toh yeah print hoga  
            speak("some thing went wrong")
      

def PlayYoutube(query):
    search_term = extract_yt_term(query)  ## mtlb jo search item hai usmein extract lagana 
    if search_term:
        speak("playing " + search_term + " on youtube") ## speak se jo hmri query hai wooh hmra v.a bolega
        kit.playonyt(search_term) ## pywhatkit se humhara search_item play hoga 
    else:
        speak("Sorry, I couldn't understand what to play on YouTube.")

        
def hotword():
    porcupine=None # variables hai jo initialize kr rahe hai 
    paud=None
    audio_stream=None ## background mein microphone ko chalane ke liye use hota hai 
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("d")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
        


# fiinding contact 
def findContact(query):
    
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])  ## eska mtlb hai  jo  hmri query hai agar usmein ek jaise  naam hai toh jo sabse pehle save hai wooh pehle  aayega  
        mobile_number_str = str(results[0][0]) ## jo  bhi number milega use string meinn convert  krna 
        if not mobile_number_str.startswith('+91'): 
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
def whatsApp(mobile_no, message, flag, name):
    from engine.command import speak
    import subprocess
    import pyautogui
    import time
    from urllib.parse import quote

    # Build WhatsApp URL
    if flag == 'message':
        encoded_message = quote(message)
        whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    else:
        whatsapp_url = f"whatsapp://send?phone={mobile_no}"

    # Open WhatsApp Desktop
    full_command = f'start "" "{whatsapp_url}"'
    subprocess.run(full_command, shell=True)

    # Wait for WhatsApp to load the chat
    time.sleep(4)

    if flag == 'message':
        pyautogui.press("enter")
        speak("Message sent successfully to " + name)

    elif flag == 'call':
        speak("Calling " + name)
        # ✅ Your actual voice call button position
        pyautogui.moveTo(1797, 106)
        time.sleep(0.5)
        pyautogui.click()

    elif flag == 'video call':
        speak("Starting video call with " + name)
        # ✅ Your actual video call button position
        pyautogui.moveTo(1727, 106)
        time.sleep(0.5)
        pyautogui.click()





## function for automatically phone call through phone 
def makeCall(name, mobileNo):
    mobileNo = mobileNo.replace(" ", "")  ## ensure no space in mobile number
    speak("Calling " + name)

    # Correct ADB path with quotes
    adb_path = '"C:\\platform-tools-latest-windows (2)\\platform-tools\\adb.exe"'
    adb_command = f'{adb_path} shell am start -a android.intent.action.CALL -d tel:{mobileNo}'

    os.system(adb_command)

import os
import time

ADB_PATH = '"C:\\Users\\agast\\Downloads\\platform-tools-latest-windows\\platform-tools\\adb.exe"'  # Update if needed


def sendMessage(message, contact_no, name=None):
    print(f"Sending to {name or contact_no}: {message}")

    # Escape spaces properly
    safe_message = message.replace(" ", "%s")

    command = (
        f'{ADB_PATH} shell am start '
        f'-a android.intent.action.SENDTO '
        f'-d sms:{contact_no} '
        f'--es sms_body "{safe_message}" '
        f'--ez exit_on_sent true'
    )

    print(f"[DEBUG] ADB command: {command}")
    os.system(command)
    time.sleep(1)

    # Simulate pressing ENTER to send
    os.system(f"{ADB_PATH} shell input keyevent 66")  # KEYCODE_ENTER

