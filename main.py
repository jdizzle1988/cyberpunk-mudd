#!/usr/bin/python
import csv

def game():
    
    gloop = 1

    while gloop != 0:

        title, des, exits, npc = getroom()
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
        print npc + " Is in the area."
        print " "
        command = raw_input("What would you like to do?: ").lower()

        if "go" in command:
            if "south" in command:
                room[1] += 1
        





    return;

def new_game():


    char_setup()
    game()

    return;

def char_setup():
    print "Hello. Welcome to Cyber War 2120. You are about to enter a cyber-punk style future where you can create your own destiny."
    global room
    room = [1, 1]
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
        cdex += 1
        cint += 5
        cwis += 3
        ccha += 4
    elif cclass == "netmind":
        cclass = "Netmind"
        cstr += 0
        ccon += 2 
        cdex += 0
        cint += 3
        cwis += 5
        ccha += 5   
    elif cclass == "runner":
        cclass = "Runner"
        cstr += 2
        ccon += 3 
        cdex += 5
        cint += 0
        cwis += 2
        ccha += 3
    elif cclass == "cybernetic":
        cclass = "Cybernetic"
        cstr += 5
        ccon += 5 
        cdex += 0
        cint += 2
        cwis += 2
        ccha += 1
    elif cclass == "warlord": 
        cclass = "Warlord"
        cstr += 4
        ccon += 3 
        cdex += 0
        cint += 1
        cwis += 2
        ccha += 5

    print "Here is your character sheet. To see your character sheet just type, /c "
    csheet()
    raw_input("Press enter to continue....")

    return;

def csheet():
    
    print " "
    print "--Character Sheet--"
    print "Name:  " + cname
    print "Sex:   " + csex
    print "Class: " + cclass
    print "--------Stats--------"
    print "Strength:     " + str(cstr)
    print "Constitution: " + str(ccon)
    print "Dexterity:    " + str(cdex)
    print "Intelligence: " + str(cint)
    print "Wisdom:       " + str(cwis)
    print "Charisma:     " + str(ccha)
    print " "


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

    with open('./db/world.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if room[0] == row['x'] and room[1] == row['y']:
                #print(row['x'], row['y'], row['title'], row['desc'], row['exits'], row['npc'])
                title = row['title']
                des = row['desc']
                exits = row['exits']
                npc = row['npc']

            


    return (title, des, exits, npc);

new_game()
