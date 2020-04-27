#!/usr/bin/env python
import os
import random

RED="\e[31m" 
GREEN="\e[32m" 
YELLOW="\e[33m" 
BLUE="\e[34m" 
PURPLE="\e[35m" 
CYAN="\e[36m" 
WHITE="\e[37m" 
colors = ['\033[1;31m', '\033[1;35m']
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
numberer1 = red+"["+yellow+"1"+red+"]"+green
numberer2 = red+"["+yellow+"2"+red+"]"+green
numberer3 = red+"["+yellow+"3"+red+"]"+green
numberer4 = red+"["+yellow+"4"+red+"]"+green
numberer5 = red+"["+yellow+"5"+red+"]"+green
numberer0 = red+"["+yellow+"0"+red+"]"+green
bullets = red+"<"+yellow+" * "+red+">"+green

logo = """
 (                                                                 
 )\ )      )          (    (    (                                  
(()/(   ( /(     (    )\   )\   )\ )       (            (      (   
 /(_))  )\())   ))\  ((_) ((_) (()/(      ))\    (      )\    ))\  
(_))   ((_)\   /((_)  _    _    /(_))_   /((_)   )\ )  ((_)  /((_) 
/ __|  | |(_) (_))   | |  | |  (_)) __| (_))    _(_/(   (_) (_))   
\__ \  | ' \  / -_)  | |  | |    | (_ | / -_)  | ' \))  | | / -_)  
|___/  |_||_| \___|  |_|  |_|     \___| \___|  |_||_|   |_| \___|  
                  
                           """
logo2 = """ShellGenie V1.0 """                                                                    
print(random.choice(colors) + logo +yellow + logo2)
print(yellow)
print(blue+"<===========================================================>")
print(red+"×"+yellow+"                    "+green+"«"+yellow+"ShellGenie"+green+"»                           "+red+"×")
print(red+"×"+yellow+"                "+green+"‹"+yellow+"TERMUX SHELL MODIFIER"+green+"›                   "+red+" ×")
print(red+"×"+yellow+"           Easily Customize your termux shell             "+red+" ×")
print(red+"×"+yellow+"    Author © https://github.com/ShinazBinShajahan/         "+red+"×")
print(blue+"<===========================================================>")
count = 2
while count < 10:
    print("\n\n"+yellow+"Pick an Option"+white+"  :: ")
    print("\n"+numberer1+ "Customize Your Shell")
    print(numberer2+ "Reset your Shell to Default")
    print(numberer3+ "More Tools")
    print(numberer0+ "Exit ShellGenie\n\n")
    choice = input(yellow+"Select an Option"+white+" :: "+yellow)
    if choice == "1" :
        print("\n\n"+red+"***"+yellow+"***"+green+"***"+cyan+"CHOICES"+green+"***"+yellow+"***"+red+"***"+white+"\n")
        print(numberer1+" Simple Mode")
        print(numberer2+" Simple Mode , Coloured")
        print(numberer3+" Simple Header With Advanced PS1")
        print(numberer4+" Coloured Header with Advanced PS1")
        print(numberer5+" Other Shells")
        print(numberer0+" Go to Home Menu\n")
        choiceone = input(yellow+"Enter Your Choice "+white+":: "+yellow)
        if choiceone == "1":
            print("\n")
            bannername = input(bullets+ "Enter Your Header Title :: "+white)
            ps = input(bullets+ "Enter How your PS1 looks like \n ::example : ===> \n  default is $ \n Enter ::")
            if not ps :
                ps = "$"
            sub =input(bullets+ "Enter a Sub-Heading (leave blank for nothing) ::")
            with open("bash.bashrc",'a+') as f:
                f.write("figlet "+bannername)
                f.write("\n echo -e " + sub)
                f.write("\n" +"PS1=\'"+ps+"\'")
                f.close()
                os.system("bash b.sh")
        elif choiceone == "2":
            print("\033[0;32m")
            bannername = input(bullets+ "Enter Your Header Title"+white+" :: "+yellow)
            bannercolor = input(bullets+ "The Available Colours For Header Title are :: \n"+red+"  Red , "+green+"Green , "+blue+"Blue , "+yellow+"Yellow ,"+cyan+" Cyan , "+purple+"Purple  "+green+"\n Enter  your likely Colour"+white+" :: "+yellow)
            bannercolor = bannercolor.lower()
            if bannercolor == "red":
                bcolor = RED
            elif bannercolor == "green" :
                bcolor  = GREEN
            elif bannercolor =="blue":
                bcolor = BLUE
            elif bannercolor == "yellow":
                bcolor = YELLOW
            elif bannercolor == "cyan" :
                bcolor = CYAN
            elif bannercolor == "purple":
                bcolor = PURPLE
            else :
                bcolor = WHITE
            ps = input(bullets+ "Enter Your PS1 style ( Default is "+white+"$ "+green+")  "+white+":: "+yellow)
            if not ps:
                ps = "$"
            pscolor = input(bullets+ "Enter The Colour for your PS1 from the following :: \n"+red+"  Red , "+green+"Green , "+blue+"Blue , "+yellow+"Yellow ,"+cyan+" Cyan , "+purple+"Purple  "+green+"\n Enter  your likely Colour"+white+" :: "+yellow)
            pscolor = pscolor.lower()
            if pscolor == "red":
                psclr = RED
            elif pscolor == "green" :
                psclr  = GREEN
            elif pscolor =="cyan":
                psclr = CYAN
            elif pscolor == "purple":
                psclr = PURPLE
            elif pscolor == "blue" :
                psclr = BLUE
            elif pscolor == "yellow":
                psclr = BLUE
            else :
                psclr = WHITE
            sub = input(bullets+ "Enter your Sub-Heading here , leave blank for nothing :: ") 
            with open("bash.bashrc",'a+') as f:
                f.write("echo -e \""+bcolor+"\"\n figlet "+ bannername)
                f.write("\necho -e \""+YELLOW+"<===============================================>\"")
                f.write("\necho -e \""+RED+"                   "+sub + "\"")
                f.write("\necho -e \"" + YELLOW +"<===============================================>\"")
                f.write("\n" +"PS1=\'"+psclr+ ps +"\'")
                f.close()
                os.system("bash b.sh")
        elif choiceone == "3" :
            print("\033[0;32m")
            bannername = input(bullets+ "Enter Your Header Title :: ")
            sub =input(bullets+ "Enter a Sub-Heading (leave blank for nothing)"+white+" ::" + yellow)
            pstime =input(bullets+ "Do you want to show the current time on your PS1 ? "+yellow+" [ "+green+"Y "+white+"/ "+red+"N"+yellow+" ]"+white+" :: "+yellow)
            pstime = pstime.lower()
            dirchoice = input(bullets+ "Do you want to Show the working directory in your PS1 ? "+yellow+" [ "+green+"Y "+white+"/ "+red+"N"+yellow+" ]"+white+" :: "+yellow)
            dirchoice=dirchoice.lower()
            if dirchoice == "y" :
                print(bullets+ "Do you want to show :: \n "+numberer1+" only the current directory name or \n "+numberer2+" the whole name from the root ? ")
                diryes = input(green+"Enter "+yellow+"["+white+"1"+green+" / "+white+"2"+yellow+"]"+white+" :: "+white)
                if diryes == "1":
                    diryesfinal = "\W"
                else :
                    diryesfinal = "\w"
            else : 
                diryesfinal = ""
            userps = input(bullets+ "Do you want to show your name in your PS1 ? "+yellow+" [ "+green+"Y "+white+"/ "+red+"N"+yellow+" ]"+white+" :: "+yellow)
            userps = userps.lower()
            if userps == "y" :
                usernamefinal = input(bullets+ "Enter your name to be displayed on PS1 :: ")
            else :
                usernamefinal = "localhost"
            if pstime == "y" :
                timeps = "\T"
            else : 
                timeps= ""
            with open("bash.bashrc",'a+') as f:
                f.write("figlet "+bannername)
                f.write("\necho -e \""+YELLOW+"<===============================================>\"")
                f.write("\necho -e \""+RED+"                   "+sub + "\"")
                f.write("\necho -e \"" + YELLOW +"<===============================================>\"")
                f.write("\n" +"PS1='\[\e[31m\]┌─[\[\e[37m\]"+timeps+"\[\e[31m\]]─────\e[0;31m[root\e[1;33m@\e[0;31m["+usernamefinal+"\e[0;31m]\e[0;31m───[\#]\n|\n\e[0;31m└─[\[\e[31m\]\e[0;35m" + diryesfinal + "\[\e[31m\]]>'"+"\""+WHITE+"\"")
                f.close()
                os.system("bash b.sh")
        elif choiceone == "4":
            print("\033[0;32m")
            bannername = input(bullets+ "Enter Your Header Title"+white+" :: "+yellow)
            bannercolor = input(bullets+ "The Available Colours For Header Title are :: \n"+red+"  Red , "+green+"Green , "+blue+"Blue , "+yellow+"Yellow ,"+cyan+" Cyan , "+purple+"Purple  "+green+"\n Enter  your likely Colour"+white+" :: "+yellow)
            bannercolor = bannercolor.lower()
            if bannercolor == "red":
                bcolor = RED
            elif bannercolor == "green" :
                bcolor  = GREEN
            elif bannercolor =="blue":
                bcolor = BLUE
            elif bannercolor == "yellow":
                bcolor = YELLOW
            elif bannercolor == "cyan" :
                bcolor = CYAN
            elif bannercolor == "purple":
                bcolor = PURPLE
            else :
                bcolor = WHITE
            sub =input(bullets+ "Enter a Sub-Heading (leave blank for nothing)"+white+" ::" + yellow)
            pstime =input(bullets+ "Do you want to show the current time on your PS1 ? "+yellow+" [ "+green+"Y "+white+"/ "+red+"N"+yellow+" ]"+white+" :: "+yellow)
            pstime = pstime.lower()
            dirchoice = input(bullets+ "Do you want to Show the working directory in your PS1 ? "+yellow+" [ "+green+"Y "+white+"/ "+red+"N"+yellow+" ]"+white+" :: "+yellow)
            dirchoice=dirchoice.lower()
            if dirchoice == "y" :
                print(bullets+ "Do you want to show :: \n "+numberer1+" only the current directory name or \n "+numberer2+" the whole name from the root ? ")
                diryes = input(green+"Enter "+yellow+"["+white+"1"+green+" / "+white+"2"+yellow+"]"+white+" :: "+white)
                if diryes == "1":
                    diryesfinal = "\W"
                else :
                    diryesfinal = "\w"
            else : 
                diryesfinal = ""
            userps = input(bullets+ "Do you want to show your name in your PS1 ? "+yellow+" [ "+green+"Y "+white+"/ "+red+"N"+yellow+" ]"+white+" :: "+yellow)
            userps = userps.lower()
            if userps == "y" :
                usernamefinal = input(bullets+ "Enter your name to be displayed on PS1 :: ")
            else :
                usernamefinal = "localhost"
            if pstime == "y" :
                timeps = "\T"
            else : 
                timeps= ""
            with open("bash.bashrc",'a+') as f:
                f.write("echo -e \""+bcolor+"\"\n"+"figlet "+bannername)
                f.write("\necho -e \""+YELLOW+"<===============================================>\"")
                f.write("\necho -e \""+RED+"                   "+sub + "\"")
                f.write("\necho -e \"" + YELLOW +"<===============================================>\"")
                f.write("\n" +"PS1='\[\e[31m\]┌─[\[\e[37m\]"+timeps+"\[\e[31m\]]─────\e[0;31m[root\e[1;33m@\e[0;31m["+usernamefinal+"\e[0;31m]\e[0;31m───[\#]\n|\n\e[0;31m└─[\[\e[31m\]\e[0;35m" + diryesfinal + "\[\e[31m\]]>'"+"\""+WHITE+"\"")
                f.close()
                os.system("bash b.sh")
        elif choiceone == "5" :
            print(red+"< "+yellow+"*"+red+" >"+green+"These are Some extra Shells Available (I Donot Own These !)")
            print("\n"+numberer1+ "The Parrot OS Shell")
            print(numberer2+ "Fish Shell")
            print(numberer0+ "Go To Home Menu")
            pass
            pass
            shellchoice = input(yellow+"Pick A Shell"+white+" :: "+yellow)
            if shellchoice == "1":
                os.system("bash data/prt/prt.sh")
            elif shellchoice == "2":
                os.system("bash data/fsh/fsh.sh")
            
                
                    
            
    elif choice == "0":
        print("\033[0;32m")
        os.system("clear")
        print(bullets+ "Thank you for using ShellGenie \n Follow me For more tools \n" , " \033[0;31m" , " Exiting...")
        count = 30
    elif choice == "2":
        os.system("bash data/dflt/dflt.sh")
    elif choice =="3":
        print(bullets+"Find me on github \n" + yellow +"https://github.com/ShinazBinShajahan")
        print(numberer1+red+"SetDoor"+green+"A simple PHP Backdoor Binder")
        setdoor = input(yellow+"Do you want to install SetDoor ?"+white+ "[Y / N ]::")
        setdoor = setdoor.lower()
        if setdoor == "y" :
            os.system("cd $home && git clone https://github.com/ShinazBinShajahan/SetDoor")
            print(green+"Thank you for installing SetDoor")
        else : 
            print("okay , moving back..")
    
