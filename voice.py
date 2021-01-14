import webbrowser
import pyttsx3
import os
import pyaudio
print("""-------------------------------------------------------OPENING---------------------------------------------------------
                                                   
                                
                                                     Please Wait!
""")

engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
engine.say("hello Mam")
engine.say("i am your assistant ")
engine.say("Regina Phalangeeee")
engine.say("how can i help you")
engine.runAndWait()




while True: 
 print("""
 ......................................................WELCOME!........................................................
 """)

 ask=input("Want to continue Yes/No?:")
 if ask == "yes":
      engine.say("kindly enter your requirements by selecting one of the choices from the menu")
      engine.runAndWait()
      print("""                                 
                                          Enter your requirements by selecting one of the choices:                  

MENU
                                                                    
Press 01:  To open google
Press 02:  To open calendar
Press 03:  To open gmail
Press 04:  To create a file
Press 05:  To open any file in notepad
Press 06:  To open control panel
Press 07:  To open Whatsapp web
Press 08:  To open Youtube
Press 09:  To open command prompt
Press 10:  To open aws management console
press 11:  To open System Details
Press 12:  To show the IP address of system
Press 13:  To open PowerShell
Press 14:  To clear screen
Press 15:  To get current list of all tasks running on your pc
Press 16:  To list all drivers of your system
Press 17:  To create a folder
Press 18:  To show history
Press 19:  To show what device last woke your PC from a sleep state   
Press 20:  It will show detailed power consumption report for your PC
Press 21:  To shut down your system  
Press 22:  To restarts your PC and launches the Advanced Start Options menu(This is useful if you want to restart your computer for troubleshooting purposes.)       
Press 23:  To automatic scan and repair tools that focuses on windows system 
Press 24:  To show today's date 
""")
      ch=input("Enter your choice :")

      
   
      if ("01" in ch):
       engine.say("opening google")
       engine.runAndWait()
       webbrowser.open("https://www.google.com")
 
      elif ("02" in ch):
        engine.say("Opening calendar")
        engine.runAndWait()
        webbrowser.open("https://www.timeanddate.com/calendar/")

      elif ("03" in ch):
       engine.say("opening gmail")
       engine.runAndWait()
       webbrowser.open("https://mail.google.com/mail/u/0/")
      
      elif ("04" in ch):
        engine.say("Enter the file name you want to create")
        engine.runAndWait()
        file=input("file name:")
        loc=input("enter location where you want to create:")
        os.system("cd {}".format(loc))
        pyttsx3.speak("you can feed your data here")
        os.system("notepad {}".format(file))
        

      elif ("05" in ch):
       fi=input("Enter file name:")
       loc=input("Enter the absolute file location:")
       os.system("cd {}".format(loc))
       os.system("notepad {}".format(fi))
       

      elif ("06" in ch):
       engine.say("Opening control pannel")
       engine.runAndWait()
       os.system('control panel')
      
        
      elif ("07" in ch):
       engine.say("opening whatsapp web")
       engine.runAndWait()
       webbrowser.open("https://web.whatsapp.com/")
      
      elif("08" in ch):
        engine.say("opening youtube")
        engine.runAndWait()
        webbrowser.open("https://www.youtube.com/")
      elif("09" in ch):
        engine.say("opening command prompt")
        engine.runAndWait()
        os.system("start cmd")
          
      elif("1" in ch) and ("0" in ch ):
         engine.say("Opening AWS Management Console")
         engine.runAndWait()
         webbrowser.open("https://console.aws.amazon.com/console/home?region=us-east-1#")

      elif("11" in ch):
        os.system("systeminfo")
        engine.say("here are some system information")
        engine.runAndWait()
      elif("12" in ch):
        os.system("ipconfig")
        engine.say("here is your system ip")
        engine.runAndWait()
      elif("13" in ch):
        os.system("start powershell")
      elif("14" in ch):
        engine.say("clearning screen")
        engine.runAndWait()
        os.system("cls")
      elif("15" in ch):
       engine.say("showing task lists")
       engine.runAndWait()
       os.system("tasklist")
      elif("16" in ch):
        engine.say("here are all drivers lists")
        engine.runAndWait()
        os.system("driverquery")
      elif("17" in ch):
        folder=input("enter your folder name you want to create")
        os.system("mkdir {}".format(folder))
        rec=pyttsx3.speak("Folder created!")
        print(rec)
      elif("18" in ch):
        engine.say("showing history")
        engine.runAndWait()
        his=os.system("doskey /history")
        print(his)
     
      elif("20" in ch):
        engine.say("It will show the Wake count")
        engine.runAndWait()
        os.system("powercfg /lastwake")
      elif("20" in ch):
        
        engine.say("Note")
        engine.say("It requires administartor permission")
        os.system("powercfg /energy")
      elif("21" in ch):
        engine.say("shutting down please wait")
        engine.runAndWait()
        print("Please wait!")
        os.system("shutdown /s")
      elif("22" in ch):
         enginge.say("Restarting your system")
         engine.runAndWait()
         os.system("shutdown /r /o")
      elif("23" in ch):
         engine.say("For this you must have admin privilleges")
         engine.say("it will take time")
         engine.runAndWait()
     
         os.system("sfc /scannow")
      elif("24" in ch):
       engine.say("Showing today's date")
       engine.runAndWait()
       os.system("date")
         
      
      else: 
       print("Do not support")  
 else:
    os.system("cls")
    print("........................................................Come Soon!......................................................")
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.say("Thank you, Mam  ")
    engine.say("See you later! ")
    engine.runAndWait()
    exit()