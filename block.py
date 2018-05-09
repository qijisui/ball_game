import math
import pygame
class Block():
    def __init__(self,screen,pos,size,num,color=(0,0,0)):
        self.screen = screen
        self.centerx= pos[0]
        self.centery= pos[1]
        self.size   = size 
        self.num    = num
        self.color  = color
        self.draw_block()
    
    def draw_block(self):
        ''' 将图形绘制在屏幕上 
            绘制矩形函数
            rect(Surface, color, Rect, width=0)
        '''
        self.left             = self.centerx - self.size/2
        self.top              = self.centery - self.size/2
        self.width            = self.size
        self.height           = self.size
        self.right            = self.left + self.width
        self.bottom           = self.top + self.height
        self.block_rect       = pygame.Rect(self.left, self.top, self.width, self.height)
        pygame.draw.rect(self.screen,self.color,self.block_rect,0)
        # 绘制num数到方块上
        self.draw_num()
        
    def draw_num(self):
        ''' 
            使用 pygame.font 类
            中的render方法，用法如下：
            render(...)
            render(text, antialias, color, background=None) -> Surface
            draw text on a new Surface
            blit(...)
            blit(source, dest, area=None, special_flags = 0) -> Rect
            draw one image onto another
        '''
        str_size = 30
        num_str = str(self.num)
        str_x_pixel = str_size/2*len(num_str) # 求出字符串的像素宽
        str_y_pixel = str_size                # 求出字符串像素高
        (str_pos_x,str_pos_y) = (self.centerx-str_x_pixel/2,self.centery-str_y_pixel/2)
        my_font = pygame.font.SysFont('arial',str_size)
        self.screen.blit(my_font.render(str(self.num), True, (255,255,255)), (str_pos_x, str_pos_y))
    
    def intersect_point_get(self,rad,pos):
        '''
            用于检测碰撞点
        '''
        # 计算方程 y = ax + b
        # 直线斜率等于tan值
        a = math.tan(rad)
        # y=ax+b 求b 需使用 b = y - a*x
        b = pos[1] - a * pos[0] 
        
        #print('小球轨迹入射曲线为：y = {0:.3f}x + {1:.3f}'.format(a,b))
        
        # 计算小球所在直线与正方型的交点设直线与上下左右四条边的交点分别为p1,p2,p3,p4
        
        # 已知y求x 用 x = (y - b)/a
        x1 = ( self.top - b )/a 
        x2 = ( self.bottom - b )/a
        # 已知x求y 用 ax + b
        y3 = a * self.left + b
        y4 = a * self.right + b
        
        #print('直线与正方形四条边延长线交点为p1={{{:0.3f},{:0.3f}}},p2={{{:0.3f},{:0.3f}}},p3={{{:0.3f},{:0.3f}}},p4={{{:0.3f},{:0.3f}}}'.format(x1,self.top,x2,self.bottom,self.left,y3,self.right,y4))
        
        # 将所有交点添加到列表中 (最后面的参数为法线参数)
        point_list = [(x1,self.top,math.radians(90)),(x2,self.bottom,math.radians(90)),(self.left,y3,math.radians(180)),(self.right,y4,math.radians(180))] 
        
        intersect_point_list = []
        # 检测在正方型边界上的点,存储到列表中
        for p in point_list :
            if (p[0] >= self.left and p[0] <= self.right and  p[1] >= self.top and p[1] <= self.bottom) :
                intersect_point_list.append(p)
       
        # 将列表中的点按照x值从小到大进行排列
        intersect_point_list.sort(key=lambda p:p[0])
        #print(intersect_point_list)

        
        # 根据输入的速度方向的x速度分量若大于0则代表小球x轴上由左到右运动，取最左边交点，反之取最右侧交点
        if math.cos(rad) >= 0 :
            intersect_point = intersect_point_list[0]
        else :
            intersect_point = intersect_point_list[-1]

        #print ('交点为{}'.format(intersect_point))
        
        return intersect_point
        
    
    def hit_check(self,pos):
        '''
            用于检测某物体是否与该方块发生碰撞
             collidepoint(...)
             collidepoint(x, y) -> bool
             collidepoint((x,y)) -> bool
             test if a point is inside a rectangle
        '''
        ishit=self.block_rect.collidepoint(pos)
        if ishit :
            self.num-=1
        
        return ishit 
            
            
            
            
#import sys
#import pygame
#import math
#from random import randint
#from ball import Ball
#from block import Block
#
#pygame.init()
#pygame.display.set_caption("Ball Game")
#bg_color = (230,230,230)
#screen_width = 860
#screen_height = 640
#screen   =  pygame.display.set_mode((screen_width,screen_height))
#
#block = Block(screen,(0,0),10,10)
#block.intersect_point_get(math.radians(145),(0,0))




        