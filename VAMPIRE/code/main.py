# Import all settings defined in the settings.py file
from settings import *
from player import Player
from sprites import *

from random import randint

# Define the Game class to encapsulate the game's functionality
class Game:
    def __init__(self):
        # Initialize all pygame modules
        pygame.init()


        # --- SETUP ------
        # Create a display surface with the specified window dimensions
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # Set the title of the game window
        pygame.display.set_caption('Survivor')
        # Create a clock to manage the game's frame rate
        self.clock = pygame.time.Clock()
        # Initialize a running flag to control the game loop
        self.running = True
        # --- SETUP ------

        # GROUPS
        # group 1
        self.all_sprites = pygame.sprite.Group()
        # blue cube instances
        # group 2
        self.collision_sprites = pygame.sprite.Group()

        # SPRITES
        # player
        # This line below creates an instance of the Player class and adds it to the self.all_sprites group, allowing it to be managed alongside all game objects.
        self.player = Player((400, 300), self.all_sprites, self.collision_sprites)

        # random blue cubes
        for i in range(6):
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)

            # Random width and height for the cubes
            w, h = randint(60, 100), randint(50, 100)  # Different sizes each time

            # Create a collision sprite
            CollisionsSprite((x, y), (w, h), (self.all_sprites, self.collision_sprites))
            # By passing self.collision_sprites as an argument, the player gains access to the collision detection logic without being a direct member of that group. This allows the player to check for potential collisions with other sprites while not being included in the collision checks themselves.




    def run(self):
        # Main game loop that runs while the game is active
        while self.running:
            # Calculate the time since the last frame (in seconds)
            dt = self.clock.tick() / 1000

            # Handle events, such as user inputs and window actions
            for event in pygame.event.get():
                # Check if the user wants to quit the game
                if event.type == pygame.QUIT:
                    self.running = False  # Set running to False to exit the loop

            # Update game state (placeholder for future updates)
            self.all_sprites.update(dt)

            # -- DRAW --
            # Draw the current frame to the display
            self.display_surface.fill("black")
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()

        # Quit all pygame modules when the game loop ends
        pygame.quit()

# Check if this script is being run directly (not imported)
if __name__ == '__main__':
    # Create an instance of the Game class
    game = Game()
    # Start the game loop
    game.run()
