#!/usr/bin/python
import os, sys, pygame
import fontutil
from pygame.locals import *

if not pygame.font: print "Warning, fonts disabled"

class Bubble(object):

	def __init__(self, text=None, font=None, fontcolor=None, backgroundcolor=None, bordercolor=None):
		if not text:
			text = ("Hello World!\nThis is another line\n");
		if not font:		
			font = pygame.font.Font(None, 36)
		if not fontcolor:
			fontcolor = (255, 0, 0)
		if not backgroundcolor:
			backgroundcolor = (255, 255, 255)
		if not bordercolor:
			bordercolor = (0, 0, 0)
		
		self.backgroundcolor = backgroundcolor
		self.bordercolor = bordercolor	
		self.textsurface = fontutil.rendertext(text, font, fontcolor, backgroundcolor)
		self.move((0, 0))

	def move(self, (left, top)):
		self.bubblepolygon = []
		if not left:
			left = 50
		if not top:
			top = 50

		self.textpos = Rect(left, top, self.textsurface.get_width(), self.textsurface.get_height())
		bubblerect = self.textpos.inflate(20,10)
		self.bubblepolygon.append(bubblerect.topleft)
		self.bubblepolygon.append(bubblerect.topright)
		self.bubblepolygon.append(bubblerect.bottomright)
		self.bubblepolygon.append((bubblerect.left+30, bubblerect.bottom))
		self.bubblepolygon.append((bubblerect.left, bubblerect.bottom+20))
		self.bubblepolygon.append((bubblerect.left+10, bubblerect.bottom))
		self.bubblepolygon.append(bubblerect.bottomleft)
		self.bubblepolygon.append(bubblerect.topleft)

	def render(self, surface):
		if not surface:
			print "Warning, no surface defined"
		pygame.draw.polygon(surface, self.backgroundcolor, self.bubblepolygon, 0)
		pygame.draw.polygon(surface, self.bordercolor, self.bubblepolygon, 2)
		surface.blit(self.textsurface, self.textpos)	

