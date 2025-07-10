import re 
import os 
import time 
def extract_yt_term(command): ## yeah function query mein se play and youtube ko hata tha hai aur jo search krna hai woooh rkhta hai
    pattern = r"play\s+(.*?)\s+youtube"
    match = re.search(pattern, command, re.IGNORECASE) ## yesh search krta hai jo hum search kr rahe hai wooh  shi hai na aur ignorecase mtlb capital ho ya lower mein frk  nhi pdtha
    return match.group(1) if match else None ## agar pattern se match hota hai result aata hai wrna none 
 
 # hum jo siri  wave ko bolte hai query jaise  jarvis can you open youtube toh hmre liye jarvis and can you word 
 # (cont..) toh hmre liye aise words kaam ke nhi hai toh wooh unko remove krta hai 
def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string
 ## example of remove_words 
#input_string = "make a phone call to papa"
#words_to_remove = [ 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', '']

#result = remove_words(input_string, words_to_remove)
#print(result)

# key events like receive call, stop call, go back
import os
import time

# ✅ Set correct ADB path here (double quotes around full path are fine)
ADB_PATH = '"C:\\Users\\agast\\Downloads\\platform-tools-latest-windows\\platform-tools\\adb.exe"'

# Send key event like ENTER, BACK, HOME, etc.
def keyEvent(key_code):
    command = f'{ADB_PATH} shell input keyevent {key_code}'
    os.system(command)
    time.sleep(1)

# Tap anywhere on screen
def tapEvents(x, y):
    command = f'{ADB_PATH} shell input tap {x} {y}'
    os.system(command)
    time.sleep(1)

# Insert text into an input field
def adbInput(message):
    command = f'{ADB_PATH} shell input text "{message}"'
    os.system(command)
    time.sleep(1)

# Go back multiple times using BACK key
def goback(times=4):
    for _ in range(times):
        keyEvent(4)  # 4 = KEYCODE_BACK

# (Optional) Replace spaces with %s (if needed for older Androids)
def replace_spaces_with_percent_s(input_string):
    return input_string.replace(' ', '%s')


