import pygame
import random
import math
from pygame import mixer

pygame.init()

#Creating the Screen
screen = pygame.display.set_mode((800,600))#width and height

#background
background = pygame.image.load('background.jpeg')

#title and icon

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#playerIcon
picon = pygame.image.load('player.png')
piconx = 370
picony = 150
picony = "Ready"
#playerVariables
playerIcon = pygame.image.load('player.png')
playerX = 370
PlayerY = 490
playerX_change = 0

#backgroundMusic
mixer.music.load('background.wav')
mixer.music.play(-1)

#EnemyVariables
enemyIcon= []
enemyY=[]
enemyX=[]
enemyX_change=[] 
enemyY_change=[]
no_of_enemies = 6
for i in range(no_of_enemies):
    enemyIcon.append(pygame.image.load('skull.png'))
    enemyX.append(random.randint(0,729))
    enemyY.append(random.randint(50,200))
    enemyX_change.append(5)
    enemyY_change.append(4)

#BulletVariables
BulletIcon = pygame.image.load('bullet.png')
BulletX = 0
BulletY = 490
BulletX_change = 0
BulletY_change = 10
bullet_State = "Ready"#you cant see the bullet but it is present

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY= 10
font_name = pygame.font.Font('freesansbold.ttf',15)
dev_name = font_name.render("BySHUBHAM",True,(255,255,255))
namex = 10
nameY = 50

#game over text

over_font = pygame.font.Font('freesansbold.ttf',64)

#showScoreFUnc
def show_score(x,y):
    score = font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

#gameOVerFuncation

def game_over_text():
    over_text = font.render("GAME OVER ",True,(255,255,255))
    screen.blit(over_text,(300,250))


#playerFunction

def player(x,y):
    screen.blit(playerIcon,(x,y))

#enemyFunction
def enemy(x,y,i):
    screen.blit(enemyIcon[i],(x,y))

#bulletFunction
def fire(x,y):
    global bullet_State
    bullet_State = "fire"
    screen.blit(BulletIcon,(x+16,y+10))

#collisonFunction

def collision(enemx,enemyy,Bulletx,BUllety):
    distance = math.sqrt((math.pow(enemx-Bulletx,2))+(math.pow(enemyy-BUllety,2)))
    if distance < 27:
        return True
    else:
        return False



if __name__ == "__main__":


    #Game loop
    Running = True
    while Running:
        #RGB        
        screen.fill((0,0,0))
        screen.blit(background,(0,0))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
        
            
            #if keystroke is pressed
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    playerX_change =-4        
                if event.key == pygame.K_RIGHT: 
                    playerX_change =4
                if event.key == pygame.K_SPACE:
                    if bullet_State is "Ready":
                        bullet_sound = mixer.Sound('laser.wav')
                        bullet_sound.play()
                        #get current x cordinate
                        BulletX = playerX
                        fire(BulletX,BulletY)


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
        
        #checking player boundaries  
        playerX += playerX_change
        if playerX <= 0:
            playerX =0
        elif playerX >= 730:
            playerX = 730
        
        #checking for enemy boundaries enenmy movement
        for i in range (no_of_enemies):
            #gameover 
            if enemyY[i] > 440:
                for j in range(no_of_enemies):
                    enemyY[j] = 2000
                    game_over_text()
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 5
                enemyY[i] += enemyY_change[i]

            elif enemyX[i] >= 730:
                enemyX_change[i] =-5
                enemyY[i] += enemyY_change[i]

    



        #checking collision
        
            colision = collision(enemyX[i],enemyY[i],BulletX,BulletY)
            if colision:
                colision_sound = mixer.Sound('explosion.wav')
                colision_sound.play()
                BulletY = 490
                bullet_State = "Ready"
                score_value +=1
                print(score_value)
                enemyX[i] = random.randint(0,729)
                enemyY[i] = random.randint(50,200)
                
            enemy(enemyX[i],enemyY[i],i)
            

        
        #bulletMovement
        if BulletY<=0:
            BulletY = 490
            bullet_State="Ready"
        

        if bullet_State is "fire":
            fire(BulletX,BulletY)
            BulletY -= BulletY_change
        # #increasing level
        # if score_value % 5 == 0:
        #     for i in range (no_of_enemies):
        #         #gameover 
        #         if enemyY[i] > 440:
        #             for j in range(no_of_enemies):
        #                 enemyY[j] = 2000
        #                 game_over_text()
        #         enemyX[i] += enemyX_change[i]
        #         if enemyX[i] <= 0:
        #             enemyX_change[i] = 5
        #             int(enemyX_change[i] + 2)
                    
        #             enemyY[i] += enemyY_change[i]

        #         elif enemyX[i] >= 730:
        #            enemyX_change[i] =-5
        #            enemyX_change[i] =-2
             
        #            enemyY[i] += enemyY_change[i]
           

    
        player(playerX,PlayerY)
        show_score(textX,textY)
        screen.blit(dev_name,(namex,nameY))
    
        pygame.display.update()