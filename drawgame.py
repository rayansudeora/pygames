import pygame
pygame.init()
pygame.font.init()

#ISSUES:
#when pausing the square covers some text wherever it is
#still moves at beginning (black but still moves and takes out controls text)
#add boundaries

window_w = 500
window_h = 700
window = pygame.display.set_mode((window_w, window_h))#<--  #defining parameters for screen


dark_drawing = False
no_moving = False
popping = False


pygame.display.set_caption("Draw!")

#defining some colors:
WHITE = (255,255,255)
BLACK = (0,0,0)
DARK = (20,20,20)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GRAY =  (128,128,128)
MAROON = (128,0,0)
INDIGO = (75,0,130)
GOLD = (212, 175, 55)
PINK = (255, 113, 181)
color = BLACK

#attributes of our drawing square:
x=50
y=50 
width = 50
height = 50
vel = 5





font = pygame.font.SysFont('Arial', 70, bold=False, italic=False)


def message(msg, color, x, y):
	screen_text = font.render(msg, True, color)
	text_rect = screen_text.get_rect(center=(x, y))
	window.blit(screen_text, text_rect)

message("PRESS 'p' TO", RED, window_w/2, ((window_h/2)-50))
message("VIEW CONTROLS", RED, window_w/2, window_h/2)

'''
def pause():
	paused = True
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c: #if the user presses c, continue the drawing
					paused = False
'''

font = pygame.font.SysFont('Arial', 30, bold=False, italic=False)
def controls():
	message("CONTROLS: ", PINK, 250, 150)
	pygame.display.update()
	message("ARROW KEYS TO MOVE", GOLD, 250, 200)
	message("'p' TO PAUSE, 'c' TO CONTINUE", GOLD, 250, 250)
	message("SPACE BAR TO ERASE/MOVE WITHOUT DRAWING", GOLD, 250, 300)
	message("'r' FOR COLOR RED", GOLD, 250, 350)
	message("'b' FOR COLOR BLUE", GOLD, 250, 400)
	message("'w' FOR COLOR WHITE", GOLD, 250, 450)
	message("'y' FOR COLOR YELLOW", GOLD, 250, 500)
	message("'m' FOR COLOR MAROON", GOLD, 250, 550)
	message("'g' FOR COLOR GREEN", GOLD, 250, 600)
	message("'i' FOR COLOR INDIGO", GOLD, 250, 650)
	message("PRESS '1' TO START OR CLEAR", GOLD, 250, 100)
		

start = True
run = True
while run:
	keys = pygame.key.get_pressed()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if keys[pygame.K_p]:
			if start:
				window.fill(BLACK) 
				pygame.display.update()
				new_window = window.copy()
				controls()
				start = False
			else:
				new_window = window.copy()
				controls()
				no_moving = True
			
		if keys[pygame.K_c]:
			window.blit(new_window, (0,0))
			no_moving = False

		if keys[pygame.K_1] or keys[pygame.K_KP1]:
			window.fill(BLACK)
			pygame.display.update()
			no_moving = False






		


	#if keys[pygame.K_p]:
	#	pause() #if user presses p, run the pause function
	if keys[pygame.K_SPACE]:
		dark_drawing = True
		position = (x,y)
		pos = []
		pos.append(position)
		color = DARK



	if keys[pygame.K_LEFT] and not no_moving:
		x -= vel #if the left arrow key is pressed, move left
		position = (x,y)
		if dark_drawing:
			pos.append(position)
			popping = True
				
	if keys[pygame.K_RIGHT] and not no_moving:
		x += vel #if the right arrow key is pressed, move right
		position = (x,y)
		if dark_drawing:
			pos.append(position)
			popping = True
	if keys[pygame.K_UP] and not no_moving:
		y -= vel #if the up arrow key is pressed, move up
		position = (x,y)
		if dark_drawing:
			pos.append(position)
			popping = True
	if keys[pygame.K_DOWN] and not no_moving:
		y += vel #if the down arrow key is pressed, move down
		position = (x,y)
		if dark_drawing:
			pos.append(position)
			popping = True

	if keys[pygame.K_r]:
		dark_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = RED #if user presses 'r', make the drawing color red
			
	if keys[pygame.K_b]:
		dark_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = BLUE #if user presses 'b', make the drawing color blue

	if keys[pygame.K_w]:
		dark_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = WHITE #if user presses 'w', make the drawing color white

	if keys[pygame.K_y]:
		dark_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = YELLOW #if user presses 'y', make the drawing color yellow
		
	if keys[pygame.K_m]:
		dark_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = MAROON #if user presses 'm', make the drawing color maroon
		
	if keys[pygame.K_g]:
		dark_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = GREEN #if user presses 'g', make the drawing color green

	if keys[pygame.K_i]:
			dark_drawing = False
			while popping:
				pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
				pos.pop(0)
				if len(pos)==0:
					popping = False
			color = INDIGO #if user presses 'i', make the drawing color indigo

	pygame.draw.rect(window, color, (x, y, width, height)) #make drawing color red
	pygame.display.update()





pygame.quit()