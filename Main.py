import os
import eel
from engine.features import *
from engine.command import *
from engine.auth import recoganize
  
def start ():  ## yeah humne multi threading ke liye kiya hai esliye start func bnaya 
    ## for connecting frontend file we use eel function
 eel.init("Frontend")
 ## calling opening  v.a sound function 
 playAssistantSound()
 @eel.expose
 def init(): 
     eel.hideLoader()
     speak("Ready for face Authentication")
     flag= recoganize.AuthenticateFace()
     if flag==1:
        eel.hideFaceAuth()
        speak("Face Authentication  is successful")
        eel.hideFaceAuthSuccess()
        speak("Hello Friend,How May I Assist you ?")
        eel.hideStart()
        playAssistantSound()
     else:
        speak("Face Authentication is Fail")
 ## taki v.a  jabhi open hoon jab face authenticate hoon jye 




## for opening our V.a in App mode
 os.system('start msedge.exe  --app="http://localhost:8000/index.html"')

## for knowing eel ki kaunsi frontent file hai hamari (index.html)
 eel.start("index.html", mode=None,host="localhost", block=True)  

