#!/usr/bin/env python3

from items import items

cart = []
shop = True

print('welcome to Amazon :)')

def listItems():
    for item in items:
        itemNum = item['num']
        itemName = item['name']
        itemPrice = item['price']
        print(str(itemNum) + ' \t ' + itemName + ' \t ' + str(itemPrice))

def exitApp():
    shop = False
    print('thank you for shopping with Amazon. see you soon :)')
    quit()

def showMenu():
    print('\n\ni  list items')
    print('a itemnum  add item to cart')
    print('s  show shopping cart')
    print('c  clear shopping cart')
    print('b  buy items')
    print('e  exit')

def main():
    global cart
    while shop == True:
        showMenu()
        menuChoice = input('? ').lower()
        print('*' + menuChoice[0:2:1] + '*')
        if menuChoice == "i":
            listItems()
        elif menuChoice[0:2:1] == 'a ':
            itemNum = menuChoice[2::]
            print(itemNum)
            #if itemNum in items:
            cart.append(itemNum)
            print(cart)
            print('    has been added to your cart...')
        elif menuChoice == "s":
            print('your cart contains: ')
            print(cart)
        elif menuChoice == "c":
            print(cart)
            cart = []
            print(cart)
            print('your cart has been cleared...')
        elif menuChoice == "b":
            print('your order has been placed....')
            exitApp()
        elif menuChoice == "e":
            exitApp()

main()