
import pygame
import random

#defining colours
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)


#pygame initialisation
x=pygame.init()
window_x=500
window_y=500
gamewindow=pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("mrjk snake game")
font = pygame.font.SysFont(None, 55)
clock=pygame.time.Clock()

def plotsnake(gamewindow,colour,head,snake_size):
    for x,y in head:
        pygame.draw.rect(gamewindow,colour,[x,y,snake_size,snake_size])

def check_gameover(head,snake_list):
    if head in snake_list[:-1]:
        return True
    else:
        return False


def mainloop():
    gameover=False
    quitgame=False
    score=0
    fps=60
    snake_x=random.randint(20,window_x-20)
    snake_y=random.randint(20,window_y-20)
    food_x=random.randint(20,window_x-20)
    food_y=random.randint(20,window_y-20)
    velocity_x=0
    velocity_y=0
    snake_size=10
    snake_length=1
    snake_list=[]
    previous="null"
    while not quitgame:
        if gameover==True:
            gamewindow.fill(white)
            text="Gameover. score:"+str(score)
            message = font.render(text, True,red)
            gamewindow.blit(message,(10,10))
            text1="Press enter to play again"
            message1 = font.render(text1, True,red)
            gamewindow.blit(message1,(10,60))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        mainloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame=True
                if event.type==pygame.KEYDOWN: 
                    if event.key==pygame.K_RIGHT:
                        if previous!="left":
                            velocity_x=4
                            velocity_y=0
                            previous="right"
                    if event.key==pygame.K_LEFT:
                        if previous!="right":
                            velocity_x=-4
                            velocity_y=0
                            previous="left"
                    if event.key==pygame.K_UP:
                        if previous!="down":
                            velocity_x=0
                            velocity_y=-4
                            previous="up"
                    if event.key==pygame.K_DOWN:
                        if previous!="up":
                            velocity_x=0
                            velocity_y=4
                            previous="down"
            snake_x+=velocity_x
            snake_y+=velocity_y

            if snake_x>window_x:
                snake_x=0
            if snake_x<0:
                snake_x=window_x
            if snake_y>window_y:
                snake_y=0
            if snake_y<0:
                snake_y=window_y
            
            
            if abs(snake_x-food_x)<9 and abs(food_y-snake_y)<9:
                score+=10
                snake_length+=4
                food_x=random.randint(20,window_x-20)
                food_y=random.randint(20,window_y-20)  
                     

            gamewindow.fill(white)
            text1="Score: "+str(score)
            message1 = font.render(text1, True,red)
            gamewindow.blit(message1,(5,5))
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            
            plotsnake(gamewindow,black,snake_list,snake_size)
            
            gameover=check_gameover(head,snake_list)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
            pygame.display.update()
            clock.tick(fps)
    pygame.quit()
    quit()


mainloop()
print("apple")