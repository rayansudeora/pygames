import pygame
pygame.init()
pygame.font.init()

#FIRST PRIORITY: Figure out how to switch between colors seamlessly
#SECOND PRIORITY: Space function

window_w = 500
window_h = 700
window = pygame.display.set_mode((window_w,window_h))#<--  #defining parameters for screen

redgame = False
bluegame = False
whitegame = False
yellowgame = False
maroongame = False
greengame = False
no_drawing = False
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
color = BLACK

#attributes of our drawing square:
x=50
y=50 
width = 50
height = 50
vel = 5

#font = pygame.font.SysFont('Arial', 100, bold=False, italic=False)
def message(msg, color):
	screen_text = font.render(msg, True, color)
	text_rect = screen_text.get_rect(center=(window_w/2, window_h/2))
	window.blit(screen_text, text_rect)


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
while no_drawing:
	pygame.draw.rect(window, BLACK, (x, y, width, height)) 
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				no_drawing = False
		if keys[pygame.K_LEFT]:
			x -= vel #if the left arrow key is pressed, move left
		if keys[pygame.K_RIGHT]:
			x += vel #if the right arrow key is pressed, move right
		if keys[pygame.K_UP]:
			y -= vel #if the up arrow key is pressed, move up
		if keys[pygame.K_DOWN]:
			y += vel #if the down arrow key is pressed, move down
'''

run = True
while run:
	pygame.time.delay(50)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	


	if keys[pygame.K_p]:
		pause() #if user presses p, run the pause function
	if keys[pygame.K_SPACE]:
		no_drawing = True
		position = (x,y)
		pos = []
		pos.append(position)
		color = DARK



	if keys[pygame.K_LEFT]:
		x -= vel #if the left arrow key is pressed, move left
		position = (x,y)
		if no_drawing:
			pos.append(position)
			popping = True
			
	if keys[pygame.K_RIGHT]:
		x += vel #if the right arrow key is pressed, move right
		position = (x,y)
		if no_drawing:
			pos.append(position)
			popping = True
	if keys[pygame.K_UP]:
		y -= vel #if the up arrow key is pressed, move up
		position = (x,y)
		if no_drawing:
			pos.append(position)
			popping = True
	if keys[pygame.K_DOWN]:
		y += vel #if the down arrow key is pressed, move down
		position = (x,y)
		if no_drawing:
			pos.append(position)
			popping = True

	if keys[pygame.K_r]:
		no_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = RED #if user presses 'r', make the drawing color red
		
	if keys[pygame.K_b]:
		no_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = BLUE #if user presses 'b', make the drawing color blue

	if keys[pygame.K_w]:
		no_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = WHITE #if user presses 'w', make the drawing color white

	if keys[pygame.K_y]:
		no_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = YELLOW #if user presses 'y', make the drawing color yellow
	
	if keys[pygame.K_m]:
		no_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = MAROON #if user presses 'm', make the drawing color maroon
	
	if keys[pygame.K_g]:
		no_drawing = False
		while popping:
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:
				popping = False
		color = GREEN #if user presses 'g', make the drawing color green


	pygame.draw.rect(window, color, (x, y, width, height)) #make drawing color red
	pygame.display.update()
	
	



pygame.quit()