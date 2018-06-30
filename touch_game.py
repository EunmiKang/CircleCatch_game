# -*- coding: utf-8 -*-

import sys
import numpy as np
import random
import pygame
from pygame import *
from pygame.locals import *
from pygame.draw import *
import threading
import time

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

color = [red, green, blue]
p = 30.00
score = 0

class Circle:
	score = 0
	def __init__(self):
		pass

	def __del__(self):
		pass

	def draw_circle(self):
		x = random.randrange(30, 471)
		y = random.randrange(30, 471)
		chosenColor = random.choice(color)
		circleObj = circle(screen, chosenColor, (x, y), 30, 5)
		pygame.display.update()
		a = time.time()
		t = threading.Timer(0.50, self.draw_circle)
			
		if a > startTime + p:
			t.cancel()
			print "Game Over"
		else :	
			t.start()
			deleteTime = time.time()
			self.thread_remove_circle(x, y, deleteTime, chosenColor)

	def thread_remove_circle(self, x, y, deleteTime, chosenColor):
		t = threading.Timer(0, self.remove_circle, [x, y, deleteTime, chosenColor])
		t.start()

	def remove_circle(self, x, y, deleteTime, chosenColor):
		global score
		deleteP = 1.45
		delete = False
		while not delete:
			n = time.time()
			if n > deleteTime + deleteP: 
				circle(screen, black, (x, y), 30, 5)
				pygame.display.update()
				#print "time over delete"
				delete = True
			else:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					# 입력부분 - 마우스 버튼 클릭
					elif event.type == MOUSEBUTTONDOWN:
						mouse_pos = pygame.mouse.get_pos()
						gap_x = abs(mouse_pos[0] - x)
						gap_y = abs(mouse_pos[1] - y)
						if gap_x<=30 and gap_y<=30:
							circle(screen, black, (x, y), 30, 5)
							pygame.display.update()
							if chosenColor == color[0]:	#red
								print "red circle touch! (-5)"
								score -= 5
							elif chosenColor == color[1]:	#green
								print "green circle touch! (+10)"
								score += 10 
							elif chosenColor == color[2]:	#blue
								print "blue circle touch! (+20)"
								score += 20
							print "< score:", score, " >"
							delete = True


# Main

pygame.init()
screen = pygame.display.set_mode((500, 500), RESIZABLE)
pygame.display.set_caption('project1: touch circle')

c = Circle()
startTime = time.time()
c.draw_circle()

