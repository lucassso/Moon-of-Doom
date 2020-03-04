phealth = 200
import time
input('Read the story CAREFULLY and answer each question with precision. Press enter to continue.\n')
name = input('What\'s your name?\n')
name = name.title().strip(" ")

print('You have just crash landed on the Moon of Doom. Welcome, {}.'.format(name))
print('You start walking forward. All you have is your clothes and a mysterious backpack which seems to hold an infinite supply of objects. At least you wont run out of space. As well as this, the weight of the bag does not change no matter what. Now where will y—- Oh no, a giant monster appeared!')

print('You saw a weapon lying right beside you. You picked it up quickly.')
weapon1 = input ('What weapon was it? \n')
weapon1 = weapon1.lower().strip("a ").replace(' ', '')
print('Ah, yes. The %s.'%weapon1)
print('You stood up and threw the %s mightily at the ugly monster.' %weapon1)
print('The %s exploded on ugly monster, which was actually your reflection in a mirror, destorying it.'% weapon1)
phealth = phealth-1
print('The shards of the mirror flew everywhere. One hit your leg, dealing 1 damage to you. You have '+ str (phealth)+' health left.')


print('You keep walking, clearly embarassed.')
print('')
print('You came across a potato. Because you are starving, you attempt to eat it. As you go to pick up the potato, it sprouts human eyes where its potato eyes previously were.')
weapon2 = input ('You look around, and see a weak point. What do you try to kill it with?\n')
weapon2 = weapon2.strip("a ").strip(" ").lower()
print ('Great! You pull a %s out of your backpack. You try to kill the potato, but fail.'% weapon2)
phealth -= 29
print('This annoys the potato. It secretes acid out of one of its eyes at you. Your finger melted. You now have '+ str (phealth)+' health left.') 
heal = input('What will you use to heal your finger? Quick, you‘re bleeding!\n')
heal = heal.strip(' ').lower()
if heal == "bandages":
  phealth += 30
  print('Good choice. You pull bandages out of your backpack and you regenerate 30 health. You are now at '+ str(phealth)+' health.')
elif heal == 'medicine':
  phealth += 30
  print("Good choice. You grab some medicine out of your backpack and apply it to your wound. You gain 30 health.")
else:
  phealth += 10
  print('Questionable choice. You use it, but it is not as effective as most healing products. You are now at '+str(phealth)+' health.')
print ('You healed your finger. OK, now you need to try and kill the potato.')
weapon3 = input ('What else can you use to kill the potato? There must be something in that backpack you can use!\n')
weapon3 = weapon3.strip("a ").strip(" ").strip("your ").lower()
print('You threw your %s at the potato. Critical hit! The potato now has only one more eye. Wait, that eye is golden!'% weapon3)
print('You look for things in your backpack to kill the golden eye. You see that you can either stab the eye with something sharp, or try to pull out the eye with your hands.')


ans0 = input('will you try and stab the eye, or rip out the eye?\n')
ans0 = ans0.strip(" ").lower()
if ans0 == 'rip out the eye':
  print('')
  print('You decide to pull the eye out. It works! After you pulled the eye out, you realize that the potato is a robot. The golden eye was its source of energy. You decided to keep it in your backpack just in case you need it.')
elif ans0 == 'stab the eye':
  phealth -= 20
  print('You take out your sword and lunge it into the golden eye. It has no effect. The eye is METAL. The potato takes the sword and lunges it into your eye. You now have only '+ str (phealth)+' health. What else could you do...')
  print("")
  print('You decide to pull the eye out. It works! After you pulled the eye out, you realize that the potato is a robot. The golden eye was its source of energy. You decided to keep it in your backpack just in case you need it.')
else:
  phealth -= 50
  print('The potato quickly uses its laser and beams you before you can do anything. You now only have '+ str (phealth)+' health.')
  print('You decide to pull the eye out. It works! After you pulled the eye out, you realize that the potato is a robot. The golden eye was its source of energy. You decided to keep it in your backpack just in case you need it.')

print('')
print('You continue to explore the desolete moon, and you come across a large tent made out of a liquid. What? Strange, you cannot see through the liquid, so you don’t know what is in it.')
tent = input('Would you like to explore the tent?\n')
tent = tent.strip(" ").lower()
if tent == 'yes':
  phealth -= 10
  print('You decide to go inside the tent. You see a bed, a chest, and an empty fridge. You look on the ground and see a skeleton and decide that the previous owner starved to death. You sleep in the tent and wake up, refreshed. You regain 10 health. You are now at '+ str(phealth) +' health. As you leave, your backack brushes against the tent. The liquid that the tent is made out of collapses. Some of that liquid gets into your mouth. Before you have time to react, you swallow it. It was poisonous! You gag in pain and in a short time the effects wear off. You lose 20 health.')
elif tent == 'no':
  phealth -= 15
  print('You just leave it alone. However, while you are walking, you find a bee. You try to step on it, not wanting to deal with it. It quickly stings you and flops on the ground. You are depleted of 15 health. You now have '+ str(phealth) +' health.' )
print('')
print('You keep walking. Your path splits into two paths.')
path = input('Which way will you go, right or left?\n')
if path.strip(" ").lower() == 'right':
  riddle = input('You go right. You see a guard that has a riddle for you. He says, “What is the shape of an egg, has the leaves of a plant, and the thorns of a rose?”\n')
  if riddle.strip(' ').lower == 'pineapple':
    print('”Correct! I clearly see you have the knowledge to proceed.” The guard lets you pass. You keep walking.')
  else:
    phealth -= 30
    print('”Incorrect! I see now that you do not possess enough knowledge.” The guard slashes you with his sword. You are depleted to '+ str(phealth+10) +' health. You quickly pull a grenade out of your bag and throw it at the guard, releasing the pin. You immediately take cover behind a tree. The guard dies. You peek to see if he died. While looking, a grenade fragment hits your cheek. It does not penetrate your skin, but does bruise you. You are now at ' + str(phealth) +' health. You keep walking, careful to not step on his organs. You keep walking.')
    #Continue path to the right here

if path.strip(" ").lower() == 'left':
  phealth -= 5
  print('You walk left, and come across a river. You attempt to swim across it. While you swim, you cut your leg on a jagged rock and the river becomes red. You quickly swim across and lay down on the other side. You now have '+ str(phealth) +' health. Ouch. You bandage up your leg and keep walking.')
else:
  print('After a while, you just walk down the middle of the two paths. I can’t believe I never thought of that. You walk down the path easily, and find a clearing.')
print('Both paths merge into one path again. You keep walking.')
print('')
print('You see a forest approaching. Strange, there seems to be no light shining inside the dark forest. You could use a lantern in your bag to see, right? You pull the lantern out of your bag. You inspect it to find that there are no batteries left.')
light = input('You formulate two options. You could find a power source or walk without light. What will you do?\n')
if light == 'find a power source':
  print('''You think about what could be a power source. Hmm... oh yeah! You swiftly pull out the golden eye. You insert it into the lantern. Then you try to turn the lantern on. Success! ''')
  print('''You start walking through the woods. As you are walking you feel a creature move within the bushes, watching you. After a minute, it goes away.''')
  print('''At the end of the forest, your lantern runs out of energy. You inspect the golden eye. As you look at it, sparks fly off of it. The eye ran out of energy. You realize it serves no more purpose and throw it into the woods.''')
  print('You keep walking.')
  print('')
  print('You see a small tavern coming into view. It is called “The Rusty Tavern”. You decide to walk inside. You walk inside to see an ominous man which seems to be the bartender. He says,“Would you like to spin the wheel? All you need to give me is 3 coins.” You say yes, and pay him. He leads you to a wall. You squint your eyes in confusion. He reaches towards the wall to reveal a hidden doorknob. He opens the door and you follow him inside.')
  print('He reveals a wheel of fortune divided into six parts. One of the parts are red, the rest are white. He says,”If it lands on red, you die. If it lands anywhere else, you get a free drink and you are allowed to spin again for free.')
  bar = input('”Would you like to spin the wheel?”\n')
  if bar == ('no'):
    print('You say no. He hesitates when you gesture for your money back. You reluctanty leave. What a scam.')
  elif bar == ('yes'):
    print('You decide to spin the wheel...')
    print('WHITE')
    phealth += 5
    print('You get a small cup of beer which you drink in one chug. You gain 5 health, from the beer.')
    bar2 = input('”Would you like to spin again?”\n')
    if bar2 == ('no'):
      print('You say no. You leave, feeling a bit tipsy.')
    if bar2 == ('yes'):
      print('You decide to spin the wheel...')
      print('WHITE')
      phealth += 5
      print('You get a small cup of beer which you drink in one chug. You start feeling a bit tipsy, but recieve 5 more health.')
      bar3 = input('”Would you like to spin again?”\n')
      if bar3 == ('no'):
        print('You say no. You leave, feeling drunk.')
      if bar3 == ('yes'):
        print('You decide to spin the wheel...')
        print('WHITE')
        phealth += 5
        print('You drink your beer. Now you know you are drunk. You gain 5 health. You should probably stop playing soon...')
        bar4 = input('“Would you like to spin again?”\n')
        if bar4 == ('no'):
          print('You say no. You leave, feeling satified yet drunk.')
        if bar4 == ('yes'):
          print('You decide to spin the wheel...')
          print('WHITE')
          phealth += 5
          print('You hesitate, but drink the entire beer, spilling a lot along the way. You still get 5 more health. You must be very drunk now.')
          bar5 = input('“Would you like to spin again?”\n')
          if bar5 == ('no'):
            print('You say no. You leave... feeling like you finally made the right choice.')
          if bar5 == ('yes'):
            print('You decide to spin the wheel...')
            print('RED')
            phealth -= 30
            print('Oh no... the bartender slashes you with his sword, with the intent to kill, but only hits you in the ribcage. That slash still does significant damage, about 30 damage. You now have '+ str(phealth) +' health. You play dead anyways. After a minute, he chuckles and throws you into the pile of trash outside the building. As soon as you hear him leave, you run away quickly. You stumble and fall, remebering how drunk you are. He comes outside to see you alive, and running away. Now you have no choice but to fight him. You pull a grenade out of your bag and throw it at him. He just stands there as it explodes. When the dust clears, he is still standing. He must be explosion-proof.')
            phealth -= 20
            print('He stabs you with his sword. You take 20 damage. You struggle to stand, but you get up, and drop your bag. You then remember something. You quickly search you bag for... the golden eye. Then you realize that you already used it. Son of a bi—')
            phealth -= 150 
            print('The bartender slaps you in the face with a rock. You get knocked out. You lose 150 health, and now have '+ str(phealth) +' health.')
            phealth += 100
            print('You wake up in the trash pile again. He must’ve thought you really did die. You quickly tip toe away and continue on your path. You stop at a clearing to heal yourself. You use your Potion Of Healing. Damn, you wish you didn’t need to use it. You wanted to save it for later. But it works and heals you of 100 health. All of your previous injuries also heal, leaving you rejuvenated. You now have '+ str(phealth) +' health.')
else:
  phealth -= 20
  print('You can’t think of any power sources with you. Ok... I’m sure there is nothing in the forest that can hurt you. You start walking. As you near the end, you feel a creature around you. You try to run to the end, but it blocks your path. Where is it... it‘s seems to be a black creature that has two red eyes. You try to attack with your sword, but the creature slashes you with its... claws? Now you have '+ str(phealth) +' health. You swing wildly, and finially spill its blood with your sword as you move on. You make it to the end of the forest without any more trouble.')
  print('You keep walking.')
  print('')
  print('You see a small tavern coming into view. It is called “The Rusty Tavern”. You decide to walk inside. You walk inside to see an ominous man which seems to be the bartender. He says,“Would you like to spin the wheel? All you need to give me is 3 coins.” You say yes, and pay him. He leads you to a wall. You squint your eyes in confusion. He reaches towards the wall to reveal a hidden doorknob. He opens the door and you follow him inside.')
  print('He reveals a wheel of fortune divided into six parts. One of the parts are red, the rest are white. He says,”If it lands on red, you die. If it lands anywhere else, you get a free drink and you are allowed to spin again for free.')
  bar = input('”Would you like to spin the wheel?”\n')
  if bar == ('no'):
    print('You say no. He gives you your money back and you leave.')
  elif bar == ('yes'):
    print('You decide to spin the wheel...')
    print('WHITE')
    phealth += 5
    print('You get a small cup of beer which you drink in one chug. You get 5 health back.')
    bar2 = input('”Would you like to spin again?”\n')
    if bar2 == ('no'):
      print('You say no. You leave, feeling a bit tipsy.')
    if bar2 == ('yes'):
      print('You decide to spin the wheel...')
      print('WHITE')
      phealth += 5
      print('You get a small cup of beer which you drink in one chug. You start feeling a bit tipsy, however you get 5 more health.')
      bar3 = input('”Would you like to spin again?”\n')
      if bar3 == ('no'):
        print('You say no. You leave, feeling drunk.')
      if bar3 == ('yes'):
        print('You decide to spin the wheel...')
        print('WHITE')
        phealth += 5
        print('You drink your beer. Now you know you are drunk. You get 5 more health. You should probably stop playing soon...')
        bar4 = input('“Would you like to spin again?”\n')
        if bar4 == ('no'):
          print('You say no. You leave, feeling satified yet drunk.')
        if bar4 == ('yes'):
          print('You decide to spin the wheel...')
          print('WHITE')
          phealth = phealth + 5
          print('You hesitate, but drink the entire beer, spilling a lot along the way. You still get +5 health... You must be very drunk now.')
          bar5 = input('“Would you like to spin again?”\n')
          if bar5 == ('no'):
            print('You say no. You leave... feeling like you finally made the right choice.')
          if bar5 == ('yes'):
            print('You decide to spin the wheel...')
            print('RED')
            phealth -= 30
            print('Oh no... the bartender slashes you with his sword, with the intent to kill, but only hits you in the ribcage. That slash still does significant damage, about 30 damage. You now have '+ str(phealth) +' health. You play dead anyways. After a minute, he chuckles and throws you into the pile of trash outside the building. As soon as you hear him leave, you run away quickly. You stumble and fall, remebering how drunk you are. He comes outside to see you alive, and running away. Now you have no choice but to fight him. You pull a grenade out of your bag and throw it at him. He just stands there as it explodes. When the dust clears, he is still standing. He must be explosion-proof.')
            phealth += 10
            print('He stabs you with his sword. You take 20 damage. You struggle to stand, but you get up, and drop your bag. Something familiar rolls out. The golden eye! Good thing you didn’t use it, now it would come in handy. Taking a scratch from that black creature was worth it to save you from, most likely, death. You throw it with amazing precision, and it lands in the bartender’s mouth and goes down his throat. He gets electrocuted. While he is stunned, you pull a mace out of your bag and slice off his head. Finally, he is dead. You go to pick up your bag and decide to heal yourself before leaving. You want to use the Potion Of Healing, which gives you an extra 100 health. You go to drink it, but it slips out of your hand and the glass bottle shatters on the ground, spilling its contents intp the grass. The ground area immediately sprouts flowers where the bottle spilled. Wow. You feel upset as you start to walk, but then some of your wounds heal. Some of the potion must’ve splashed onto you and healed you. You now have 30 more health, giving you '+ str(phealth) +' health.')
print('You keep walking.')
print('')
print('You come across a gravestone aside the path you were walking on. You try to read the gravestone, but cannot see the small writing.')
trap = input('Do you move closer to see what it says?\n')
if trap.strip(" ").lower() == "yes":
  print("")
else:
  print("You contemplate about it, but curiosity gets the best of you.")
print('You inch closer to see what it says. As you stand in front of it, you fall into a pit. It was a trap! As you see the ground get closer, you impact it, taking 42069 damage. You die!')
time.sleep(7)
print("""
  
  
""")
print('"Okay %s, you can take off your headset now."'% name)
exit()
