## multi threading ke liye hai  taaki dono proceeses saath mein work aaye 
import multiprocessing
#subprocess is a built-in Python module that lets you run external programs or commands from your Python code
import subprocess
 
# To run Jarvis ( yeah frontend mein  run hoga )
def startJarvis():
     # Code for process 1
    print("Process 1 is running.")
    from Main import start
    start()

    # To run hotword ( yeah backend mein run hoga )
def listenHotword():
    # Code for process 2
    print("Process 2 is running.")
    from engine.features import hotword
    hotword()

 # Start both processes
if __name__ == '__main__':
        
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start() ## yeah jarvis ko start krne ke liye hai 
        subprocess.call([r'device.bat'])
        p2.start() ## yeah hotword detect krne ke liye hai 
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")      