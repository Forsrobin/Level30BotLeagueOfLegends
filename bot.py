import os
from os import path

def startMenu():
  print("""\033[1;31;40m
  ___                     ________  ________  __________   
  |\  \                   |\   __  \|\   __  \|\___   ___\ 
  \ \  \      ____________\ \  \|\ /\ \  \|\  \|___ \  \_| 
   \ \  \    |\____________\ \   __  \ \  \ \  \   \ \  \  
    \ \  \___\|____________|\ \  \|\  \ \  \_\  \   \ \  \ 
     \ \_______\             \ \_______\ \_______\   \ \__\ 
      \|_______|              \|_______|\|_______|    \|__|
  \033[0;37;40m                                                 
  """)
  print("-= League Of Legends bor created by \033[1;33;40mforsrobin\033[0;37;40m and \033[1;33;40mfrowly\033[0;37;40m =- \n")

def menu():
  print("[1] - Start bot")
  print("[2] - Setup bot")
  print("[3] - Buy bot")
  print("[0] - Exit")



def startBot():
  #Check if bot config exsists
  if not path.exists("settings/bot.conf"):
    os.system('cls||clear')
    print("Path does not exsist, please setup your bot first\n")
    return

  #If config exsists read in all values

def main():
  os.system('cls||clear')
  startMenu()

  endBot = True

  while endBot:
    menu()
    choice = int(input())

    if choice == 1:
      startBot()
    elif choice == 0:
      endBot = False
      print("See you soon! c:")


if __name__ == "__main__":
    main()