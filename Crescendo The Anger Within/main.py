# Source code for the game 'Crescendo the anger within'

# Made by Adam Wareshallee and is under the GNU General Public License v3.0 (GPLv3).

###############################################################################################################################################
# Libaries to be used in my game 'Crescendo the anger within' 
# (1) Importing the random libary libary (for the enemy).
# (2) Importing the pygame libary in order to display a window and enables the spirtes to move and essentially allow the whole game to function.
# (3) Importing OS libery to allow the background to display on the pygame window.
# (4) Initialisng pygame to start up all imported pygame modules needed for the game.   

import random #(1)
import pygame #(2)
import os #(3)
pygame.init() #(4)
pygame.mixer.init()  # Initialize mixer for audio
font = pygame.font.Font(None, 36)
################################################################################################################################################
# Setting the display resolution and title of the game
# (1) How high the display is .
# (2) How wide the display should be.
# (3) Game's title


DisplayOUTPUT = pygame.display.set_mode((1200, 800)) # (1) How high the display is and (2) How wide the display should be
GameTitle = pygame.display.set_caption("Crescendo the anger within") # (3) Game's title
clock = pygame.time.Clock()
################################################################################################################################################
# Animation for Adam the defender 

# Idle animation for Adam the defender
Idle_AdamTheDefender = [pygame.image.load("Idle1.png"),
            pygame.image.load("Idle2.png"),
            pygame.image.load("Idle3.png"),
            pygame.image.load("Idle4.png"),
            pygame.image.load("Idle5.png"),
            pygame.image.load("Idle6.png"),
            pygame.image.load("Idle7.png"),
            pygame.image.load("Idle8.png"),
            pygame.image.load("Idle9.png"),
            pygame.image.load("Idle10.png"),
            pygame.image.load("Idle11.png")]
            

# Right animation (base animation)
right_AdamTheDefender =  [pygame.image.load("WRR1.png"),
         pygame.image.load("WRR2.png"),
         pygame.image.load("WRR3.png"),
         pygame.image.load("WRR4.png"),
         pygame.image.load("WRR5.png"),
         pygame.image.load("WRR6.png"),
         pygame.image.load("WRR7.png"),
         pygame.image.load("WRR8.png"),
         pygame.image.load("WRR9.png"),
         pygame.image.load("WRR10.png"),
         pygame.image.load("WRR11.png")]

# Left animation (flipped version of right animation)
left_AdamTheDefender = [pygame.transform.flip(img, True, False) for img in right_AdamTheDefender]
################################################################################################################################################
# Animation for Flapberry Fudgewhistle (the enemy)

# Load and scale base enemy images
left_FlapberryFudgewhistle = [pygame.transform.scale(pygame.image.load(f"EW{i}.png"), (int(pygame.image.load(f"EW{i}.png").get_width() * 0.5), int(pygame.image.load(f"EW{i}.png").get_height() * 0.5))) for i in range(1,10)]

# Right animation (flipped version of left animation)
right_FlapberryFudgewhistle = [pygame.transform.flip(img, True, False) for img in left_FlapberryFudgewhistle]

################################################################################################################################################
# Displaying the background and using the os libary to allow the background to display on the pygame window
# (1) Ask sir why it says error when i remove os.path.join.
# (2) Ask sir for the same for bullets as well. 

Display_background = pygame.transform.scale(pygame.image.load(os.path.join("Background.png")), (1200, 800)) # (1) try to not use win_width or win_height
bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("RageBullets.png")), (10, 10)) # (2)

# Load sound effects
zombie_sound = pygame.mixer.Sound(os.path.join("sounds", "zombie.mp3"))
zombie_dead_sound = pygame.mixer.Sound(os.path.join("sounds", "zombie-dead.mp3"))
gun_shot_sound = pygame.mixer.Sound(os.path.join("sounds", "gun-shot.mp3"))
game_over_sound = pygame.mixer.Sound(os.path.join("sounds", "game-over.mp3"))
jump_sound = pygame.mixer.Sound(os.path.join("sounds", "jump.mp3"))
jump_sound.set_volume(0.3) # Reduce volume so its not too loud
cinematic_hit_sound = pygame.mixer.Sound(os.path.join("sounds", "cinematic-hit.mp3"))
walking_sound = pygame.mixer.Sound(os.path.join("sounds", "loud-footsteps.mp3"))
walking_sound.set_volume(1.0)  # Set volume to maximum
################################################################################################################################################
# Class for Adam the defender (research later)
# (1) Jumping animation for the defender (it allows the Loyal defender object to have the attribute jump) - research later
# (2) Bullet animation for the defender
# (3) Move_hero - find out what it is
# (4) def draw - find out what it is

class AdamTheDefender:
     def __init__(self, x, y, ):
        self.x = x #research this
        self.y = y
        self.Impetusx = 10 #represents the velocity of AdamTheDefender along the x-axis. Find out how to increase speed.
        self.Impetusy = 10
        self.face_right = True
        self.face_left = False
        self.jump = False # (1)
        self.bullets = [] # (2) If removed ('int' object has no attribute 'move') - Find out why!
        self.hitbox = (self.x, self.y, 300, 290)
        self.StepDirectory = 0  # Initialize here to avoid attribute error

     #(3)
     def move_AdamTheDefender(self, userInput):
        moving = False
        if userInput[pygame.K_RIGHT] and self.x <= 1100: # The self.x <= 1100 controls the border for AdamTheDefender on the right side of the screen (x).
           self.x += self.Impetusx # This allows AdamTheDefender to move to the right with the '+'.
           self.face_right = True # This allows the right animation to operate when the right key is pressed
           self.face_left = False # This allows the left animation to not operate when the right key is pressed
           moving = True
        elif userInput[pygame.K_LEFT] and self.x >= 0: # The self.x <= 0 controls the border for AdamTheDefender on the left side of the screen (x).
           self.x -= self.Impetusx # This allows AdamTheDefender to move to the left with the '-'.
           self.face_right = False #This allows the right animation to not operate when the left key is pressed
           self.face_left = True #This allows the left animation to operate when the left key is pressed
           moving = True
        else:
           self.StepDirectory = 0 # If removed it gives a attribute error that AdamTheDefender object has no attribute 'stepIndex

        # Handle walking sound
        if moving and not pygame.mixer.get_busy():
           walking_sound.play(-1)  # Loop walking sound when moving
        elif not moving:
           walking_sound.stop()  # Stop walking sound when not moving

     # (4)
     def draw(self, DisplayOUTPUT): # What is draw
       self.hitbox = (self.x + 15, self.y + 0, 120, 200)
       # pygame.draw.rect(DisplayOUTPUT, (0,255,0), self.hitbox, 2)  # Debug: Uncomment to see hitbox
       if self.StepDirectory >= 9:
           self.StepDirectory = 0
       if self.face_left:
           DisplayOUTPUT.blit(left_AdamTheDefender[self.StepDirectory], (self.x, self.y)) # find out what is blit
           self.StepDirectory += 1
       if self.face_right:
           DisplayOUTPUT.blit(right_AdamTheDefender[self.StepDirectory], (self.x, self.y))
           self.StepDirectory += 1

     # (5)
     def jump_motion (self, userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
           self.jump = True
           jump_sound.play()  # Play jump sound when jumping
        if self.jump:
           self.y -= self.Impetusy*5 # THis also changes how high the defender jumps
           self.Impetusy -= 1 # This if set 10 for some reason makes him stop jumping
        if self.Impetusy < -10:
           self.jump = False
           self.Impetusy = 10 # This changes how high the defender jump
           
     def direction(self): # Without this the class for adam doesnt work - try and implement this into the Adam class
        if self.face_right:
            return 1
        if self.face_left:
            return -1
       
     # (6)
     def shoot(self, userInput):
        if userInput[pygame.K_f]:
           bullet = Bullet(self.x, self.y, self.direction())
           self.bullets.append(bullet)
           gun_shot_sound.play()  # Play gun shot sound when shooting
        for bullet in self.bullets:
           bullet.move()
################################################################################################################################################
# Class for the bullets
class Bullet:
    def __init__(self, x, y, direction):
        # Adjust bullet spawn position based on player facing direction
        # Player width is approximately 120 (from hitbox)
        if direction == 1:  # Facing right
            self.x = x + 120  # Spawn from right side, slightly further out
        elif direction == -1:  # Facing left
            self.x = x  # Spawn from left side, aligned with player left edge
        self.y = y + 120  # Keep vertical position the same (shoulder level)
        self.direction = direction

    def draw_bullet(self):
        DisplayOUTPUT.blit(bullet_img, (self.x, self.y)) # Renmeber to show controls to the user maybe by using a pop up or a menu 

    def move(self):
        if self.direction == 1:
            self.x += 30
        if self.direction == -1:
            self.x -= 30
    
    def off_screen(self):
        return not(self.x >= -1 and self.x <= 1200 + 1)
################################################################################################################################################
# Class for the enemy (Flapberry Fudgewhistle) - FIXED VERSION
class Enemy:
    def __init__(self, x, y, direction):
        self.x = x
        # Match player's ground level (player is at Y=290, which seems to be the ground)
        self.y = 250  # Adjusted to match the ground in your background
        self.direction = direction  # 1 for right, -1 for left
        self.StepDirectory = 0
        # Get actual sprite dimensions for hitbox
        sprite_width = left_FlapberryFudgewhistle[0].get_width()
        sprite_height = left_FlapberryFudgewhistle[0].get_height()
        self.hitbox = (self.x, self.y, sprite_width, sprite_height)

    def step(self):
        if self.StepDirectory >= 33:
            self.StepDirectory = 0

    def draw(self, DisplayOUTPUT):
        self.step()
        # Determine which way enemy should face based on player position
        if player.x < self.x:
            # Player is to the left, so enemy should face right (towards player)
            DisplayOUTPUT.blit(right_FlapberryFudgewhistle[self.StepDirectory//4], (self.x, self.y))
        else:
            # Player is to the right, so enemy should face left (towards player)
            DisplayOUTPUT.blit(left_FlapberryFudgewhistle[self.StepDirectory // 4], (self.x, self.y))
        self.StepDirectory += 1
        
        # Update hitbox to match sprite size
        sprite_width = left_FlapberryFudgewhistle[0].get_width()
        sprite_height = left_FlapberryFudgewhistle[0].get_height()
        self.hitbox = (self.x, self.y, sprite_width, sprite_height)
        
        # Debug: Draw hitbox (uncomment to see collision box)
        # pygame.draw.rect(DisplayOUTPUT, (255, 0, 0), self.hitbox, 2)

    def move(self):
        # Move towards the player
        if player.x < self.x:
            self.x -= 3  # Move left towards player
            self.direction = -1  # Facing left
        elif player.x > self.x:
            self.x += 3  # Move right towards player
            self.direction = 1  # Facing right

        # Update hitbox position
        sprite_width = left_FlapberryFudgewhistle[0].get_width()
        sprite_height = left_FlapberryFudgewhistle[0].get_height()
        self.hitbox = (self.x, self.y, sprite_width, sprite_height)

        # Play zombie sound when moving towards player (only if not already playing to avoid spam)
        if not pygame.mixer.get_busy():
            zombie_sound.play(-1)  # Loop the zombie sound

        # Check if enemy reached player (game over condition)
        player_rect = pygame.Rect(player.hitbox)
        enemy_rect = pygame.Rect(self.hitbox)
        if player_rect.colliderect(enemy_rect):
            return True  # Signal game over

        # Remove enemy if it goes off screen
        if self.x < -200 or self.x > 1400:
            return True
        return False

    def off_screen(self):
        return not(self.x >= -200 and self.x <= 1400)
    
################################################################################################################################################
# Draw Game - find out what this is
def draw_game():
    global lives  # Make lives accessible in the function
    # Single place to draw the entire frame (background, sprites, UI)
    DisplayOUTPUT.fill((0, 0, 0))
    DisplayOUTPUT.blit(Display_background, (0,0))
    # Draw enemies first so they appear behind the player
    for enemy in enemies:
        enemy.draw(DisplayOUTPUT)
    player.draw(DisplayOUTPUT)
    for bullet in player.bullets:
        bullet.draw_bullet()
        # Debug: Draw bullet hitbox (uncomment to see)
        # pygame.draw.rect(DisplayOUTPUT, (255, 255, 0), (bullet.x, bullet.y, 10, 10), 2)

    # Draw score and lives on top so they're always visible
    score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
    DisplayOUTPUT.blit(score_text, (5, 5))
    lives_text = font.render("Lives: {}".format(lives), True, (255, 255, 255))
    DisplayOUTPUT.blit(lives_text, (5, 35))

    # Draw controls
    controls_text = font.render("Controls: Arrow Keys to Move, SPACE to Jump, F to Shoot", True, (255, 255, 255))
    DisplayOUTPUT.blit(controls_text, (5, 65))

    # Use a single flip per frame to avoid tearing/flicker
    pygame.display.flip()

################################################################################################################################################
# Draw Game Over Screen
def draw_game_over():
    # Draw semi-transparent overlay
    overlay = pygame.Surface((1200, 800))
    overlay.set_alpha(200)  # Transparency level (0-255)
    overlay.fill((0, 0, 0))
    DisplayOUTPUT.blit(overlay, (0, 0))
    
    # Draw "GAME OVER" text
    game_over_font = pygame.font.Font(None, 100)
    game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(600, 250))
    DisplayOUTPUT.blit(game_over_text, game_over_rect)
    
    # Draw final score
    score_font = pygame.font.Font(None, 60)
    final_score_text = score_font.render(f"Final Score: {score}", True, (255, 255, 255))
    score_rect = final_score_text.get_rect(center=(600, 350))
    DisplayOUTPUT.blit(final_score_text, score_rect)
    
    # Draw replay button
    button_width = 300
    button_height = 80
    button_x = 450
    button_y = 450
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    
    # Check if mouse is hovering over button
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        button_color = (0, 200, 0)  # Lighter green on hover
    else:
        button_color = (0, 150, 0)  # Dark green
    
    pygame.draw.rect(DisplayOUTPUT, button_color, button_rect)
    pygame.draw.rect(DisplayOUTPUT, (255, 255, 255), button_rect, 3)  # White border
    
    # Draw button text
    button_font = pygame.font.Font(None, 50)
    button_text = button_font.render("REPLAY", True, (255, 255, 255))
    text_rect = button_text.get_rect(center=button_rect.center)
    DisplayOUTPUT.blit(button_text, text_rect)
    
    pygame.display.flip()
    
    return button_rect  # Return button rect for click detection

################################################################################################################################################
# Check collisions - FIXED VERSION
def check_collisions():
    global score
    for bullet in player.bullets[:]:  # Use slice to avoid modification during iteration
        # Remove bullets that go off-screen
        if bullet.off_screen():
            player.bullets.remove(bullet)
            continue
            
        for enemy in enemies[:]:  # Use slice to avoid modification during iteration
            # Create rectangles for collision detection
            bullet_rect = pygame.Rect(bullet.x, bullet.y, 10, 10)
            enemy_rect = pygame.Rect(enemy.hitbox)
            
            if bullet_rect.colliderect(enemy_rect):
                # Collision detected - increase score and remove bullet and enemy
                score += 100
                zombie_dead_sound.play()  # Play zombie death sound
                print(f"Hit! Score: {score}")  # Debug message
                if bullet in player.bullets:
                    player.bullets.remove(bullet)
                if enemy in enemies:
                    enemies.remove(enemy)
                break  # Break inner loop since bullet is destroyed

#########################################################################################
# Instance of Hero-Class

player = AdamTheDefender(300, 290)
################################################################################################################################################
#instance of enemy class

enemies = []
################################################################################################################################################
#textbox to output score
score = 0
lives = 3  # Player starts with 3 lives
running = True
game_over = False  # New variable to track game over state

# what is this
run = True
while run:

    # This allows the user to quit the game when the user clicks the X button on the pygame window
    for event in pygame.event.get(): # this for loop control all of the things that need to be conttsantly run
        if event.type == pygame.QUIT:
            run = False
        
        # Handle replay button click when game is over
        if game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Get button rect from draw function
            button_rect = pygame.Rect(450, 450, 300, 80)
            if button_rect.collidepoint(mouse_pos):
                # Reset game
                game_over = False
                score = 0
                lives = 3  # Reset lives
                enemies.clear()
                player.bullets.clear()
                player.x = 300
                player.y = 290
                print("Game restarted!")

    # Only update game if not game over
    if not game_over:

################################################################################################################################################
        # Input

        userInput = pygame.key.get_pressed()
################################################################################################################################################
        # Shoot

        player.shoot(userInput)

################################################################################################################################################
        # Movement

        player.move_AdamTheDefender(userInput)
        player.jump_motion(userInput)

################################################################################################################################################
        # Enemy - FIXED VERSION
        if len(enemies) == 0:
            rand_nr = random.randint(0, 1)
            if rand_nr == 1:
                # Spawn from right side, moving left
                enemy = Enemy(1200, 500, -1)
                enemies.append(enemy)
            else:
                # Spawn from left side, moving right
                enemy = Enemy(-100, 500, 1)
                enemies.append(enemy)
        
        # Update player hitbox before collision checks
        player.hitbox = (player.x + 15, player.y + 0, 120, 200)

        for enemy in enemies[:]:  # Use slice to avoid modification during iteration
            should_remove = enemy.move()
            if should_remove:
                # Check if it was a collision with player
                player_rect = pygame.Rect(player.hitbox)
                enemy_rect = pygame.Rect(enemy.hitbox)
                if player_rect.colliderect(enemy_rect):
                    lives -= 1  # Lose a life
                    cinematic_hit_sound.play()  # Play cinematic hit sound when enemy gets player
                    print(f"Enemy reached you! Lives left: {lives}")
                    if lives <= 0:
                        print("GAME OVER!")
                        game_over = True  # Set game over when no lives left
                        game_over_sound.play()  # Play game over sound
                else:
                    print("Enemy escaped!")
                enemies.remove(enemy)

################################################################################################################################################
        # Check for collisions between bullets and enemies
        check_collisions()

        # Draw Game in Window
        draw_game()
    else:
        # Draw game over screen
        draw_game_over()

    # Cap the framerate to a sensible value to avoid the game running uncapped as it could make rendering appear unstable on some systems.
    clock.tick(60)

################################################################################################################################################
pygame.quit()
################################################################################################################################################
# End of source code                                                                                                                           #
################################################################################################################################################
