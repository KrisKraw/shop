#!/usr/bin/env python3

from items import items

cart = []
shop = True

print('\nwelcome to Amazon :)')

def getItem(itemNum):
    for item in items:
        if itemNum == item['num']:
            return item
        

def listItems():
    print('item# \t name  \t\t price')
    print('==============================')
    for item in items:
        itemNum = item['num']
        itemName = item['name']
        itemPrice = item['price']
        print(str(itemNum) + ' \t ' + itemName + ' \t ' + str(itemPrice))

def addItem(menuChoice):
    global cart
    itemNum = menuChoice[2::]
    cart.append(itemNum)
    itemName = getItem(itemNum)['name']
    print(f'{itemName} has been added to your cart...')

def showCart():
    global cart
    print('your cart contains: ')
    print('item# \t name  \t price')
    print('==============================')
    subtotal = 0
    for item in cart:
        itemName = getItem(item)['name']
        itemPrice = getItem(item)['price']
        subtotal += itemPrice
        print(itemName + ' \t ' + str(itemPrice))
    print(f'\nsubtotal: $ {subtotal}')


def clearCart():
    global cart
    cart = []
    print('your cart has been cleared...')


def checkOut():
    print('your order has been placed....')
    exitApp()


def exitApp():
    shop = False
    print('thank you for shopping with Amazon. see you soon :)')
    quit()


def showMenu():
    print('\ni  list items')
    print('a itemnum  add item to cart')
    print('s  show shopping cart')
    print('c  clear shopping cart')
    print('o  check out')
    print('e  exit')


def main():
    while shop == True:
        showMenu()
        menuChoice = input('? ').lower()
        if menuChoice == "i":
            listItems()
        elif menuChoice[0:2:1] == 'a ':
            addItem(menuChoice)
        elif menuChoice == "s":
            showCart()
        elif menuChoice == "c":
            clearCart()
        elif menuChoice == "o":
            checkOut()
        elif menuChoice == "e":
            exitApp()

main()