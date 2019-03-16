import pygame
import random
import tkinter as tk
from tkinter import *
import os


WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
YELLOW =    (255, 255, 231)
GREY =      (89, 101, 109)
TEXTCOLOR = (  0,   0,  0)

(width, height) = (500, 500)

a = pygame.math.Vector2(width/2,0)
b = pygame.math.Vector2(0,height)
c = pygame.math.Vector2(width,height)

g = pygame.math.Vector2(random.randint(0, width),random.randint(0, height))

running = True

def drawCircle():
    pygame.draw.circle(screen, YELLOW, (int(a.x), int(a.y)), 1)
    pygame.draw.circle(screen, YELLOW, (int(b.x), int(b.y)), 1)
    pygame.draw.circle(screen, YELLOW, (int(c.x), int(c.y)), 1)

    pygame.draw.circle(screen, YELLOW, (int(g.x), int(g.y)), 1)

def createFractal():
    global g

    r = random.randint(0,2)
    if r == 0:
        g = midpoint(g,a)

        pygame.draw.circle(screen, YELLOW, (int(g.x), int(g.y)), 1)

    if r == 1:
        g = midpoint(g,b)

        pygame.draw.circle(screen, YELLOW,(int(g.x), int(g.y)), 1)
        
    if r == 2:
        g = midpoint(g,c)
        
        pygame.draw.circle(screen, YELLOW, (int(g.x), int(g.y)), 1)

def midpoint(p1, p2):
    return pygame.math.Vector2((p1.x+p2.x)/2, (p1.y+p2.y)/2)
    
def main():
    global running, screen, buttonwin

    root = tk.Tk()

    embed = tk.Frame(root, width = 500, height = 500) #creates embed frame for pygame window
    embed.grid(columnspan = (600), rowspan = 500) # Adds grid
    embed.pack(side = BOTTOM) #packs window to the left

    os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
    os.environ['SDL_VIDEODRIVER'] = 'windib'

    pygame.display.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill(GREY)
    buttonwin = tk.Frame(root, width = 75, height = 500)
    buttonwin.pack(side = BOTTOM)

    label1 = Label(buttonwin,text = 'SIERPINSKI TRAINGLE')
    label1.pack(side=BOTTOM)

    label2 = Label(buttonwin,text = 'Press the menu to plot first three point, then press any up arrow to start simulation.')
    label2.pack(side=BOTTOM)
    
    root.update()
    pygame.display.update()

    while running:
        keys = pygame.key.get_pressed()  #checking pressed keys
        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawCircle()
                pygame.display.update()

            if event.type == pygame.QUIT:
                running = False

            while keys[pygame.K_UP]:
               createFractal()
               pygame.display.update()
                
if __name__ == '__main__':
    main()
