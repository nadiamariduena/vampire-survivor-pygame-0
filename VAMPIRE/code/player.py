from settings import *
# the settings contains the width & height


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join("../images", "player", "down", "0.png" )).convert_alpha()

        self.rect = self.image.get_frect(center = pos)

        self.hitbox_rect = self.rect.inflate(-60, 0)


        # ----- MOVEMENT ---------
        # This vector will store the direction in which the player is moving.
        # It helps determine the player's movement by setting the x and y components.
        self.direction = pygame.Vector2()

        # The speed of the player, defining how fast it moves in pixels per second.
        # A higher value means the player will move faster across the screen.
        self.speed = 500

        # Store the collision sprites so the player can check for collisions with them.
        # This will help manage collision detection during movement.
        self.collision_sprites = collision_sprites


    def input(self):
         keys = pygame.key.get_pressed()
         self.direction.x = int(keys[pygame.K_RIGHT]) - int((keys[pygame.K_LEFT]))
         self.direction.y = int(keys[pygame.K_DOWN]) - int((keys[pygame.K_UP]))


        # This line means: "If we already have a direction (like up, down, left, or right), then normalize it. If we don’t have a direction yet, just keep it the way it is."
         self.direction = self.direction.normalize() if self.direction  else self.direction




    def move(self,dt):
        #self.rect.center += self.direction * self.speed * dt # before
        # self.rect.x += self.direction.x * self.speed * dt
        # self.rect.y += self.direction.y * self.speed * dt

        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')

        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

        self.rect.center = self.hitbox_rect.center

    #  (BORDERS) ----------
    # def draw(self, surface):
    #     # Draw the player image
    #     surface.blit(self.image, self.rect.topleft)

    # # Draw the yellow border around the rect
    #     border_rect = self.rect.inflate(2, 2)  # Inflate by 2 pixels for the border
    #     pygame.draw.rect(surface, (255, 255, 0), border_rect, 1)  # Yellow border for the rect

    #     # Draw the hitbox rectangle in red for visibility
    #     pygame.draw.rect(surface, (255, 0, 0), self.hitbox_rect, 1)  # Red for the hitbox
    #  (BORDERS) ----------

    def collision(self, direction):
        # Here, we start a loop that goes through each obstacle (sprite) in the 'collision_sprites' group. This group contains all the objects we want to check for collisions with.
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                #This line checks if the player's rectangle (self.rect) overlaps with the rectangle of the current sprite. The colliderect function returns True if there is any overlap.
                # print("pverlap")
             if direction == 'horizontal':
                # Check if the player is moving to the right
                if self.direction.x > 0:
                    # If so, set the player's right side to the left side of the obstacle
                    self.hitbox_rect.right = sprite.rect.left

                # Check if the player is moving to the left
                if self.direction.x < 0:
                    # If so, set the player's left side to the right side of the obstacle
                    self.hitbox_rect.left = sprite.rect.right
             else:
                if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom
                if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top


    def update(self, dt):
        self.input()
        self.move(dt)