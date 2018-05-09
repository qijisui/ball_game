import sys
import pygame
import math
import time
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
    
    block_list = []
    for i in range(0,5):
        block_list.append(Block(screen,(randint(0,screen_width),randint(0,screen_height)),70,200,color=(randint(0,255),randint(0,255),randint(0,255))))
    
    ball_list  = []

    for i in range(0,50):
        ball_list.append(Ball(screen,amp=randint(1,5),angle = randint(0,180),centerx=randint(0,screen_width),centery=randint(0,screen_height),color=(randint(0,255),randint(0,255),randint(0,255))))
        
    while True:
        screen.fill(bg_color)
        for ball in ball_list :
            ball.ball_demo(screen_width,screen_height)
            # 如果与小球发生碰撞
            for block in block_list:
                if block.hit_check(ball.ball_pos_get()) :
                    point = block.intersect_point_get(ball.rad,ball.ball_pos_get())
                    ball.velocity_reflect(point[2])
        for block in block_list:   
            block.draw_block()
        pygame.display.flip()
        time.sleep(0.01)
        
run_game()
