from pygame.math import Vector2
import pygame,sys,random

class Snake:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction=Vector2(1,0)
    def draw_snake(self):
        for block in self.body:         #iterating thru the body 
            x_pos=int(block.x*cell_size)
            y_pos=int(block.y*cell_size)
            block_rect=pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)
    def move_snake(self):
        body_copy=self.body[:-1]
        body_copy.insert(0,body_copy[0]+self.direction) #adding two vectors
        self.body=body_copy[:]
         
class Fruit:

    def __init__(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x,self.y)
    def draw_fruit(self):
        fruit_rect=pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)


pygame.init()
cell_size=40
cell_number=20
screen=pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
clock=pygame.time.Clock()   

fruit=Fruit()
snake=Snake()
# test_surface=pygame.Surface ((100,200))
# test_surface.fill((0,0,255))
# test_rect=test_surface.get_rect(center   =(200,250))
# x_pos=200

SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction=Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                snake.direction=Vector2(0,1)
            if event.key == pygame.K_LEFT:
                snake.direction=Vector2(-1,0) 
            if event.key == pygame.K_RIGHT:
                snake.direction=Vector2(1,0)           
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    # screen.blit(test_surface,(x_pos,250))
    # screen.blit(test_surface,test_rect)
    pygame.display.update()
    clock.tick(60)
