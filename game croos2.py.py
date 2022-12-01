"""
programmer by en:salem khmes phyan
"""
import pygame
from pygame.locals import *
from sys import exit
import sys
import time,random

x=random.randrange(5,390,1)
y=280
pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')
WHITE = (255, 255, 255)
catImg1 = pygame.image.load('2.png')
catImg2 = pygame.image.load('2.png')
catImg3 = pygame.image.load('2.png')
catImg4 = pygame.image.load('2.png')
background = pygame.image.load('game.jpeg')
speed1=[10,0]
speed2=[10,1]
catx2 = 15
caty2 = 90
catx3 = 169
caty3 = 203
speed=[0,0]
position =catImg1.get_rect()
position2=catImg2.get_rect()
badrect=pygame.Rect(catImg2.get_rect())
badrect1=pygame.Rect(catImg3.get_rect())
global f1,d
hit = pygame.mixer.Sound("alarm.wav")
	

socre_font=pygame.font.Font(None,50)
score_text = socre_font.render("game over",True,(255,0,0))
score_rect = score_text.get_rect()
score_rect.centerx = 150
score_rect.centery = 90

socre_font2=pygame.font.Font(None,33)
score_text2= socre_font2.render("you win",True,(255,0,0))
score_rect2 = score_text2.get_rect()
score_rect2.centerx = 150
score_rect2.centery = 90 
#screen.blit(score_text,score_rect) 
direction1 = 'right1'
direction2 = 'right2'
direction3='right3'
while True: # the main game loop
	hit.play()
	DISPLAYSURF.fill(WHITE)
	for event in pygame.event.get():
		if event.type == QUIT:
			
			pygame.quit()
			sys.exit()
	#part1
	DISPLAYSURF.blit(background, (0, 0))	
	if direction1 == 'right1':
		speed1=[+3,0]
		if position.right >400:
			direction1 = 'left1'
	elif direction1 == 'left1':
		speed1=[-3,0]
		if position.left <0:
			direction1='right1'
			
	#part 2
	if direction2 == 'right2':
		badrect.right=catx2
		badrect.bottom=caty2
		catx2+=4
		if catx2>400:
			direction2 = 'left2'
	elif direction2 == 'left2':
		badrect.right=catx2
		catx2-=4
		if badrect.right<0:		
			direction2 = 'right2'
	#part 3
	if direction3 == 'right3':
		badrect1.right=catx3
		badrect1.bottom=caty3
		catx3 += 5
		if catx3>400:
			direction3 = 'left3'
	elif direction3 == 'left3':
		badrect1.right=catx3
		catx3 -=5
		if badrect1.right<0:
			direction3='right3'		
	pressed_keys = pygame.key.get_pressed()
	if pressed_keys[K_LEFT]:
		x-=5
		# if position.collidepoint(x,y):
  # 			speed1=[0,0]
  #           #catx2,caty2=90,90
  #   		direction2='top'
    		
  #   		direction3='top'	
	elif pressed_keys[K_RIGHT]:
		x+=5
		# if position.collidepoint(x,y):
 		# 	speed1=[0,0]
   #          #catx2,caty2=90,90
			# direction2='top'
			# direction1='top'
			# direction3='top'	
	if pressed_keys[K_UP]:
		y-=5
		# if position.collidepoint(x,y):
		# 	speed1=[0,0]
  #           #catx2,caty2=90,90
		# 	direction2='top'
		# 	direction1='top'
		# 	direction3='top'	
	elif pressed_keys[K_DOWN]:
		y+=5
		# if position.collidepoint(x,y):
		# 	speed1=[0,0]
  #           #catx2,caty2=90,90
		# 	direction2='top'
		# 	direction1='top'
		# 	direction3='top'
	if pressed_keys[K_f]:
		DISPLAYSURF = pygame.display.set_mode((400, 300), FULLSCREEN, 32)
	if 	pressed_keys[K_e]:
		DISPLAYSURF = pygame.display.set_mode((400, 300),0, 32)
			
	if y<0:	
	 		DISPLAYSURF.blit(score_text2,score_rect2)
			
			x=184
	 		y=280
					
	if position.collidepoint(x,y)or badrect.collidepoint(x,y) or badrect1.collidepoint(x,y):
            DISPLAYSURF.blit(score_text,score_rect)
            
            speed1=[0,0]
            #catx2,caty2=90,90
            direction2='top'
            direction1='top'
            direction3='top'
            hit.stop()

	# if badrect.collidepoint(x,y):
 #            DISPLAYSURF.blit(score_text,score_rect) 
 #            speed1=[0,0]
 #            #catx2,caty2=90,90
 #            direction2='top'
 #            direction1='top'
 #            direction3='top'
	# if badrect1.collidepoint(x,y):
 #            DISPLAYSURF.blit(score_text,score_rect) 
 #            speed1=[0,0]
 #            #catx2,caty2=90,90
 #            direction2='top'
 #            direction1='top'
 #            direction3='top'        


    
		#DISPLAYSURF.blit(score_text1,score_rect1)        

	position=position.move (speed1)
	#position2=position2.move (catx2,caty2)       
	#position=position.move (catx1,caty1)	
	DISPLAYSURF.blit(catImg2,badrect)											
	#DISPLAYSURF.blit(position, (catx1, caty1))
	DISPLAYSURF.blit(catImg1, position)
	
	DISPLAYSURF.blit(catImg3, badrect1)
	DISPLAYSURF.blit(catImg4, (x,y))					
	pygame.display.update()	
	fpsClock.tick(FPS)

					
