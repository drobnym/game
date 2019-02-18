#Little castle game
#sc-function of room
#r1-room1
#r2-room2
#m1-monster1
#h1-hall1
#h2-hall2
#k-kitchen
#dictionarires - roomsc = {"user input" : "response"} 
r1 = {"go left" : "You enter a room with enemy soldier that instantly charges you!" ,
"go right" : "You enter a small armory. You see armor that looks like yours.",
"take apple" : "Oh no! You touched the poisoned apple and died in horrible pain.",
"status" : "You see an apple on round table and two doors. Doors on the right side are smaller than the ones on your left."}
r2 = {"go left" : "You try to open the door but it's locked. This is not the way!",
"take armor" : "You put on the armor. It fits perfectly!",
"go back" : "You return back to the first room.",
"status1" : "You see very familiar armor and on your left there is a classic wooden door with a key hole.",
"status2" : "You see wooden door"}
m1 = {"go back" : "You return back to the first room",
"go right" : "As you slightly open the door you see crowd of enemy soldiers outside. You close the door.",
"go left" : "You wander into empty kitchen, but there is a glowing freezing wand!",
"go straight" : "Just as you close the door and turn around, you see multiple fireballs rushing towards you! Luckily the wand is in your hand and you destroy the fireballs. As you look around, at the end of the hall you see doors to both of your left and right. Choose wisely ;-)",
"go straight_ww" : "Just as you close the door and turn around, you see multiple fireballs rushing towards you! There is nothing you can do against fire... You burn to death!",
"status" : "You see a slain enemy at your feet. Other than that there is nothing to see in this room. You can go back, right, left, straight. "}
k = {"go back" : "You return to the previous room, where you see your dead enemy.",
"take wand" : "As you grab the wand you feel the power coursing through your veins. Let\'s get out of here this is just an ordinary kitchen.",
"status1" : "You see glowing magical wand, other than that it\' just a normal kitchen. You can only go back to the previous room",
"status2" : "You have the magical wand, what are you still doing in the kitchen?! Go back!"}
h1 = {"go back" : "You are back at the place of your first encounter.",
"go left" : "Feeling strong after last encounter, you open the door on your left just to see room full of hostiles. Before you could do anything multiple arrows pierced through your head.",
"status" : "You see a well lit hall and at the end there are doors to your left and right.",
"go right" : "You enter huge king's room. Guards see you in your armor with a bloody weapon and start running towards you. As kings sees what is happening he stops them and calls you closer."}
h2 = {"goodbye" : "King tells you that he has been watching you and he wants you to wield the power of the wand, you will become one of the strongest wizards ever known! It wasn\'t just a dream!"}
#default start of a game - empty inventory, alive, room1
inv = []
alive = True
current_room = r1
cannotg = "You can\'t go there"
cannoti = "You can\'t take that."
won = "Congratulations! You won the game."
next_pr = "Next project will be similar game but object oriented, with rng, magic and other stuff!"

#function definitions
#instructions only once in the beginning
def instr():
  print("""
  ---------------
  Use only 1 command at a time.
  <go> <straight, back, right, left>
  <take> <item>
  <status>
  ---------------
  
  Welcome to the after party, you just woke up in a castle after a night of heavy drinking...
  You don't even remember your own name let alone the night before.
  You are remembering a dream where you and a king made huge plans together...
  Though, was it just a dream?
  Suddenly you hear a loud and scare sound.
  This is not one of those days where you can lay in bed all day!
  """)
#user input fn, in case of caps, makes list [0,1]
def cmd(raw_command):
  commnd = raw_command.lower().split()
  return commnd
#restart caps function
def gaov(game_over):
  gover = game_over.lower()
  return gover
#default room - room1 function
def room1(command):
  global alive
  global current_room
  try:
    if command[0] == "status":
      inv_str = str(inv)
      r1_stat = r1.get("status")
      print(inv_str + " " + str(r1_stat))
    if command[0] == "take" and command[1] == "apple":
      print("You touched the poisoned apple and died.")
      alive = False
    elif command[0] == "take":
      print(cannoti)
    if command[0] == "go" and command[1] == "left":
      if 'armor' in inv:
        print("Good thing you went to the armory first! After heroic battle you emerge victorious!")
        current_room = m1
      else:
        print("Oh no, you don't have any fighting gear! Angry soldier killed you with a single swing.")
        alive = False
    elif command[0] == "go" and command[1] == "right":
      current_room = r2
      if "armor" not in inv:
        text1 = r1.get("go right")
        print(text1)
      else:
        print("Nothing to see here... Go back!")
    elif command[0] == "go":
      print(cannotg)
  except IndexError:
    print("Enter command!")
#armory - room2 function
def room2(command):
  global alive
  global current_room
  try:
    if command[0] == "status" and "armor" not in inv:
      inv_str = str(inv)
      r2_stat = r2.get("status1")
      print(inv_str + " " + str(r2_stat))
    elif command[0] == "status" and "armor" in inv:
      inv_str = str(inv)
      r2_stat = r2.get("status2")
      print(inv_str + " " + str(r2_stat))
    if command[0] == "take" and command[1] == "armor" and "armor" not in inv:
      inv.append("armor")
      r2g = r2.get("take armor")
      print(r2g)
    elif command[0] == "take":
      print(cannoti)
    if command[0] == "go" and command[1] == "left":
      print("Door is locked. This is not the way!")
    elif command[0] == "go" and command[1] == "back":
      text2 = r2.get("go back")
      print(text2)
      current_room = r1
    elif command[0] == "go":
      print(cannotg)
  except IndexError:
    print("Enter command!")
#first encounter - monster1
def monster1(command):
  global alive
  global current_room
  try:
    if command[0] == "status":
      inv_str = str(inv)
      m1_stat = m1.get("status")
      print(inv_str + " " + str(m1_stat))
    elif command[0] == "take":
      print(cannoti)
    if command[0] == "go" and command[1] == "left":
      if "wand" not in inv:
        text = m1.get("go left")
        print(text)
        current_room = k
      else:
        print("Doors are suddenly locked")
    elif command[0] == "go" and command[1] == "right":
      text3 = m1.get("go right")
      print(text3)
    elif command[0] == "go" and command[1] == "straight":
      current_room = h1
      if "wand" in inv:
        text4 = m1.get("go straight")
        print(text4)
      else:
        text5 = m1.get("go straight_ww")
        print(text5)
        alive = False
    elif command[0] == "go" and command[1] == "back":
      text6 = m1.get("go back")
      print(text6)
      current_room = r1
    elif command[0] == "go":
      print(cannotg)
  except IndexError:
    print("Enter command!")
#kitchen - kitchen function
def kitchen(command):
  global alive
  global current_room
  try:
    if command[0] == "status" and "wand" not in inv:
      inv_str = str(inv)
      k_stat = k.get("status1")
      print(inv_str + " " + str(k_stat))
    if command[0] == "status" and "wand" in inv:
      inv_str = str(inv)
      k_stat2 = k.get("status2")
      print(inv_str + " " + str(k_stat2))
    if command[0] == "take" and command[1] == "wand" and "wand" not in inv:
      inv.append("wand")
      print(k.get("take wand"))
      k.pop("take wand", "You already have it!")
    elif command[0] == "take":
      print(cannoti)
    elif command[0] == "go" and command[1] == "back":
      text7 = k.get("go back")
      print(text7)
      current_room = m1
    elif command[0] == "go":
      print(cannotg)
  except IndexError:
    print("Enter command!")
#first hall - hall1 function
def hall1(command):
  global alive
  global current_room
  try:
    if command[0] == "status":
      inv_str = str(inv)
      h1_stat = h1.get("status")
      print(inv_str + " " + str(h1_stat))
    if command[0] == "go" and command[1] == "left":
      gg = h1.get("go left")
      print(gg)
      alive = False
    elif command[0] == "go" and command[1] == "right":
      current_room = h2
      text8 = h1.get("go right")
      print(text8)
    elif command[0] == "go" and command[1] == "back":
      text9 = k.get("go back")
      print(text9)
      current_room = m1
    elif command[0] == "go":
      print(cannotg)
  except IndexError:
    print("Enter command!")
#final hall - hall2 function
def hall2(command):
  last = h2.get("goodbye")
  print(last)
  print(won)
  print(next_pr)
  
#program start
#instructions for use
instr()
#infinite loop for asking for user input while staying alive
while alive == True:
  raw_command = input("What do you want to do?")
  
  
  command = cmd(raw_command)
  
  if current_room == r1:
    room1(command)
  elif current_room == r2:
    room2(command)
  elif current_room == m1:
    monster1(command)
  elif current_room == k:
    kitchen(command)
  elif current_room == h1:
    hall1(command)
  if current_room == h2:
    hall2(command)
    break
#infinite loop breaks once user dies, if user inputs "yes" game restarts
  if alive == False: 
    game_over = input("GAME OVER! Do you want to start again?")
    gover = gaov(game_over)
    if gover == 'yes':
      current_room = r1
      alive = True
      inv = []
#Thank you if you got through here :-) Even though I know it could have been done way better I will appreciate any constructive feedback, feel free to send me one at drobny.mat@gmail.com 