import os
import random
import keyboard
import time


mapX, mapY = 25, 25
beatmap = [[2 for j in range(mapX+2)] for i in range(mapY+2)]

pX, pY  = 4, 4
tick = 0.3


def create_map():
    for i in range(mapY):
        for j in range(mapX):
            r = random.randrange(0, 5)
            beatmap[i+1][j+1] = 0 if r == 2 else 0 if r == 1 else r

def show_map(): 
    os.system('cls')
    beatmap[pY][pX] = 1 #Player Spawn
   
    for i in range(mapY+2):
        for j in range(mapX+2):
            e = beatmap[i][j]
            if e == 0: #empty
                print('  ', end='')
            elif e == 1: #player
                print('▣ ', end='')
            elif e == 2: #wall
                print('██', end='')
            elif e == 3:
                print('🪨 ', end='')
            elif e == 4:
                print('🌳', end='')
        print('')

def main():
    global mpX
    global mpY
    global pX
    global pY
    mpObj = [0, 0]
    while True:
        if keyboard.is_pressed('w'):
            mpX, mpY = pX, pY
            pY -= 1
            mpObj[0] = beatmap[pY][pX]
            if mpObj[0] == 2 or mpObj[0] == 3:
                pY += 1
                mpObj[0] = beatmap[pY][pX]
            else:
                beatmap[pY][pX] = 1
                beatmap[mpY][mpX] = mpObj[1]
                mpObj[1] = mpObj[0]
            show_map()
            time.sleep(tick)
        if keyboard.is_pressed('s'):
            mpX, mpY = pX, pY
            pY += 1
            mpObj[0] = beatmap[pY][pX]
            if mpObj[0] == 2 or mpObj[0] == 3:
                pY -= 1
                mpObj[0] = beatmap[pY][pX]
            else:
                beatmap[pY][pX] = 1
                beatmap[mpY][mpX] = mpObj[1]
                mpObj[1] = mpObj[0]
            show_map()
            time.sleep(tick)
        if keyboard.is_pressed('a'):
            mpX, mpY = pX, pY
            pX -= 1
            mpObj[0] = beatmap[pY][pX]
            if mpObj[0] == 2 or mpObj[0] == 3:
                pX += 1
                mpObj[0] = beatmap[pY][pX]
            else:
                beatmap[pY][pX] = 1
                beatmap[mpY][mpX] = mpObj[1]
                mpObj[1] = mpObj[0]
            show_map()
            time.sleep(tick)
        if keyboard.is_pressed('d'):
            mpX, mpY = pX, pY
            pX += 1
            mpObj[0] = beatmap[pY][pX]
            if mpObj[0] == 2 or mpObj[0] == 3:
                pX -= 1
                mpObj[0] = beatmap[pY][pX]
            else:
                beatmap[pY][pX] = 1
                beatmap[mpY][mpX] = mpObj[1]
                mpObj[1] = mpObj[0]
            show_map()
            time.sleep(tick)
        if keyboard.is_pressed('q'):
            return 0


create_map()
show_map()
main()

# print(beatmap)

