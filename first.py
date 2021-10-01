#step 1 : we are importing the necessary library
import speech_recognition as sr
import os
import pyttsx3
import sys
engine = pyttsx3.init()

#step 2 : we are starting the main code part for our code
r = sr.Recognizer()
def seekh():
  pyttsx3.speak("let me explain about its working") 
  engine.runAndWait()
  pyttsx3.speak("I am here to fulfill ur wishes") 
  engine.runAndWait()
  pyttsx3.speak("suppose you want to open chrome so just type chrome and i will open chrome")
  engine.runAndWait()
  pyttsx3.speak("You can say... I want to draw.... and I will open paint")
  engine.runAndWait()
  pyttsx3.speak("I hope that you now understand how to use this.")
  pyttsx3.speak("I am waiting for your wishes")
  
#this is not a start button
def start():
  print("chat with me with your requirements : "  , end='')
  while 1:
            p=input()
            if ("explain" in p) or ("forgot" in p) or ("how to" in p) or ("what should i do" in p):
               pyttsx3.speak("i will help you")
               seekh()
            elif ("chrome" in p) or ("internet" in p) or ("explorer" in p) or ("google" in p):
               pyttsx3.speak("opening chrome")
               os.system("chrome")
            elif ("notepad" in p) or ("jupyter" in p) or ("text" in p) or ("editor" in p) or ("write" in p):
               pyttsx3.speak("opening notepad")
               os.system("notepad")
            elif ("draw" in p) or ("paint" in p) or ("colour" in p) or ("sketch" in p):
               pyttsx3.speak("opening ms paint")
               os.system("mspaint")
            elif ("exit" in p)  or ("quit" in p) or("bye" in p) or("leave" in p):
               pyttsx3.speak("goodbye. Hope to see you soon")
               os.exit()
            elif ('calculator' in p):
               pyttsx3.speak('Opening your calculator')
               os.system('calc')
            elif ('facebook' in p) or ("fb" in p):
               pyttsx3.speak('opening facebook')
               os.system('start  http://www.facebook.com/')
            elif ('whatsapp' in p):
               pyttsx3.speak('Opening your whatsapp')
               os.system('start https://www.whatsapp.com/?lang=en')
            elif ('songs' in p) or ("listen" in p):
               pyttsx3.speak('here it comes')
               os.system('start https://gaana.com/')
            elif ('watch' in p) or ("movies" in p):
               pyttsx3.speak('opening youtube')
               os.system('start https://www.youtube.com/')
            else:
               pyttsx3.speak("not avilable ")
               engine.runAndWait()
               pyttsx3.speak("please enter something valid ")



def verify():
  print("enter your password ")
  i=3
  while 1:
            s=input()
            if ("first" in s):
              pyttsx3.speak("correct password")
              break
            elif ("forgot" in s) or ("don't remember" in s):
              pyttsx3.speak("sorry u can't use this ")
              os.exit()
            else:
              i-=1
              pyttsx3.speak("wrong password")
              pyttsx3.speak("you have" +str(i)+ "attempt left")
              #pyttsx3.speak(i)
              #pyttsx3.speak("attempt left")
              if i == 0:
                pyttsx3.speak("no attempt left")
                os.exit()
    
    


 
def check():
  while 1:
            q= input()
            if ("yes" in q) or ("YES" in q) or ("Yes" in q):
               pyttsx3.speak("you are quite intelligent")
               engine.runAndWait()
               start()
               break
            elif ("no" in q) or ("NO" in q) or ("No" in q):
               pyttsx3.speak("no problem")
               seekh()
               start()
            elif ("out" in q) or ("exit" in q) or ("quit" in q) or ("leave" in q):
               pyttsx3.speak("goodbye")
               break
            else:
               pyttsx3.speak("please enter yes or no")




pyttsx3.speak("Welcome")
engine.runAndWait()
pyttsx3.speak("please enter password")
verify()


print("do you know how to use it")
pyttsx3.speak("I hope you know how to use this ")
engine.runAndWait()
pyttsx3.speak("enter yes if you know everthing ")
engine.runAndWait()
pyttsx3.speak("or enter no if you want me to explain it to you")

check()


