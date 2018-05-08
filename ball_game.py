import sys
import pygame
import math
from random import randint
from ball import Ball
from block import Block

def run_game():
    pygame.init()
    pygame.display.set_caption("Ball Game")
    bg_color = (230,230,230)
    screen_width = 860
    screen_height = 640
    screen   =  pygame.display.set_mode((screen_width,screen_height))
    block    =  Block(screen,(100,100),70,20,color=(0,0,0))
    
    ball_list  = []

    for i in range(1,50):
        ball_list.append(Ball(screen,amp=randint(1,10),angle = randint(0,180),centerx=randint(0,screen_width),centery=randint(0,screen_height),color=(randint(0,255),randint(0,255),randint(0,255))))
        

    while True:
        screen.fill(bg_color)
        for ball in ball_list :
            ball.ball_demo(screen_width,screen_height)
        #block.draw_block()
        pygame.display.flip()
run_game()
