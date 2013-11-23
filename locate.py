#!/usr/bin/env python
# linux server location for ip lookup
#49 lines to page
# Teck
import socket
import subprocess
from socket import *
from threading import *
import os
import sys
import urllib2
import time
import re
import random
# 96 88 89 90 92 93 94 103 104 108 109 110 112 113 11\



class bcolors:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERL = '\033[4m'
        ENDC = '\033[0m'
        backBlack = '\033[40m'
        backRed = '\033[41m'
        backGreen = '\033[42m'
        backYellow = '\033[43m'
        backBlue = '\033[44m'
        backMagenta = '\033[45m'
        backCyan = '\033[46m'
        backWhite = '\033[47m'

def disable(self):
    self.PURPLE = ''
    self.CYAN = ''
    self.BLUE = ''
    self.GREEN = ''
    self.YELLOW = ''
    self.RED = ''
    self.ENDC = ''
    self.BOLD = ''
    self.UNDERL = ''
    self.backBlack = ''
    self.backRed = ''
    self.backGreen = ''
    self.backYellow = ''
    self.backBlue = ''
    self.backMagenta = ''
    self.backCyan = ''
    self.backWhite = ''
    self.DARKCYAN = ''











while True:

   def local():
         try:
             print bcolors.YELLOW + "local ip information" +bcolors.ENDC
             ch = (raw_input("Is this a local look up?(Y/N): "))
             if ch == "Y" or ch == "y":
                    locallook()
             elif ch == "n" or ch == "N":
                      os.system("clear")
                      print bcolors.DARKCYAN + "[+]Skipping local look up "+ bcolors.ENDC
                      time.sleep(0.3)
                      pass
             elif ch == "":
                      time.sleep(0.1)
                      print bcolors.RED + "[!]You left the question blank"+bcolors.ENDC
                      os.system("clear")
                      return local()
             elif ch == "Goto portscan":
                      print "Skipping to portscan"
                      menu()

             else:
                time.sleep(0.3)
                print "[*]Invalid option"
                os.system("clear")
                return local()

         except KeyboardInterrupt:
                 print "\n\n"+"quitting"
                 raise SystemExit


   def portscan():
        try:
            host = (raw_input("host : " ))
            #strt = input("start ")
            #end = input("end ")
            print "=" * 40
            print "Now port scanning" , host
            print "=" * 40
            print "Well run a ping sweep first"
            time.sleep(0.2)
            os.system("ping  "+ host+ " -c 5")
            print "[*]ping sweep complete"+'\n'+"Now port scanning" + bcolors.ENDC
            portlst = 21,22,23,443
            for port in portlst:
                s = socket(AF_INET, SOCK_STREAM)
                if s.connect_ex((host,port)) == 0:
                      print  bcolors.GREEN + "Port :",port,"[!]Open" +bcolors.ENDC

                else:
                     print bcolors.RED + "Port :",port," Closed" + bcolors.ENDC
                     s.close()
        except KeyboardInterrupt:
                print "Ctl-C caught"
                raise SystemExit

        finally:
            print "scan complete for ",host
            options()

   def menu():
            print "Would like to port scan the host(Y/N)"
            a = (raw_input("Choice: "))
            if a == 'Y' or a == 'y':
                  print "How would you like perform this scan"
                  print bcolors.CYAN + "=" * 10
                  print "1) -->  Common port scan"
                  print "2) -->  Specifiyed range scan "
                  print "3) -->  Single port scan"
                  print "=" * 10 + bcolors.ENDC
            #elif a == 'N' or a == 'n':

                  y = input("Choice: ")
                  if y == 1:
                        portscan()
                        return menu()
                  elif y == 2:
                          portrange()
                          return menu()
                  elif y == 3:
                          singleport()
                          return menu()
                  elif y == "clear":
                          clear()

                  else:
                     time.sleep(0.3)
                     print "Invalid choice"
                     return menu()




   def update():
          print "Would you like to update to script"
          o = (raw_input("Y/N"))
          if o  == "Y":
                 print "Proceeding"
                 print "updating the script uses gith\n\nI hope u have github setup"
                 os.chdir(/root)
                 print "Removing old directory"
                 os.system("rm -rf locate")
                 print "Getting the updated script"
                 os.system("git clone git://github.com/Tecksupport/locate")
                 os.getcwd()
                 print "Changing dircetories"
                 os.chdir("/root/locate")
                 print "making script excutable"
                 os.system("chmod 777 locate.py")
                 print "Moving back dirs"
                 os.chdir("/root")
                 print "All done"
                 options()

          else:
             print "its Kind of dumb not to update your script but ok then\n\nwhat ever floats your boat"
             options()












   def portrange():
         try:
            print host
            first = input("Enter start range: ")
            last  = input("Enter end range: ")
            print "=" * 20
            print "specified scanner"
            print "=" * 20
            print "ping sweep begin "
            os.system("ping "+ host+ " -c 5") + bcolors.YEELOW
            print "ping complete"+'\n'+"Now port scanning" + bcolors.ENDC
            for port in range(first, last):
                s = socket(AF_INET, SOCK_STREAM)
                #message = s.recv(1024)
                if s.connect_ex((host,port)) == 0:
                   print bcolors.GREEN + "Port : ",port, "Open" + bcolors.ENDC
                      # print "[!]"+str(message)
                else:
                    print bcolors.RED + "Port : ",port, "Closed" + bcolors.ENDC
                    s.close()


         finally:
            print "Scan complete for "+ host
            options()


   def clear():
           os.system("clear")
           options()




   screenLock = Semaphore(value=1)
   def singleport():
         try:
             host = (raw_input("Enter host: "))
             port = input("Enter port num: ")
             print "=" * 30
             print "Single port and application scanning"
             print "=" * 30
             print "Talking to host first\r\n"
             os.system("ping " + host+ " -c 5")
             print "Complete\nScanning the port",port
             s = socket(AF_INET, SOCK_STREAM)
             s.connect((host, port))
             s.send('Tecks port scan\r\n')
             msg = s.recv(100)
             screenLock.acquire()
             print bcolors.GREEN + '[!]%d/tcp open'%port + bcolors.ENDC
             print "[+] " + str(msg)
         except:
              screenLock.acquire()
              print bcolors.RED +  "[-]%d/tcp Closed"%port + bcolors.ENDC
              s.close()

         finally:
            screenLock.release()
            s.close()
            print "Scanner complete for ",host
            options()



   def util():
         print bcolors.CYAN + "*" * 10
         print "1 ->> nslookup"
         print "2 ->> ping"
         print "3 ->> finger"
         print "4 ->> dig"
         print "5 ->> whois"
         op =  input("Enter choice: ")
         if op == 1:
                nslook()
                options()
         if op == 2:
                ping()
                options()
         if op == 3:
                finger()
                options()
         if op == 4:
                dig()
                options()
         if op == 5:
                whois()
                options()

   def dig():
        print "Choice of dig"
        targ = (raw_input("Enter host to dig: "))
        os.system("dig " + targ)
        time.sleep(0.04)
        options()
   def whois():
         print "Choice of whois"
         host = (raw_input("Enter host : "))
         os.system("whois " + host)
         time.sleep(0.04)
         options()



   def nslook():
        print "NSlookup"
        n = (raw_input("Would you like to do a nslookup?(Y/N)"))
        if n == "Y" or n == "y":
              print "[OK]"
              trg = (raw_input("Plaese enter the host name: "))
              os.system("nslookup  " + trg )
              pass
        if n == "N" or n == "n":
              print "Moving on"
              pass
        if n == "Skip portscan":
              print "Skipping"
              menu()

   def locallook():
         print "Looking up the local IP address"
         ff = urllib2.urlopen("http://showmemyip.com")
         s = str(ff.read())
         ff.close()
         pattern = r'(<.*?>)'
         ff = open('local.txt','w')
         ff.write(re.sub(pattern,'',s))
         ff.close()
         locall = open("local.txt").readlines()[28],
         for lines in locall:
             print (lines)
             time.sleep(0.3)
         ip = (lines)
         os.system("clear")
         print bcolors.BOLD+ bcolors.UNDERL+bcolors.RED + " Now add the ip below   " +ip +bcolors.ENDC



   def bar():
        prgbar_width = 18
        sys.stdout.write("[%s]" % (" " * prgbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (prgbar_width+1))
        for i in xrange(prgbar_width):
            time.sleep(0.1)
            sys.stdout.write(bcolors.DARKCYAN +"~" + bcolors.ENDC)
            sys.stdout.flush()
            sys.stdout.write("")

   def finger():
       print "This can be done with a finger command"+'\n'+"would you like me to run the finger commnd"+'\n'+"1 for Yes 2 for No"
       fi = input()
       if fi == 1:
              print "using the finger command"
              os.system("finger")
              pass
       elif fi == 2:
                print "going foward then"
                pass
   def ping():
        try:
           print "Would you like to ping to see if the host is alive"
           p = (raw_input("(Y/N)"))
           if p  == "Y" or p == "y":
                  print "Ok lets ping the host"
                  host = (raw_input("Enter the host IP: "))
                  print "pinging ==>[",host,"]" + bcolors.YELLOW
                  os.system('ping ' + host)
                  pass
           elif p == "N" or p == "n":
                   print "Then ill pass on then"
                   pass
        except KeyboardInterrupt:
               time.sleep(0.1)
               print '\n'+ bcolors.backRed +"going back to main"+ bcolors.ENDC
               pass


   def options():
         print bcolors.YELLOW + "Choose a choice" + bcolors.ENDC
         print bcolors.CYAN + "*" * 10
         print "1 >> Outside Ip Lookup"
         print "2 >> Local IP Lookup"
         print "3 >> Port scanner"
         print "4 >> Utilites"
         print "5 >> Update" + bcolors.ENDC
         c = input("->>__ ")
         if c == 1:
               pass
         elif c == 2:
                 local()
         elif c == 3:
                 menu()
         elif c == 4:
                 util()
         elif c == 5:
                 update()

         else:
           print"[!] Invalid choice"
           time.sleep(0.2)
           return options()









   os.system("clear")
   print  bcolors.CYAN + "============================"
   print "  Ip information parser     "
   print "============================"
   print "server version 1.6" + bcolors.ENDC
   options()
   #  ping()
   #nslook()

# Add this all to a menu so this way its all over the place

   try:
       f = bcolors.BOLD + "Enter First Octant: " + bcolors.ENDC
       s = bcolors.BOLD + "Enter second Octant:" + bcolors.ENDC
       t = bcolors.BOLD + "Enter Third Octant: " + bcolors.ENDC
       fo = bcolors.GREEN + "Enter fourth Octant: "+ bcolors.ENDC
       fail = bcolors.RED + "You entered this blank"+bcolors.ENDC
       wait = bcolors.CYAN + "Continue?(Y/N)" +bcolors.ENDC


       f = (raw_input(f))
       if f == "":
             print fail
             f = (raw_input("Enter first Octant: "))

       s = (raw_input(s))
       if s == "":
             print fail
             s = (raw_input("Enter second Octant: "))

       t = (raw_input(t))
       if t == "":
             print fail
             t = (raw_input("Enter third Octant: "))

       fo = (raw_input(fo))
       if f  == "":
              print fail
              fo = (raw_input("Enter fourth Octant: "))
   except KeyboardInterrupt:
            print '\n'+"Quitting"
            raise SystemExit
   print  "specifyed  ip address "+f+'.'+s+'.'+t+'.'+fo
   time.sleep(0.1)

   try:
      ff = urllib2.urlopen("http://www.iplocationfinder.com/"+f+'.'+s+'.'+t+'.'+fo)
      print bcolors.BOLD+bcolors.CYAN+ "Now fetching your infomation"+bcolors.ENDC
      bar()
      os.system("clear")
      s = str(ff.read())
      ff.close()
      pattern = r'(<.*?>)'
      ff = open('location.txt', 'w')
      ff.write(re.sub(pattern,'',s))
      ff.close()
   except urllib2.HTTPError, e:
        time.sleep(0.1)
        print "This IP does not exist"+'\n'+"Exitting"
        print e
        time.sleep(0.1)
        os.system("clear")
        print "This is the last output information requested"+'\n'+"Since you typed an invalid IP address"







   lip = open('location.txt').readlines()[66],
   for lines in lip:
       print bcolors.UNDERL+bcolors.GREEN + (lines)
   trip = open('location.txt').readlines()[67],
   for lines in trip:
       print (lines)
   rip = open('location.txt').readlines()[68],
   for lines in rip:
       print (lines)

   it = open('location.txt').readlines()[69],
   for lines in it:
       print (lines)

   of = open('location.txt').readlines()[70],
   for lines in of:
       print (lines)
   read = open('location.txt').readlines()[71],
   for lines in read:
       print (lines)
   ancor = open('location.txt').readlines()[72],
   for lines in ancor:
       print (lines)
   teck = open('location.txt').readlines()[73],
   for lines in teck:
       print (lines)
   god = open('location.txt').readlines()[74],
   for lines in god:
       print (lines)
   ip = open('location.txt').readlines()[75],
   for lines in ip:
       print (lines)
   look = open('location.txt').readlines()[77],
   for line in look:
       print (lines)
   hack = open('location.txt').readlines()[78],
   for lines in hack:
##   sick = open('location.txt').readlines()[108],
##   for lines in sick:
##       print (lines)
##   find = open('location.txt').readlines()[109],
##   for lines in find:
##       print (lines)
##   snap = open('location.txt').readlines()[110],
##   for lines in snap:
##       print (lines)
##   tack = open('location.txt').readlines()[112],
##   for lines in tack:
##       print (lines)
##   help = open('location.txt').readlines()[113],
##   for lines in help:
##       print (lines)
##   sex = open('location.txt').readlines()[114],
##   for lines in sex:
##       print (lines)
##   itia = open('location.txt').readlines()[115],
##   for lines in itia:
       print (lines)+ bcolors.ENDC  # Lines can be added if more is needed
       try:
         pause = (raw_input(wait))
         if pause == "Y" or pause == "y":
                   pass
         elif pause == "N" or pause == "n":
                     i = random.randrange(0,2)
                     if i == 0:
                           print "Thank you for using this program"
                           raise SystemExit
                     if i == 1:
                           print "[Even though your winning it dosen't mean you've won]"
                           raise SystemExit
         else:
              print "Thanks for not answering the question i'll exit then"
              raise SystemExit
       except KeyboardInterrupt:
               print "You hit Ctl-C Exitting"
               raise SystemExit


