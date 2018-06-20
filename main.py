#!/usr/bin/python
import csv
import os
import numpy as nrand

def game():
    
    gloop = 1

    while gloop != 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        title, des, exits, npc, zone, lvl = getroom()
        print " "
        print "Location: " + title
        print " "
        print des
        oexit = exits.split("|")
        i = 0
        ex = ""
        while i <= 3:
            if oexit[i] == "n":
                ex = ex + "North "                
                i += 1
            elif oexit[i] == "e":
                ex = ex + "East "
                i += 1
            elif oexit[i] == "s":
                ex = ex + "South "
                i += 1
            elif oexit[i] == "w":
                ex = ex + "West "
                i += 1
            elif oexit[i] == "0":
                i += 1
            else:
                ex = ex + "None"
        print " "
        print "The obvious exit(s) are: " + ex
        print " "
        if npc != "0":
            print npc + " Is in the area."
        else:
            print "There is no one around."
        print " "
        
        if "pve" in zone:
            print "Something attacks!"
            combat(lvl)
        else:
            command = raw_input("What would you like to do?: ").lower()
            if "go" in command:
                if "north" in command:
                    if "North" in ex:
                        room[1] -= 1
                    else:
                        print "No exit that direction!"
                        raw_input("Press enter to continue....")
                elif "east" in command:
                    if "East" in ex:
                        room[0] += 1
                    else:
                        print "No exit that direction!"
                        raw_input("Press enter to continue....")
                elif "south" in command:
                    if "South" in ex:
                        room[1] += 1
                    else:
                        print "No exit that direction!"
                        raw_input("Press enter to continue....")
                elif "west" in command:
                    if "West" in ex:
                        room[0] -= 1
                    else:
                        print "No exit that direction!"
                        raw_input("Press enter to continue....")
                else:
                    print "Invalid Direction."
            elif "/c" in command:
                csheet()
                raw_input("Press Enter to Return...")
            elif "/i" in command:
                inv()
                raw_input("Press Enter to Return...")
            else:
                print "Invalid Command"
         





    return;

def start_game():

    print "Cyberwar 2120"
    print "(N)ew Game"
    print "(L)oad Game"
    print "(Q)uit Game"
    game = raw_input("> ").lower()

    if game == "n":
        new_game()
    elif game == "l":
        exit
    elif game == "q":
        exit


    return;

def new_game():


    char_setup()
    game()

    return;

def char_setup():
    print "Hello. Welcome to Cyber War 2120. You are about to enter a cyber-punk style future where you can create your own destiny."
    global room
    room = [1, 1]
    global credit
    credit = 50
    global hp
    hp = 0
    global chp
    chp = 0
    global slots
    slots = 0
    global armor
    armor = 0
    global cname
    cname = raw_input('Please enter your character name: ')
    global csex
    csex = raw_input('Are you a (m)ale or (f)emale: ').lower()
    if csex == "m":
        csex = "Male"
    elif csex == "f":
        csex = "Female"
    global cstr
    cstr = 10
    global cdex
    cdex = 10
    global ccon
    ccon = 10 
    global ccha
    ccha = 10
    global cint
    cint = 10
    global cwis
    cwis = 10
    global atk
    atk = 1
    end = 1

    while end != 0:
        print " "
        print "Excellent " + cname + " now you must select your class."
        print "To hear more about the class, just type help classes"
        print "-------------------------------------------------------"
        print "Hacker"
        print "NetMind"
        print "Runner"
        print "Cybernetic"
        print "Warlord"
        print "======================================================="
        global cclass
        cclass = raw_input('Enter the class you would like: ').lower()
        print " "

        if "help" in cclass:
            help()
        else:
            end = 0

    print "So " + cname + " you are a " + cclass

    if cclass == "hacker":
        cclass = "Hacker"
        cstr += 0
        ccon += 2
        hp = ccon + 10
        chp = hp  
        cdex += 1
        cint += 5
        cwis += 3
        ccha += 4
    elif cclass == "netmind":
        cclass = "Netmind"
        cstr += 0
        ccon += 2 
        hp = ccon + 10 
        chp = hp  
        cdex += 0
        cint += 3
        cwis += 5
        ccha += 5   
    elif cclass == "runner":
        cclass = "Runner"
        cstr += 2
        ccon += 3 
        hp = ccon + 10 
        chp = hp  
        cdex += 5
        cint += 0
        cwis += 2
        ccha += 3
    elif cclass == "cybernetic":
        cclass = "Cybernetic"
        cstr += 5
        ccon += 5 
        hp += (ccon + 10)
        chp = hp  
        cdex += 0
        cint += 2
        cwis += 2
        ccha += 1
    elif cclass == "warlord": 
        cclass = "Warlord"
        cstr += 4
        ccon += 3 
        hp = ccon + 10 
        chp = hp  
        cdex += 0
        cint += 1
        cwis += 2
        ccha += 5

    print "Here is your character sheet. To see your character sheet just type, /c "
    csheet()
    raw_input("Press enter to continue....")

    return;

def csheet():
    os.system('cls' if os.name == 'nt' else 'clear')
    print " "
    print "--Character Sheet--"
    print "Name:  " + cname
    print "Sex:   " + csex
    print "Class: " + cclass
    print "HP:    " + str(chp) + "/" + str(hp)
    print "--------Stats--------"
    print "Strength:     " + str(cstr)
    print "Constitution: " + str(ccon)
    print "Dexterity:    " + str(cdex)
    print "Intelligence: " + str(cint)
    print "Wisdom:       " + str(cwis)
    print "Charisma:     " + str(ccha)
    print " "


    return;

def inv():

    os.system('cls' if os.name == 'nt' else 'clear')
    print "-------Inventory-------"
    print "======================="
    print "Credits: " + str(credit)
    print "-------Equipped-------"
    with open('./player_data/inv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if "y" == row['equip'] and "head" == row['pos']:
                print "Head:  " + row['title']
    with open('./player_data/inv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if "y" == row['equip'] and "body" == row['pos']:
                print "Body:  " + row['title']
    with open('./player_data/inv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if "y" == row['equip'] and "back" == row['pos']:
                print "Back:  " + row['title']             
    with open('./player_data/inv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if "y" == row['equip'] and "hand" == row['pos']:
                print "Hands: " + row['title']
    with open('./player_data/inv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if "y" == row['equip'] and "legs" == row['pos']:
                print "Legs:  " + row['title']  
    print "----------------------"
    print "-------Backpack-------"
    with open('./player_data/inv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if "y" == row['pack']:
                print row['title']
    print " "  

    return;

def combat(lvl):
    ename = ""
    ehp = ""
    ehpmax = ""
    eatk = ""
    eac = ""
    print "------Combat------"
    with open('./db/enemies.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rnd = 1 #numpy.random.rand(10)
            if rnd == row['id']:
                ename = row['name']
                ehp = row['hp']
                ehpmax = ehp
                eatk = row['dmg']
                eac = row['ac']
    fightloop = 1
    turn = 1
    chpmax = chp
    while fightloop != 0:            
        print "Enemy: " + str(ename)
        print "HP:    " + str(ehp) + "/" + str(ehpmax)
        print "---------------------"
        print "Your HP: " + str(chp) + "/" + str(chpmax)
        if turn == 1:
            command = raw_input("What do you want to do?: ")
            if "attack" in command:
                dmg = numpy.random.rand(atk)
                print "You strike " + str(ename) + " causing " + str(dmg) + " damage!"
            turn = 0
        else:
            edmg = numpy.random.rand(eatk)
            print str(ename) + " strikes you for " + str(edmg) + " damage!"



    return;

def help():

    if "hacker" in cclass:
        print "Hacker"
        print "The Hacker can get information from terminals, take control of mechs and many more. They mainly rely on sabatoge and stealth."
    elif "netmind" in cclass:
        print "Net Mind"
        print "A group of people who have surrendered their mind to the collective. A vast group of users linked directly to each others brains. They use their hive mind to gain information on targets and help their allies win."
    elif "runner" in cclass:
        print "Runner"
        print "A person who runs physical information or data to others. They are often contracted to smuggle secure information into locations not accessible by the network. They rely on their agility above all else."
    elif "cybernetic" in cclass:
        print "Cybernetic"
        print "A person who longs to shed their mortal coil and ascend into that of a machine. They use cybernetics to enhance every part of their being they can."
    elif "warlord" in cclass:
        print "Warlord"
        print "A common criminal who has risen through the ranks and become the Warlord. Specializing in all manner of weapons and ruthlessnes. They are a force to be reconned with."
    else:
        print "Invalid response"

    print " "
    raw_input('Press enter to begin game....')
    return;

def getroom():

    #get_room = room.split("|")
    title = ""
    des = ""
    exits = ""
    npc = ""
    zone = ""
    lvl = ""

    with open('./db/world.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if str(room[0]) == row['x'] and str(room[1]) == row['y']:
                #print(row['x'], row['y'], row['title'], row['desc'], row['exits'], row['npc'])
                title = row['title']
                des = row['desc']
                exits = row['exits']
                npc = row['npc']
                zone = row['zone']
                lvl = row['lvl']
                #print title + des + exits + npc

            


    return title, des, exits, npc, zone, lvl;

start_game()

