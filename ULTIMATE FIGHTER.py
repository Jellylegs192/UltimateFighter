import random
import time

print('--------------------------------')
print('WELCOME TO ULTIMATE FIGHTER!!!!!')
print('--------------------------------')

options = input('Press "1" for easy, Press "2" for medium and "3" for Champion difficulty. If you wish to view '\
'history of the past Champions type "4"\n')

if options == "1":
    monsterhp = 10
    hp = 20
    Mp = 1
    
    while monsterhp > 0 and hp > 0:
        print(f"Monster hp = {monsterhp}")
        print(f"HP =         {hp}")
        print(f"MP =         {Mp}") 
        print("What will you do?")
        print("--------------------")
        print(" 1. Sword   2. Fire \n 3. Heal   4. Mana ")
        attack = input("Decision: ")
        print("--------------------")
        if attack == "1":
            Sword = random.randint(2, 5)
            monsterhp -= Sword
            print(f"You attacked with your sword for {Sword}")
        elif attack == "2":
            if Mp > 0: 
                Mana = random.randint(8, 13)
                monsterhp -= Mana
                Mp -= 1
                print(f"You Burned the monster for {Mana} ")
            else:
                print("You have no more MP")
        elif attack == "3":
            hp +=random.randint(2,14)
            print("You heal yourself")
        elif attack == "4":
            reg = random.randint(0,2)
            if reg == 0:
                print('Mana failed!')
            else:
                Mp += reg
        if monsterhp > 0:
            print("\nMonster's turn")
            time.sleep(5)
            monsterattack = random.randint(1, 10)
            hp -= monsterattack
            print(f'\n \nMonster attacks for {monsterattack} \n ')
        else:
            break
    
    if hp > monsterhp:
        print("\nYou won the battle")
    else:
        print("\nYou Died")
    
if options == "2":
    monsterhp = 20
    hp = 20
    Mp = 1
    
    while monsterhp > 0 and hp > 0:
        print(f"Monster hp = {monsterhp}")
        print(f"HP =         {hp}")
        print(f"MP =         {Mp}") 
        print("What will you do?")
        print("--------------------")
        print(" 1. Sword   2. Fire \n 3. Heal   4. Mana ")
        attack = input("Decision: ")
        print("--------------------")
        if attack == "1":
            Sword = random.randint(2, 5)
            monsterhp -= Sword
            print(f"You attacked with your sword for {Sword}")
        elif attack == "2":
            if Mp > 0: 
                Mana = random.randint(8, 12)
                monsterhp -= Mana
                Mp -= 1
                print(f"You Burned the monster for {Mana} ")
            else:
                print("You have no more MP")
        elif attack == "3":
            hp +=random.randint(2,12)
            print("You heal yourself")
        elif attack == "4":
            reg = random.randint(0,2)
            if reg == 0:
                print('Mana failed!')
            else:
                Mp += reg
        if monsterhp > 0:
            print("\nMonster's turn")
            time.sleep(5)
            monsterattack = random.randint(1, 10)
            hp -= monsterattack
            print(f'\n \nMonster attacks for {monsterattack} \n ')
        else:
            break
    
    if hp > monsterhp:
        print("\nYou won the battle")
    else:
        print("\nYou Died")
    

if options == "3":
    monsterhp = 30
    hp = 20
    Mp = 1
    
    while monsterhp > 0 and hp > 0:
        print(f"Monster hp = {monsterhp}")
        print(f"HP =         {hp}")
        print(f"MP =         {Mp}") 
        print("What will you do?")
        print("--------------------")
        print(" 1. Sword   2. Fire \n 3. Heal   4. Mana ")
        attack = input("Decision: ")
        print("--------------------")
        if attack == "1":
            Sword = random.randint(2, 5)
            monsterhp -= Sword
            print(f"You attacked with your sword for {Sword}")
        elif attack == "2":
            if Mp > 0: 
                Mana = random.randint(8, 12)
                monsterhp -= Mana
                Mp -= 1
                print(f"You Burned the monster for {Mana} ")
            else:
                print("You have no more MP")
        elif attack == "3":
            hp +=random.randint(2,10)
            print("You heal yourself")
        elif attack == "4":
            reg = random.randint(0,2)
            if reg == 0:
                print('Mana failed!')
            else:
                Mp += reg
        if monsterhp > 0:
            print("\nMonster's turn")
            time.sleep(5)
            monsterattack = random.randint(1, 14)
            hp -= monsterattack
            print(f'\n \nMonster attacks for {monsterattack} \n ')
        else:
            break
    
    if hp > monsterhp:
        print("\nYou won the battle! You are a true champion!")
        name = input('What is your name so it may be etched into history: ')
        file = open('Champions.txt','a')
        file.write('\n')
        file.write(name)
        file.close()
    else:
        print("\nYou Died")


if options == "4":
    print('\n\nTHESE ARE THE ULTIMATE CHAMPIONS\n\n')
    record = open('Champions.txt','r')
    f = record.read()
    print(f)
    record.close()

