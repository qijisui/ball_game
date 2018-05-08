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
        
    
    def draw_block(self):
        ''' 将图形绘制在屏幕上 
            绘制矩形函数
            rect(Surface, color, Rect, width=0)
        '''
        left        = self.centerx - self.size/2
        top         = self.centery - self.size/2
        width       = self.size
        height      = self.size
        block_rect  = pygame.Rect(left, top, width, height)
        pygame.draw.rect(self.screen,self.color,block_rect,0)
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







        