print("Welcome to the dungeon!")
	print("You're courrently in room {}".format(player_location)) # fill with player position
	print("You can move {}".format(get_moves(player_location))) # fill with available moves
	print("Enter QUIT to quit")

	choice = input("Would you like a SODA, some CHIPS, or a CANDY?").lower()