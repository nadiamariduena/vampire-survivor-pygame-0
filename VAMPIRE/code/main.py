# Import all settings defined in the settings.py file
from settings import *
from player import Player
from sprites import *

from pytmx.util_pygame import load_pygame


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

        self.setup()

        # SPRITES
        # player
        # This line below creates an instance of the Player class and adds it to the self.all_sprites group, allowing it to be managed alongside all game objects.
        self.player = Player((500, 300), self.all_sprites, self.collision_sprites)

        # random blue cubes
        # - here
        # Previously, we used a loop to create six random cubes on the screen with different sizes. Now, we’ll replace those cubes with the Objects from our TMX file. This means we’ll use actual game elements like trees and rocks instead of placeholder graphics.


    def setup(self):
        map = load_pygame(join('../data', 'maps', 'world.tmx'))
        # importing the trees
        for x,y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x * TILE_SIZE,y * TILE_SIZE), image, self.all_sprites)
            print(f"Sprite position: {x * TILE_SIZE}, {y * TILE_SIZE}")

        for obj in map.get_layer_by_name('Objects'):
            CollisionsSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))
        # importing the LAYER/plane/GROUND

        for obj in map.get_layer_by_name('Collisions'):
            # print(obj.image)
            CollisionsSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites )






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

        # Draw the player with the border (BORDERS)
            # self.player.draw(self.display_surface)

            pygame.display.update()

        # Quit all pygame modules when the game loop ends
        pygame.quit()

# Check if this script is being run directly (not imported)
if __name__ == '__main__':
    # Create an instance of the Game class
    game = Game()
    # Start the game loop
    game.run()
