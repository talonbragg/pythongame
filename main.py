import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((1000, 800), 0, 32)
pygame.display.set_caption('Game')


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 255)
GREEN = (0, 255, 0)
mousex = 0
mousey = 0

catImg = pygame.image.load('cat.png')
catx = 500
caty = 500

fontObj = pygame.font.Font('freesansbold.ttf', 32)
fontNum = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Levels Cleared:', True, GREEN, BLACK)
textSurfaceNum = fontObj.render('0', True, GREEN, BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectNum = textSurfaceNum.get_rect()
textRectObj.center = (75, 50)
textRectNum.center = (150, 50)

while True:
	mouseClicked = False
	
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	DISPLAYSURF.blit(textSurfaceNum, textRectNum)
	DISPLAYSURF.blit(catImg, (catx, caty))
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			catx, caty = event.pos
			points == '1'
	pygame.display.update()
