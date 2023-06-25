METEOR CRASH by Ricardo Almeida, a21807601

The planet's time has come to an end. An endless torrent of meteors will strike the Earth
and extinguish all life in it. As a turret gunner, your job is to buy Earth as much time
as possible by shooting down the meteors before they can strike. It is a hopeless mission
but one you must perform nonetheless. Best of luck!


HOW TO RUN:
	#1: Make sure you have Pygame installed (https://www.pygame.org/wiki/GettingStarted)
	#2: Run Main.py

HOW TO PLAY:
	Press W to jump.
	Press A to move left.
	Press D to move right.
	Press SPACE to fire.

	The bullets take into account your momentum so you can curve them by shooting
	while moving left or right, or fire them higher by doing so while jumping.


This project was made for the IMFJ2 class with the purpose of incorporating the knowledge
of physics accrued throughout the semester into a game by utilizing the correct formulas
in order to have a somewhat close-to-reality simulation of the physics in the game.

PROJECT ARCHITECTURE:
	The game begins by declaring every necessary variable and relevant component.
	Next, it starts a Try Except which begins a Main Menu loop where it awaits the
	player's input to raise an Exception whill will trigger the Except and end the loop.
	Afterwards the Main Game loop will begin and it begins by making sure that there are
	always 6 meteors in game at any point. It then checks if the player is grounded to make
	sure that it handles the inputs well in gameplay's Input Manager which is called right
	after. After the input has been handled, it checks the walls to see if the player's
	input is possible to be taken into account. After this has been handled, the player's
	position is updated via the Move method. The same is then done for every bullet and meteor.
	It then checks if any meteor struck the ground, if it did, it starts the End Menu. If it
	hasn't, it sees if any meteor is in contact with a bullet so it can remove both and increase
	the player's score. Once this has been completed, it renders to the screen the background,
	then it renders the player, the bullets and the meteors by this order. Finally it flips the
	display and locks the loop to a 60 FPS framerate before starting the Main Game loop again.


REFERENCES:
	- Pygame Documentation: https://www.pygame.org/docs/
	- W3Schools: https://www.w3schools.com/python/default.asp
	- IMFJ2's GitHub: https://github.com/virtualeiro/pygame-imfvj2
	- IMFJ2's Powerpoints


Music is from the 1994's System Shock: https://youtu.be/AIMDilzrFjc