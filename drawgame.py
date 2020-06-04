import pygame
pygame.init()
pygame.font.init()



window_w = 500
window_h = 700
window = pygame.display.set_mode((window_w, window_h))#<--  #defining parameters for screen


#defining boolean variables
dark_drawing = False
no_moving = False
popping = False
first_pause = False

#title of game
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
x=30
y=30 
width = 50
height = 50
vel = 5





font = pygame.font.SysFont('Arial', 70, bold=False, italic=False)#Our font (Arial, size 70)


def message(msg, color, x, y): #function which will take the text, color, and position
	screen_text = font.render(msg, True, color)
	text_rect = screen_text.get_rect(center=(x, y)) #rect for text
	window.blit(screen_text, text_rect)

message("PRESS 'p' TO", RED, window_w/2, ((window_h/2)-50))
message("VIEW CONTROLS", RED, window_w/2, window_h/2)


font = pygame.font.SysFont('Arial', 30, bold=False, italic=False)
def controls(): #display controls messages
	message("CONTROLS: ", PINK, window_w/2, window_h-550)
	message("ARROW KEYS TO MOVE", GOLD, window_w/2, window_h-500)
	message("'p' TO PAUSE, 'c' TO CONTINUE/UNDO", GOLD, window_w/2, window_h-450)
	message("SPACE BAR TO ERASE/MOVE WITHOUT DRAWING", GOLD, window_w/2, window_h-400)
	message("'r' FOR COLOR RED", GOLD, window_w/2, window_h-350)
	message("'b' FOR COLOR BLUE", GOLD, window_w/2, window_h-300)
	message("'w' FOR COLOR WHITE", GOLD, window_w/2, window_h-250)
	message("'y' FOR COLOR YELLOW", GOLD, window_w/2, window_h-200)
	message("'m' FOR COLOR MAROON", GOLD, window_w/2, window_h-150)
	message("'g' FOR COLOR GREEN", GOLD, window_w/2, window_h-100)
	message("'i' FOR COLOR INDIGO", GOLD, window_w/2, window_h-50)
	message("PRESS '1' TO START OR CLEAR", GOLD, window_w/2, window_h-600)
		

start = True
run = True
while run:
	keys = pygame.key.get_pressed()


	for event in pygame.event.get():
		if event.type == pygame.QUIT: #if user exits, end the code
			run = False
	
		if keys[pygame.K_p]: #if user presses p, pause the game
			if start: #if this is the initial time the user pressed 'p'
				first_pause = True
				no_moving = True
				window.fill(BLACK) #start the game
				pygame.display.update()
				new_window = window.copy()
				controls() #show controls to user
				start = False 
			else:
				no_moving = True #if this is any time but the initial time the user pressed 'p'
				color_before_pause = color #save the color
				color = BLACK #hide color
				paused_x = x #save x value
				paused_y = y #save y value
				x = window_w - (window_w*2) #take drawing square out of the screen
				y = window_h - (window_h*2)
				new_window = window.copy()
				controls() #show controls to user
					
				
		if keys[pygame.K_c]: #is user presses c, continue the game
			color = color_before_pause #make the drawing square the color it previously was
			window.blit(new_window, (0,0)) #return the screen to what it looked like before pausing
			x = paused_x #return x and y to where the drawing square was before pausing
			y = paused_y
			no_moving = False #allow movement

		if keys[pygame.K_1] or keys[pygame.K_KP1]:
			color_before_pause = color
			window.fill(BLACK) #clear screen
			pygame.display.update()
			x = 30 #reset position of drawing square
			y = 30
			no_moving = False #allow movement
			if first_pause:
				first_pause = False #allow user to choose a color
			else:
				color = color_before_pause #make the drawing square the color it previously was
			


	if keys[pygame.K_SPACE]:
		dark_drawing = True #allow user to move without drawing or erase
		pos = []
		pos.append(position) #keep list of movement so it can be erased
		color = DARK



	if keys[pygame.K_LEFT] and not no_moving and x>vel: #the user is allowed to move and must stay in the screen (boundary)
		x -= vel #if the left arrow key is pressed, move left
		position = (x,y)
		if dark_drawing:
			pos.append(position)
			popping = True
				
	if keys[pygame.K_RIGHT] and not no_moving and x < window_w-width-vel: #the user is allowed to move and must stay in the screen (boundary)
		x += vel #if the right arrow key is pressed, move right
		position = (x,y)
		if dark_drawing:
			pos.append(position)
			popping = True
	if keys[pygame.K_UP] and not no_moving and y>vel: #the user is allowed to move and must stay in the screen (boundary)
		y -= vel #if the up arrow key is pressed, move up
		position = (x,y)
		if dark_drawing:
			pos.append(position)
			popping = True
	if keys[pygame.K_DOWN] and not no_moving and y < window_h-height-vel: #the user is allowed to move and must stay in the screen (boundary)
		y += vel #if the down arrow key is pressed, move down
		position = (x,y)
		if dark_drawing:
			pos.append(position)
			popping = True

	if keys[pygame.K_r]:
		dark_drawing = False #not erasing, so save all movement
		while popping: #erase everywhere dark_drawing touched
			pygame.draw.rect(window, BLACK, (pos[0][0], pos[0][1], width, height))
			pos.pop(0)
			if len(pos)==0:#once the list of all positions is empty, stop erasing
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


	
	pygame.draw.rect(window, color, (x, y, width, height)) #draw rectangle
	pygame.display.update()





pygame.quit()