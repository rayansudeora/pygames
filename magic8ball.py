import pygame
import random
#import time
import sys
pygame.init()
pygame.font.init()
keys = pygame.key.get_pressed()


window_w = 700
window_h = 750

window = pygame.display.set_mode((window_w, window_h))#<--  #defining parameters for screen
pygame.display.update()
clear_window = window.copy()

game_on = False
after_attempt = False

pygame.display.set_caption("Magic 8 Ball")

WHITE = (255,255,255)
BLACK = (0,0,0)
DARK = (20,20,20)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GRAY =  (128,128,128)
LIGHT = (235, 235, 235)
MAROON = (128,0,0)
PURPLE = (75,0,130)
GOLD = (212, 175, 55)
PINK = (255, 113, 181)


font = pygame.font.SysFont('Arial', 53, bold=False, italic=False)#Our font (Arial, size 70)

def message(msg, color, x, y): #function which will take the text, color, and position
	screen_text = font.render(msg, True, color)
	text_rect = screen_text.get_rect(center=(x, y)) #rect for text
	window.blit(screen_text, text_rect)

def magicball():
	num = random.randint(1,20)
	if num==1:
		response = pygame.image.load('magic8ballimages/as_i_see_it.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==2:
		response = pygame.image.load('magic8ballimages/ask_again_later.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==3:
		response = pygame.image.load('magic8ballimages/cannot_predict.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==4:
		response = pygame.image.load('magic8ballimages/concentrate.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==5:
		response = pygame.image.load('magic8ballimages/it_is_decidedly.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==6:
		response = pygame.image.load('magic8ballimages/do_not_count.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==7:
		response = pygame.image.load('magic8ballimages/it_is_certain.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==8:
		response = pygame.image.load('magic8ballimages/most_likely.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==9:
		response = pygame.image.load('magic8ballimages/my_reply_no.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==10:
		response = pygame.image.load('magic8ballimages/not_tell_now.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==11:
		response = pygame.image.load('magic8ballimages/outlook_good.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==12:
		response = pygame.image.load('magic8ballimages/outlook_not_good.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==13:
		response = pygame.image.load('magic8ballimages/rely_on_it.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==14:
		response = pygame.image.load('magic8ballimages/reply_hazy.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==15:
		response = pygame.image.load('magic8ballimages/signs_point.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==16:
		response = pygame.image.load('magic8ballimages/sources_say_no.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==17:
		response = pygame.image.load('magic8ballimages/very_doubtful.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==18:
		response = pygame.image.load('magic8ballimages/without_doubt.png')
		window.blit(response, (40,20))
		pygame.display.update()
	elif num==19:
		response = pygame.image.load('magic8ballimages/yes_definitely.png')
		window.blit(response, (40,20))
		pygame.display.update()
	else:
		response = pygame.image.load('magic8ballimages/yes.png')
		window.blit(response, (40,20))
		pygame.display.update()

def fade(width, height): 
	fade = pygame.Surface((width, height))
	fade.fill((0,0,0))
	opacity = 0
	for r in range(0, 300):
		opacity += 1
		fade.set_alpha(opacity)
		window.fill(BLACK)
		window.blit(fade, (0,0))
		pygame.display.update()
	pygame.time.delay(200)
	for r in range(0, 300):
		opacity -= 1
		fade.set_alpha(opacity)
		window.fill(BLACK)
		window.blit(fade, (0,0))
		pygame.display.update()


message("MAGIC 8 BALL", MAROON, window_w/2, window_h/10)
message("PRESS 1 TO BEGIN", GOLD, window_w/2, window_h/2)




pygame.display.update()

start = True
run = True
while run:
	vel = 5
	ball_x = 58
	ball_y = 40
	keys = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #if user exits, end the code
			run = False
		if keys[pygame.K_1] or keys[pygame.K_KP1] and start:
			window.blit(clear_window, (0,0))
			window.fill(LIGHT)
			

			user_q = ''
			while user_q == '':
				user_q = input("\n \n \nASK YOUR QUESTION: ")

			ball = pygame.image.load('magic8ballimages/magic_8_ball.png')
			window.blit(ball, (ball_x, ball_y))




			font = pygame.font.SysFont('Arial', 30, bold=False, italic=False)#Our font (Arial, size 70)
			message("PRESS SPACE TO RECEIVE YOUR ANSWER", BLUE, window_w/2, window_h/14)
			message("PRESS 1 TO ASK ANOTHER QUESTION!", PURPLE, window_w/2, window_h-50)
			msg_window = window.copy()
			pygame.display.update()
			game_on = True
			start = False

				

	if game_on:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					print("ASKING 8 BALL: ")
					dots = [".","..", "...", "....", ".....", "......", ".......", "........", ".........", ".........."]
					for d in range(len(dots)):
					    pygame.time.delay(200)
					    sys.stdout.write("\r" + dots[d % len(dots)])
					    sys.stdout.flush()
					print("\n")

					window.blit(msg_window, (0,0))
					magicball()
					game_on = False








pygame.quit()