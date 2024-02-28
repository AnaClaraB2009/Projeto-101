import random


response = input("Do you want to roll a dice? (y/n) ")

#quando eu troco o 'while' por um 'if' funciona
while response == "y":
    dado = random.randint(1,6)

if (dado == 1) :
    print("-----")
    print("| 1 |")
    print("-----")
    response = input("Do you want to keep playing? (y/n)")

if (dado == 2) :
    print("-----")
    print("| 2 |")
    print("-----")
    response = input("Do you want to keep playing? (y/n)")

if (dado == 3) :
    print("-----")
    print("| 3 |")
    print("-----")
    response = input("Do you want to keep playing? (y/n)")

if (dado == 4) :
    print("-----")
    print("| 4 |")
    print("-----")
    response = input("Do you want to keep playing? (y/n)")

if (dado == 5) :
    print("-----")
    print("| 5 |")
    print("-----")
    response = input("Do you want to keep playing? (y/n)")

if (dado == 6) :
    print("-----")
    print("| 6 |")
    print("-----")
    response = input("Do you want to keep playing? (y/n)")



