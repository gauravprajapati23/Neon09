import subprocess
import os
import time
from datetime import datetime
import sys
now = datetime.now()
t=now.strftime('%I:%M:%p')
print(t)
print("Listening...")

inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print("\033[95m You said: ",str(inp))

def system():
     if inp == " ":
         subprocess.call(["termux-tts-speak"," "])

#Hello functions
     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
         
     elif "hey" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
         
     elif "hello neon" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
         
     elif "hey neon" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])


#Thank you functions
     elif "thank you so much" in inp:
         subprocess.call(["termux-tts-speak","You're welcome,sir "])
    
     elif "Thank you" in inp:
         subprocess.call(["termux-tts-speak","You're welcome,sir "])
     
     elif "thank you" in inp:
         subprocess.call(["termux-tts-speak","You're welcome,sir "])
      
     elif "Thank you so much" in inp:
         subprocess.call(["termux-tts-speak","You're welcome,sir "])
      
      
#Shutdown functions
     elif "Shut Down" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()
         
     elif "shutdown" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()
         
     elif "shut down" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()
         

#Show Battery status Functions            
     elif "show battery status" in inp:
         subprocess.call(["termux-battery-status"])
    
     elif "show battery" in inp:
         subprocess.call(["termux-battery-status"])
    
     elif "tell me about battery" in inp:
         subprocess.call(["termux-battery-status"])


#Sleep Functions
     elif "go on sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)
         
     elif "goto sleep mode" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)

     elif "goto sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)


#Calling functions
     elif "make a call" in inp:
         os.system("termux-telephony-call +91")
         
     elif "call my Mom" in inp:
         os.system("termux-telephony-call 9021016359")
         
     elif "call my mom" in inp:
         os.system("termux-telephony-call 9021016359")
         
     elif "call my Papa" in inp:
         os.system("termux-telephony-call 7057593627")
         
     elif "call my Papa" in inp:
         os.system("termux-telephony-call 7057593627")


#Flashlight On functions
     elif "flashlight" in inp:
         os.system("termux-torch on")     
     elif "turn on torch" in inp:
         os.system("termux-torch on")
     elif "torch on" in inp:
         os.system("termux-torch on") 
     elif "then on torch" in inp:
         os.system("termux-torch on")               
     elif "Then on torch" in inp:
         os.system("termux-torch on") 
     elif "turn on flashlight" in inp:
         os.system("termux-torch on")
     elif "flashlight off" in inp:
         os.system("termux-torch on")

  
#Torch On functions       
     elif "then off flashlight" in inp:
         os.system("termux-torch off")
     elif "off" in inp:
         os.system("termux-torch off")
     elif "of" in inp:
         os.system("termux-torch off")  
     elif "turn off flashlight" in inp:
         os.system("termux-torch off")
     elif "turn off flashlight" in inp:
         os.system("termux-torch off")
     elif "done off flashlight" in inp:
         os.system("termux-torch off")
     elif "done off torch" in inp:
         os.system("termux-torch off")
     elif "then off torch" in inp:
         os.system("termuxx-torch off")         
     elif "torch off" in inp:
         os.system("termux-torch off")  


#Open YouTube
     elif "open YouTube" in inp:
         os.system("termux-open https://m.youtube.com")
     elif "launch YouTube" in inp:
         os.system("termux-open https://m.youtube.com")


#Open Google
     elif "open Google" in inp:
         os.system("termux-open https://www.google.co.in/")      
     elif "launch Google" in inp:
         os.system("termux-open https://www.google.co.in/")


#Open Instagram
     elif "launch Instagram" in inp:
         os.system("termux-open https://www.instagram.com/") 
     elif "open Instagram" in inp:
         os.system("termux-open https://www.instagram.com/") 
         
         
#View Contacts
     elif "view contacts" in inp:
         os.system("termux-contact-list")
     elif "open contacts" in inp:
         os.system("termux-contact-list")
     elif "show me all contacts" in inp:
         os.system("termux-contact-list")
     elif "view contact" in inp:
         os.system("termux-contact-list")
     elif "open contact" in inp:
         os.system("termux-contact-list")
     elif "show me all contact" in inp:
         os.system("termux-contact-list")

         
#Intro                           
     elif "who are you" in inp:
         subprocess.call(["termux-tts-speak","I am your virtual assistant , Neon"])
     elif "what is your name" in inp:
         subprocess.call(["termux-tts-speak","you can call me Neon "])
     elif "tell me your name" in inp:
         subprocess.call(["termux-tts-speak","you can call me Neon "])
     
     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","I am designed by Gaurav Prajapati"])
         
      
#Timming
     elif "what is time" in inp:
         subprocess.call(["termux-tts-speak",t])
     elif "tell me time" in inp:
         subprocess.call(["termux-tts-speak",t])
     elif "what is timing" in inp:
         subprocess.call(["termux-tts-speak",t])
     elif "tell me timing" in inp:
         subprocess.call(["termux-tts-speak",t])     
         
         
     else:
        subprocess.call(["termux-tts-speak","Function is out of my program."])
 
system()

os.system("python main.py")
