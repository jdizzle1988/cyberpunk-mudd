#!/usr/bin/python
import csv
import os
import numpy as nrand
import sqlite3

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
            print "There is no one around to talk to."
        print " "
        
        if "pve" in zone:
            chance = int(nrand.random.randint(low=0, high=10, size=1))
            if chance <= 2:
                print "Something attacks!"
                combat()
            else:
                print "You do not see any enemies."
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
    global invloop
    invloop = 1
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
    atk = 2
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
    raw_input("Press enter to continue....")
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
    invloop = 1
    while invloop == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        conn = sqlite3.connect('./db/cyberpunkdb.sqlite3')
        c = conn.cursor()
        print "-------Inventory-------"
        print "======================="
        print "Credits: " + str(credit)
        print "-------Equipped-------"
        for row in c.execute("SELECT i.title, i.pos FROM player_inv pi, items i WHERE pi.item_id = i.id AND equip = 'y'"):
            print str(row[1]) + ": " + str(row[0])
        print "----------------------"
        print "-------Backpack-------"
        c.close()
        c1 = conn.cursor()
        for row in c1.execute("SELECT i.title FROM player_inv pi, items i WHERE pi.item_id = i.id AND pack = 'y'"):
            print row[0]
        print " "  
        c1.close()
        command = raw_input("What would you like to do? ")
        
        if "equip" in command:
            print " "
            print "---In Backpack---"
            c2 = conn.cursor()
            for row in c2.execute("SELECT i.title FROM player_inv pi, items i WHERE pi.item_id = i.id AND pack = 'y'"):
                print row[0]
            print " "  
            c2.close()         
            command = raw_input("What would you like to equip? ")
            temp = []
            temp1 = []
            temp2 = []
            c3 = conn.cursor()
            for row in c3.execute("SELECT * FROM player_inv_v WHERE pack = 'y' AND title = '" + command + "'"):
                pos1 = row[5]
                c5 = conn.cursor()
                c5.execute("UPDATE player_inv SET equip = 'n', pack = 'y' WHERE equip = 'y' AND pos = '" + str(pos1) + "'")
                c4 = conn.cursor()
                c4.execute("UPDATE player_inv SET equip = 'y', pack = 'n' WHERE item_id = " + str(row[0]))
            conn.commit()
            c3.close()
            c4.close()
            c5.close()
            conn.close()
            # with open('./player_data/temp_inv.csv', 'wb') as wcsvfile:
            #     fieldnames = ['id','title','desc','buff','dmg','equip','pack','pos']
            #     writer = csv.DictWriter(wcsvfile, fieldnames=fieldnames, extrasaction='ignore')
            #     writer.writeheader()
            #     #thisdict = {'id': temp2[0], 'title': temp2[1], 'desc': temp2[2], 'buff': temp2[3], 'dmg': temp2[4], 'equip': temp2[5], 'pack': temp2[6], 'pos': temp2[7]}
            #     writer.writerows(temp2)
            



        elif "exit" in command:
            invloop = 0

        
            
            #print temp2
        raw_input("Press any key....")
    return;

def combat():
    conn = sqlite3.connect('./db/cyberpunkdb.sqlite3')
    c = conn.cursor()

    ename = ""
    ehp = 0
    ehpmax = 0
    eatk = 0
    eac = ""
    print "------Combat------"
    for row in c.execute("SELECT * FROM enemies WHERE id = 1"):
        ename = row[1]
        ehp = row[3]
        ehpmax = ehp
        eatk = row[4]
        eac = row[5]
    c.close()
    conn.close()
    fightloop = 1
    turn = 1
    #chpmax = hp
    global chp
    while fightloop != 0: 
        if ehp <= 0:
            fight_win()
            fightloop = 0
        elif chp <= 0:
            print "Fuck"
        else:
            os.system('cls' if os.name == 'nt' else 'clear')           
            print "Enemy: " + str(ename)
            print "HP:    " + str(ehp) + "/" + str(ehpmax)
            print "---------------------"
            print "Your HP: " + str(chp) + "/" + str(hp)
            if turn == 1:
                command = raw_input("What do you want to do?: ")
                if "attack" in command:
                    dmg = int(nrand.random.randint(low=0, high=(atk + (cstr - 10)), size=1))
                    if dmg == 0:
                        print "You missed " + str(ename) + "!"
                    else:
                        print "You strike " + str(ename) + " causing " + str(dmg) + " damage!"
                    ehp -= dmg
                    raw_input("Press Enter to end turn...")
                    turn = 0
                else:
                    print "You didn't enter a valid command!"
                
            else:
                edmg = int(nrand.random.randint(low=1, high=eatk, size=1))
                if edmg == 0:
                    print str(ename) + " Misses you!"
                else:
                    print str(ename) + " strikes you for " + str(edmg) + " damage!"
                #global hp 
                chp -= edmg
                turn = 1
                
                raw_input("Press enter to start your turn...")



    return;

def fight_win():

    print "You Win!"

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

    conn = sqlite3.connect('./db/cyberpunkdb.sqlite3')
    c = conn.cursor()
    
    
    #get_room = room.split("|")
    title = ""
    des = ""
    exits = ""
    npc = ""
    zone = ""
    lvl = ""

    for row in c.execute("SELECT * FROM world WHERE x = " + str(room[0]) + " and y = " + str(room[1])):
        title = row[3]
        des = row[4]
        exits = row[5]
        npc = row[6]
        zone = row[7]
        lvl = row[8]

    # with open('./db/world.csv') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         if str(room[0]) == row['x'] and str(room[1]) == row['y']:
    #             #print(row['x'], row['y'], row['title'], row['desc'], row['exits'], row['npc'])
    #             title = row['title']
    #             des = row['desc']
    #             exits = row['exits']
    #             npc = row['npc']
    #             zone = row['zone']
    #             lvl = row['lvl']
    #             #print title + des + exits + npc

            

    c.close()
    conn.close()
    return title, des, exits, npc, zone, lvl;

start_game()

