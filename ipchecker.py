import os
import sys
import re
import pip
import time
import datetime
import smtplib
import importlib
# check if user has installed ipgetter module
try:
    import ipgetter
except:
    # module not found, install and import this will only work on windows for now, working on a *nix solution
    try:
        print("Error importing ipgetter, must install")
        pip.main(['install', "ipgetter"])
    except:
        print("installing for unix")
        os.system("pip install ipgetter")
finally:
    globals()["ipgetter"] = importlib.import_module("ipgetter")
import subprocess
from email.mime.text import MIMEText

server = "" # outgoing smtp server
port = # enter the outgoing port number here
username = "" # username used to log in to mail account
password = "" # password used to login to mail account
sender = "" # this is what will appear in the from field
destination = "" # where are you sending emails when the IP address changes
curip = ipgetter.myip()
oldip = " "
text_subtype = 'plain'
subject = " "




def oldIP():
    try:
        ipfile = open("ipaddress.txt", 'r+')
        # print("open file")
        ipfile.close()
    except:
        print("create file")
        ipfile = open("ipaddress.txt", 'a+')
        ipfile.close()

    ipfile = open("ipaddress.txt",'r+')
    ipfile.seek(0)
    oldip = ipfile.readline()
    ipfile.close()
    return oldip
    
def checkip():
    
    # check os and clear terminal
    try:
        os.name
        if os.name == 'nt':
            # windows systems
            try:
                os.system('cls')    # This is a deprecated function please update to subprocess
                # resize the running cmd window to reduce "whitespace"
                os.system("mode con: cols=50 lines=7")
                # subprocess.run(["cls",])
                # print("User is running Windows")
            except:
                #print("error with subprocess code")
        else:
            os.system('clear')  # This is a deprecated function please update to subprocess
            # subprocess.run(["clear",])
            # print("User is running Unix")
            
    except:
        print("error checking system")
    
    print("checking ip address")
    ipfile = open("ipaddress.txt", 'r+')
    ipfile.seek(0)
    print("the current IP address is: " + curip)
    print("\n")
    print("The IP address on record is: " + oldIP())
    # check old ip
    if curip == oldIP():
        # print("SAME, waiting to check again")
        logip()
        time.sleep(3600)
        checkip()
        
    else:
        # print("different")
        sendmail()
        logip()
        time.sleep(3600)
        checkip()
        
def logip():
    
    print("logging IP address")
    ipfile = open("ipaddress.txt" , 'r+')
    ipfile.seek(0)
    ipfile.write(curip)
    ipfile.truncate()
    ipfile.close
    log = open("iplog.txt", 'a+')
    now = datetime.datetime.now()
    log.write(now.strftime("%m-%d-%Y %H:%M:%S ") + "the IP address is " + curip + "\n")
    
    log.close
    print("Waiting before trying again")
    print("checking again in an hour")
    
    
    
    
def sendmail():
    # print("trying connection")
    smtp = smtplib.SMTP_SSL(server, port)
    # print("trying to login")
    try:
        smtp.login(username, password)
        print("login success")
    except:
        print("error logging in")
    
    message = "This email is to let you know that your home IP address has changed. \n\n The new address is : " + curip + "\n\nThis has changed from the IP address of: " + oldIP() + "\n\nYou will need to adjust the IP settings within your minecraft client. \n\nThank you."
    msg = MIMEText(message, text_subtype)
    msg['Subject'] = subject
    msg['From'] = sender
    try:
        smtp.sendmail(sender, destination, msg.as_string())
        print("mail sent")
        logip()
    except:
        print("unable to send mail")
    smtp.quit()
    



checkip()

print("code found a way to reach the end")
ipfile = open("ipaddress.txt",'r+')
ipfile.seek(0)
print("Your ip address at last check was: " + ipfile.readline())