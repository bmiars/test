import random
import os




#draw playin in the grid

#take input for movement

#move player, unless invalid move (past edges of grid)

#check for win/loss

#clear screen and redraw grid


# draw a grid
CELLS = [(0,0),(1,0),(2,0),(3,0),(4,0),
		(0,1),(1,1),(2,1),(3,1),(4,1),
		(0,2),(1,2),(2,2),(3,2),(4,2),
		(0,3),(1,3),(2,3),(3,3),(4,3),
		(0,4),(1,4),(2,4),(3,4),(4,4)]

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
#pick random location for player
#pick random location for exit door
#pick random location for monster


def get_locations():
	return random.sample(CELLS, 3)

def move_player(player, move):
	# get player location
	
	if move == "LEFT":
		player = player[0]-1, player[1]
		
	if move == "RIGHT":
		player = player[0]+1, player[1]
		
	if move == "UP":
		player = player[0], player[1]-1
		
	if move == "DOWN":
		player = player[0], player[1]+1
		
	
	return player

def get_moves(player):
	moves = ["LEFT", "RIGHT", "UP", "DOWN"]
	# if player's y == 0, they can't move up
	if player[1] == 0:
		moves.remove("UP")
	# if player's y == 4, they cant move down
	if player[1] == 4:
		moves.remove("DOWN") 
	# if players x == 0, they cant move left
	if player[0] == 0:
		moves.remove("LEFT") 
	# if players x ==4, they cant move right
	if player[0] == 4:
		moves.remove("RIGHT") 
	
	return moves

def draw_map(player, monster):
	print(player)
	print(" _"*5)
	title = "|{}"

	for cell in CELLS:
		x, y = cell
		if x < 4:
			line_end = ""

			if cell == player:
				output = title.format("X")

			elif cell == monster:
				output = title.format("M")

			else:
				output = title.format("_")
		else:
			line_end = "\n"
			

			if cell == monster:
				output = title.format("M|")


			elif cell == player:
				#print("player check fired")
				output = title.format("X|")
			

			else: 
				output = title.format("_|")
		print(output, end=line_end)

def game_loop():
	monster, door, player_location = get_locations()
	playing = True

	while playing:
		clear_screen()
		draw_map(player_location, monster)

		print("You're courrently in room {}".format(player_location)) # fill with player position
		print("The monster is in room {}".format(monster))
		print("You can move {}".format(get_moves(player_location))) # fill with available moves
		print("Enter QUIT to quit")

		move = input("> ")
		
		move = [move.upper()]
		
		
		if move[0] == 'QUIT':
			break

		#Good move? Change the plaer posisition
		if set(move) <= set(get_moves(player_location)):
			
			#once player insterts move choice, run the move function and update the location
			
			player_location = move_player(player_location, move[0])
			
			moves = ["LEFT", "RIGHT", "UP", "DOWN"]
			monster_choice = random.sample(moves, 1)
			
			print(monster_choice)
			if set(monster_choice) <= set(get_moves(monster)):
				
				monster = move_player(monster, monster_choice[0])
				
				print(monster)
			


		#Bad move? Don't change anything!
		else:
			
			input("Sorry, that wasn't a valid move!")
			
		
		#On the door? They win!

		if player_location == door:
			print("You win!")

			playing = False
			
		#On the monster? They lose!
		if player_location == monster:
			print("The monster done gobbled you up!")
			print("You lose!")
			
			playing = False
		else:
			continue
	else: 
		if input("Play again? [Y/n]").lower() != "n":
			game_loop()


# set the locations








clear_screen()
print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()
	
	#Otherwise, loop back around
