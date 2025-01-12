title = " /$$$$$$$                        /$$            /$$$$$$\n| $$__  $$                      | $$           /$$__  $$\n| $$  \ $$  /$$$$$$   /$$$$$$  /$$$$$$        | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$\n| $$$$$$$  /$$__  $$ |____  $$|_  $$_/        | $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$\n| $$__  $$| $$  \ $$  /$$$$$$$  | $$          | $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$\n| $$  \ $$| $$  | $$ /$$__  $$  | $$ /$$      | $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/\n| $$$$$$$/|  $$$$$$/|  $$$$$$$  |  $$$$/      |  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$\n|_______/  \______/  \_______/   \___/         \______/  \_______/|__/ |__/ |__/ \_______/\n\n"

#For delays and timers
import time

#For clearing the terminal
import os
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#Types sentences out
import sys
def slowtype(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./20)

#These are to stop you from choosing the same option twice later on
gback = False
resupply = False
riddlew = False

#Menu & intro
def intro():
  print(title)
  print("Would you like to begin? (Y/N)")
  answer = input("")

  #No Answer
  if answer in ["n", "N", "No", "no"]:
    print(":(")
    exit()

  #Yes Answer
  elif answer in ["y", "Y", "Yes", "yes"]:
    time.sleep(0.5)
    print("\nPlease enter your name: ")
    global name
    name = input ("")

    #Timer
    countdown = 3
    print(f"\nWelcome {name}, your game starts in")
    while countdown > -1:
      time.sleep(1)
      print (countdown)
      countdown = countdown - 1
    clear()

  #Wrong Answer
  else:
    print("Invalid Answer\n")
    time.sleep(0.5)
    intro()

  #Intro Scene
  slowtype("*sunrise*\n")
  time.sleep(0.5)
  slowtype(f"Abdelkader: Captain {name}! We cannot find our map!!!! How will we get to Cyprus now!!!\n")
  time.sleep(1)
  slowtype(f"{name}: What was our final position?\n")
  time.sleep(1)
  slowtype(f"Abdelkader: Somewhere in the Eastern Mediterranean, but we do not know precisely.\n\n")
  compass()



#----------------------------------------------------------#
#                    Choosing A Direction                  #
#----------------------------------------------------------#


#Choose a direction
def compass():
  time.sleep(1.5)
  print("|-Which direction would you like to sail?-|\n1) North 2) South 3) East 4) West")
  global direction
  direction = input("")

  #North answer
  if direction in ["north", "North", "N", "n", "1"]:
    north()

  #South answer
  elif direction in ["south", "South", "S", "s", "2"]:
    if riddlew == True:
      print("You have already went this direction!!!\n")
      compass()
    else:
      south()

  #East answer
  elif direction in ["east", "East", "E", "e", "3"]:
    if resupply == True:
      print("You have already went this direction!!!\n")
      compass()
    else:
      east()

  #West answer
  elif direction in ["west", "West", "W", "w", "4"]:
    if gback == True:
      print("You have already went this direction!!!\n")
      compass()
    else:
      west()

  #Invalid answer
  else:
    print ("Invalid Answer")
    compass()




#----------------------------------------------------------#
#                      North Storyline                     #
#----------------------------------------------------------#


#Go North
def north():
  slowtype (f"\n{name}: Send us north\n")
  time.sleep(1)
  slowtype ("Abdelkader: Will do Captain\n")
  time.sleep(3)
  clear()
  slowtype (f"Abdelkader: {name}! There is a land mass to our east, should we head to it?\n")
  turn()

def turn():
  time.sleep(1)
  print("\n\n|-Go east?-|\n 1) Yes 2) No")
  a = input("")
  
  #Go east
  if a in ["y", "Y", "Yes", "yes", "1"]:
    time.sleep(1)
    slowtype (f"\n{name}: I don't see why not")
    time.sleep(1)
    slowtype ("\nAbdelkader: Alright Captain")
    time.sleep(3)
    clear()
    cyprus()
  
  #Continue north
  elif a in ["n", "N", "No", "no", "2"]:
    time.sleep(1)
    slowtype (f"\n{name}: No, keep us on our path\n")
    time.sleep(1)
    slowtype ("Abdelkader: No problem Captain\n")
    time.sleep(3)
    clear()
    turkey()

  #Invalid Answer
  else:
    print("Invalid Answer\n")
    time.sleep(0.5)
    turn()

def cyprus():
  slowtype ("*As you approach the land mass you hear shots being fired... they are being fired at you*\n")
  time.sleep(1)
  slowtype (f"Faizal: {name}!! What will we do!!\n")
  time.sleep(2)
  gback2()

def gback2():
  print ("\n\n|-What will you do?-|\n1) Turn back 2) Improvise")
  answ = input("")

  if answ == "1":
    time.sleep(1)
    slowtype (f"\n{name}: Send us back Abdelkader, and prepare the escape ships Faizal\n")
    time.sleep(1)
    slowtype (f"Abdelkader & Faizal: Ok captain\n")
    time.sleep(3)
    clear()
    
    slowtype ("\n*The ship is hit, it catches on fire and quickly starts to sink*\n")
    time.sleep(0.5)
    slowtype (f"Faizal: AAAAAAAAAAAAAAA\n")
    time.sleep(2)
    slowtype ("*You and all the crew members are killed*\n")
    time.sleep(3)
    print ("\n\nEpic Fail Ending")
    time.sleep(3)
    exit()
  
  elif answ == "2":
    time.sleep(1)
    slowtype (f"\n{name}: Abdelkader, begin evasive maneuvers")
    slowtype ("Faizal, write a letter saying we come in peace, seal it in a bottle, and throw it to them\n")
    time.sleep(1)
    slowtype ("Faizal: Alright captain\n")
    slowtype ("Abdelkader: Got it")
    time.sleep(3)
    clear()

    slowtype ("*The shots stop and it now feels very quiet, you dock the ship and begin to disembark*\n")
    time.sleep(2)
    slowtype ("Marco: My apologies for what has happened,\nwe have received intel of a coming invasion so we are on full alert\n")
    time.sleep(1)
    slowtype (f"{name}: Dont stress it, we are all alive\n")
    time.sleep(1)
    slowtype ("Marco: Since you have a ship and crew, if you don't mind....")
    time.sleep(0.5)
    slowtype("We could use some help defending\n")
    time.sleep(1)
    slowtype (f"{name}: But we just arrived! I will consider it but I may need some time")
    time.sleep(3)
    clear()
    defend()

  #Invalid Answer
  else:
    time.sleep(1)
    print("Invalid Answer\n")
    time.sleep(0.5)
    gback2()


def defend():
  print ("|-Will you help Marco defend the island-|\n1) Yes 2) No")
  a = input("")
  
  if a in ["y", "Y", "Yes", "yes", "1"]:
    time.sleep(1)
    slowtype (f"\n\n{name}: We have decided it is best we help you\n")
    time.sleep(1)
    slowtype ("Marco: Thank you so much!!! The battle is said to start tomorrow so be prepared\n")
    time.sleep(1)
    slowtype (f"{name}: Ok sir")
    time.sleep(3)
    clear()

    slowtype ("*You help fight the war, you and your crewmates help defend the island and are promoted to high military ranks*")
    time.sleep(1)
    print ("\n\n\nTide Shifter Ending")
    time.sleep(3)
    exit()
  
  #Dont sell the boat, go back to sea
  elif a in ["n", "N", "No", "no", "2"]:
    time.sleep(1)
    slowtype (f"\n\n{name}: We would really like to help... but we have business to do and we must effectively use our time\n")
    time.sleep(1)
    slowtype ("Marco: I understand, we wish you guys the best of luck\n")
    time.sleep(1)
    slowtype (f"{name}: Thank you for everything\n")
    time.sleep(3)
    clear()

    slowtype ("*You finish your business quickly and leave the island, a few days later you hear that they lost the war*")
    time.sleep(1)
    print ("\n\n\nMind Your Own Business Ending")
    time.sleep(3)
    exit()

  #Invalid Answer
  else:
    print("Invalid Answer\n")
    time.sleep(0.5)
    defend()




def turkey():
  slowtype ("*You continue sailing until you reach Antalya, you notice many ships lined up on the doc*\n")
  time.sleep(2)
  slowtype (f"\n{name}: What's going on here?\n")
  time.sleep(1)
  slowtype ("Mustafa: We are preparing for an invasion on Cyprus, would you care to join us?.. You will be rewarded generously\n")
  time.sleep(1)
  slowtype (f"{name}: But we just arrived! I will consider it but I may need some time\n")
  time.sleep(1)
  slowtype ("Mustafa: No problem, we have time\n")
  time.sleep(3)
  clear()
  invade()

def invade():
  print ("|-Will you join the invasion-|\n1) Yes 2) No")
  a = input("")

  if a in ["y", "Y", "Yes", "yes", "1"]:
    time.sleep(1)
    slowtype (f"\n{name}: We have decided we will join you\n")
    time.sleep(1)
    slowtype ("Mustafa: Wonderful!\n")
    time.sleep(3)
    clear()

    slowtype ("*The invasion is successful, you and your crew are rewarded and given government ranks for your efforts*")
    time.sleep(0.5)
    print("\n\nOttoman Ending")
    time.sleep(3)
    exit()


  elif a in ["n", "N", "No", "no", "2"]:
    time.sleep(1)
    slowtype (f"\n{name}: We have decided that it is best we don not join, as we have business to attend to\n")
    time.sleep(1)
    slowtype ("Mustafa: No problem, but I would recommend that you guys leave soon to avoid getting caught in the crossfire.\n")
    time.sleep(1)
    slowtype (f"{name}: Alright sir, thanks for everything\n")
    time.sleep(3)
    clear()

    slowtype ("*The invasion is successful, you and your crew are rewarded and given government ranks for your efforts*")
    time.sleep(0.5)
    print("\n\nOttoman Ending")

    slowtype ("*You leave the island peacefully*\n")
    time.sleep(1)
    slowtype ("Faizal: What is that above us!!\n")
    time.sleep(1)
    slowtype ("*A bright green light illuminates your surroundings, you don't wake up again*\n")
    time.sleep(0.5)
    print ("\n\nAbducted By Aliens Ending")
    time.sleep(3)
    exit()

  else:
    print("Invalid Answer\n")
    time.sleep(0.5)
    invade()



#----------------------------------------------------------#
#                      South Storyline                     #
#----------------------------------------------------------#


#Go South
def south():
  slowtype (f"\n{name}: Let us head south\n")
  time.sleep(1)
  slowtype ("Abdelkader: Say less fam\n")
  time.sleep(3)
  clear()
  egypt()

#Get a little trolled
def egypt():
  time.sleep(2)
  slowtype ("*As you approach Alexandria you see some locals by the shore, they kindly welcome you*\n")
  time.sleep(1)
  slowtype ("*The local leader emerges from the crowd, an older man with thick facial hair and a fez on his head*\n")
  time.sleep(0.5)
  slowtype (f"\nRamadan: Welcome {name}, its so nice to meet you\n")
  time.sleep(1)
  slowtype (f"{name}: Likewise\n")
  time.sleep(3)
  slowtype ("\n*Those were your final memories as you wake up in a nice garden,\nunfortunately your hands are tied and your crew is nowhere to be found*")
  time.sleep(3)
  clear()
  

  time.sleep(1)
  slowtype (f"{name}: What do you want from me\n")
  time.sleep(1)
  slowtype ("Ramadan: As you might know, you have entered this city illegally")
  time.sleep(0.5)
  slowtype ("Ramadan: That being said, I believe you had no bad intention so I will cut you a deal,\nsolve my riddle and I will let you go, but if you answer wrong we will keep your boat.")
  time.sleep(2)
  slowtype (f"\n{name}: ...I take the offer")
  time.sleep(3)
  riddle()

#riddle
def riddle():
  slowtype ("\n\n|-I am tall when I'm young, and short when I'm old, what am I-|\n1) Lebron James\n2) A candle\n3) Former US President Barack Obama\n4) A house\n5) Something that is tall when it's young and short when it's old")
  ans = input("")
  global riddlew

  if ans == "2":
    time.sleep(1)
    slowtype ("\nRamadan: right on...\nit was a pleasure meeting you and I wish you the best of luck on your journey")
    time.sleep(1)
    slowtype (f"\n{name}: Thank you sir")
    time.sleep(0.5)
    slowtype ("\n*You head back to the sea*")
    time.sleep(0.5)
    print ("\n\nRiddle Master achievement")
    time.sleep(3)
    riddlew = True
    clear()
    compass()
  
  elif ans == "5":
    time.sleep(1)
    slowtype ("\nRamadan: hahahahaha, because of your sense of humour I will let you go, I wish the best for you")
    time.sleep(1)
    slowtype (f"\n{name}: Thank you for everything sir")
    time.sleep(0.5)
    slowtype ("\n*You head back to the sea*")
    time.sleep(0.5)
    print ("\n\n200iq Achievement")
    print ("Certified Funny Guy Achievement")
    time.sleep(3)
    riddlew = True
    clear()
    compass()

  else:
    time.sleep(1)
    slowtype ("Ramadan: damn, I really thought you would get it, looks like you are stuck in this country forever")
    time.sleep(0.5)
    print ("\n\nMasri Ending")
    time.sleep(3)
    exit()



#----------------------------------------------------------#
#                       East Storyline                     #
#----------------------------------------------------------#


#Go East
def east():
  slowtype (f"\n{name}: Sail us in the direction of the sun\n")
  time.sleep(1)
  slowtype ("Abdelkader: Ok Captain")
  time.sleep(3)
  clear()
  palestine()

#Land and talk to people
def palestine():
  time.sleep(1)
  slowtype ("*You land in Palestine safely, there is no one around\nso walk along the nearest road towards the city*\n")
  time.sleep(1)
  slowtype ("*You reach a small, lower income village, you begin striking conversation with the locals*\n\n\n")
  time.sleep(2)
  slowtype(f"{name}: Yea, we are coming from Algeria and are on our way to Cyprus\n")
  time.sleep(1)
  slowtype("Ahmad: Wow... You must have a big ship to carry this crew in\n")
  time.sleep(1)
  slowtype(f"Abdelkader & Faizal & {name}: Of course hahaha\n")
  time.sleep(1)
  slowtype("Saad: Would you care to join our crew? We can use someone like yourself... and you can make some money along the way\n")
  time.sleep(1)
  slowtype("Ahmed: Alhamdulillah I have been blessed with wealth, but I have been looking for a ship for exporting my goods, would you take my offer of 10,000 gold pieces for each of you\n")
  time.sleep(1)
  slowtype(f"{name}: That offer doesn't sound to bad\n")
  time.sleep(3)
  clear()
  sell()

#Will you sell the boat?
def sell():
  global resupply
  time.sleep(1)
  print("\n\n|-Will you take the merchants offer-|\n 1) Yes 2) No")
  a = input("")
  
  #Sell boat
  if a in ["y", "Y", "Yes", "yes", "1"]:
    time.sleep(1)
    slowtype (f"\n{name}: ... We will take it")
    time.sleep(1)
    slowtype ("\nAhmed: Wonderful, come with me to my house so we can seal the deal")
    time.sleep(3)
    slowtype("\n\n\n*The deal goes through and your crew becomes rich, you spend the rest of your lives living comfortably*")
    time.sleep(0.5)
    print("\n\n*Falastini Ending*")
    time.sleep(3)
    exit()
  
  #Dont sell the boat, go back to sea
  elif a in ["n", "N", "No", "no", "2"]:
    time.sleep(1)
    slowtype (f"\n{name}: Unfortunately we can not take it as we must complete our trip\n")
    time.sleep(1)
    slowtype ("Ahmad: I understand, it was really nice meeting you\n")
    time.sleep(1)
    slowtype (f"{name}: Thank you for everything\n")
    time.sleep(0.5)
    slowtype ("\n\n\n*You head back to the sea*")
    time.sleep(0.5)
    print ("\n\nYou could've been rich smh achievement")
    time.sleep(3)

    resupply = True
    clear()
    compass()

  #Invalid Answer
  else:
    print("Invalid Answer\n")
    time.sleep(0.5)
    sell()



#----------------------------------------------------------#
#                       West Storyline                     #
#----------------------------------------------------------#


#Go West
def west():
  slowtype (f"\n{name}: We shall head west\n")
  time.sleep(1)
  slowtype ("Abdelkader: Sounds good captain\n")
  time.sleep(3)
  clear()
  back()

#Go back?
def back():
  time.sleep(1)
  slowtype ("\n*The ocean is mysteriously quiet, something tells you to turn back*\n\n")
  time.sleep(0.5)
  print ("|-Will you do it-|\n1) Yes 2) No")
  global gback
  gback = input("")

  if gback in ["y", "Y", "Yes", "yes", "1"]:
    slowtype(f"\n{name}: Forget what I said Abdelkader, turn the ship around")
    gback = True
    compass()

  elif gback in ["n", "N", "No", "no", "2"]:
    time.sleep(0.25)
    slowtype("\n*You continue west*\n")
    shipwreck()

  else:
    time.sleep(0.25)
    slowtype("Invalid Answer")
  back()

#Shipwreck Endings
def shipwreck():
  time.sleep(3)
  slowtype("Faizal: Captain!! It seems we have hit a rock!!! We must evacuate quickly!!!\n\n")
  time.sleep(0.25)
  slowtype("|-Faizal hands you the key to your personal ship-|\n1) Get in your ship and save yourself \n2) Return the key to him and tell him to save others")
  wreck = input("")

  #First Wreck Ending
  if wreck == "1":
    time.sleep(0.25)
    slowtype(f"\n{name}: Thank you Faizal\n*you rush to your personal boat*")
    slowtype("\n*While rowing you make a wrong turn and are stranded in shark infested waters, you are stuck there until you inevitably starve to death, you regret being selfish & wish you helped your Crewmates to safety*")
    time.sleep(0.5)
    print("\n\nCoward Ending")
    time.sleep(3)
    exit()

  #Second Wreck Ending
  elif wreck == "2":
    time.sleep(0.25)
    slowtype(f"\n{name}: Get the others to safety, dont worry about me\n*you hand him back the key*")
    time.sleep(0.25)
    slowtype(f"\nFaizal: Thank you for everything Captain {name}, you will not be forgotten")
    time.sleep(0.5)
    slowtype(f"\n{name}: Dont worry, we will see each other soon enough")
    time.sleep(1)
    slowtype("*The ship drowns with you in it, your crewmates make it to the Greek island of Crete safely, & you are remembered as the best Captain in history*")
    time.sleep(0.5)
    print("\n\nSelfless Ending")
    time.sleep(3)
    exit()


intro()
