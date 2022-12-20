import json
import os

with open('db.json', 'r') as f:
    database = json.load(f)
with open('item.json', 'r') as f:
    item = json.load(f)

max_lv = 99

def login(): #Login Page Gui
    os.system('cls')
    #print('RPG BETA\n\n[Login]\n[Sign in]')
    global id
    id, pw = input('Input your id : '), input('Input your password : ')
    if id in list(database.keys()):
        if database[id]['pw'] == pw:
            print(database[id]['data']['place'])
            state()
        else:
            print('wrong password')
    else:
        print('You not have id')

def signin(): #Signin Page Gui
    a = 1

def state(): #state test
    os.system('cls')
    t = 'NULL' if database[id]['data']['title'] is None else database[id]['data']['title'] 
    l = 'MAX' if database[id]['data']['lv'] >= max_lv else str(database[id]['data']['lv'])
    print('[' + t + '] ' + id)
    print('{'+ l +'} EXP | ' + str(database[id]['data']['exp']) + ' / ' + str(database[id]['data']['lv'] * 10))

def gui():
    a = 1

login()
# print('▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌')