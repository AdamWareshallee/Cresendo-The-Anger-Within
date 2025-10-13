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

# Idle (i tried to make it animated) - ask sir
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
            

# Left animation 
left_AdamTheDefender =  [pygame.image.load("WR1.png"),
         pygame.image.load("WR2.png"),
         pygame.image.load("WR3.png"),
         pygame.image.load("WR4.png"),
         pygame.image.load("WR5.png"),
         pygame.image.load("WR6.png"),
         pygame.image.load("WR7.png"),
         pygame.image.load("WR8.png"),
         pygame.image.load("WR9.png"),
         pygame.image.load("WR10.png"),
         pygame.image.load("WR11.png")]

# Right animation 
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
################################################################################################################################################
# Animation for Flapberry Fudgewhistle (the enemy)

# Left animation
left_FlapberryFudgewhistle = [pygame.image.load("EW1.png"),
        pygame.image.load("EW2.png"),
        pygame.image.load("EW3.png"),
        pygame.image.load("EW4.png"),
        pygame.image.load("EW5.png"),
        pygame.image.load("EW6.png"),
        pygame.image.load("EW7.png"),
        pygame.image.load("EW8.png"),
        pygame.image.load("EW9.png"),
        ] 

# Right animation
right_FlapberryFudgewhistle = [pygame.image.load("EW1.png"),
        pygame.image.load("EW2.png"),
        pygame.image.load("EW3.png"),
        pygame.image.load("EW4.png"),
        pygame.image.load("EW5.png"),
        pygame.image.load("EW6.png"),
        pygame.image.load("EW7.png"),
        pygame.image.load("EW8.png"),
        pygame.image.load("EW9.png")
        ]

################################################################################################################################################
# Displaying the background and using the os libary to allow the background to display on the pygame window
# (1) Ask sir why it says error when i remove os.path.join.
# (2) Ask sir for the same for bullets as well. 

Display_background = pygame.transform.scale(pygame.image.load(os.path.join("Background.png")), (1200, 800)) # (1) try to not use win_width or win_height
bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("RageBullets.png")), (10, 10)) # (2)
################################################################################################################################################class Hero
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

     #(3)
     def move_AdamTheDefender(self, userInput): 
        if userInput[pygame.K_RIGHT] and self.x <= 1100: # The self.x <= 1100 controls the border for AdamTheDefender on the right side of the screen (x).
            self.x += self.Impetusx # This allows AdamTheDefender to move to the right with the '+'.
            self.face_right = True # This allows the right animation to operate when the right key is pressed
            self.face_left = False # This allows the left animation to not operate when the right key is pressed
        elif userInput[pygame.K_LEFT] and self.x >= 0: # The self.x <= 0 controls the border for AdamTheDefender on the left side of the screen (x).
            self.x -= self.Impetusx # This allows AdamTheDefender to move to the left with the '-'.
            self.face_right = False #This allows the right animation to not operate when the left key is pressed
            self.face_left = True #This allows the left animation to operate when the left key is pressed
        else:
            self.StepDirectory = 0 # If removed it gives a attribute error that AdamTheDefender object has no attribute 'stepIndex

     # (4)
     def draw(self, DisplayOUTPUT): # What is draw
        self.hitbox = (self.x + 15, self.y + 0, 120, 200)
        pygame.draw.rect(DisplayOUTPUT, (0,0,0), self.hitbox, 1)
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
        if self.jump:
            self.y -= self.Impetusy*8 # THis also changes how high the defender jumps
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
     def shoot(self):
        if userInput[pygame.K_f]:
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
        for bullet in self.bullets:
            bullet.move()
################################################################################################################################################
# Class for the bullets
class Bullet:
    def __init__(self, x, y, direction):
        self.x = x + 120 # I guess then this chnages where the position of the bullet is left and right
        self.y = y + 120 # This chnages where the postion of the bullet is up and down
        self.direction = direction 

    def draw_bullet(self):
        DisplayOUTPUT.blit(bullet_img, (self.x, self.y)) # Renmeber to show controls to the user maybe by using a pop up or a menu 

    def move(self):
        if self.direction == 1:
            self.x += 30
        if self.direction == -1:
            self.x -= 30
################################################################################################################################################
# Class for the enemy (Flapberry Fudgewhistle)
class Enemy:
    def __init__(self, x, y, direction, ):
        self.x = x
        self.y = y
        self.direction = direction
        self.StepDirectory = 0
        self.hitbox = (self.x, self.y, 50, 100)


    def step(self):
        if self.StepDirectory >= 33:
            self.StepDirectory = 0

    # what is this
    def draw(self, DisplayOUTPUT):
        self.hitbox = (self.x +15, self.y + 50, 500, 500)
        pygame.draw.rect(DisplayOUTPUT, (0,0,0), self.hitbox, 1)
        self.step()
        if self.direction == left_AdamTheDefender:
            DisplayOUTPUT.blit(left_FlapberryFudgewhistle[self.StepDirectory//4], (self.x, self.y))
        if self.direction == right_AdamTheDefender:
            DisplayOUTPUT.blit(right_FlapberryFudgewhistle[self.StepDirectory // 4], (self.x, self.y))
        self.StepDirectory += 1

    def move(self):
        if self.direction == left_AdamTheDefender:
            self.x -= 4
        if self.direction == right_AdamTheDefender:
            self.x += 4

    def off_screen(self):
        return not(self.x >= -1 and self.x <= 1200 + 1) # This is the border for the enemy on the left and right side of the screen
    
# Draw Game - find out what this is
def draw_game():
    # Single place to draw the entire frame (background, sprites, UI)
    DisplayOUTPUT.fill((0, 0, 0))
    DisplayOUTPUT.blit(Display_background, (0,0))
    player.draw(DisplayOUTPUT)
    for bullet in player.bullets:
        bullet.draw_bullet()
    for enemy in enemies:
        enemy.draw(DisplayOUTPUT)
    # Draw score on top so it's always visible
    score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
    DisplayOUTPUT.blit(score_text, (5, 5))
    # Use a single flip per frame to avoid tearing/flicker
    pygame.display.flip()
#########################################################################################
# Instance of Hero-Class

player = AdamTheDefender(300, 290)
################################################################################################################################################
#instance of enemy class

enemies = []
################################################################################################################################################
#textbox to output score
score = 0
running = True

# what is this
run = True
while run:

    # This allows the user to quit the game when the user clicks the X button on the pygame window
    for event in pygame.event.get(): # this for loop control all of the things that need to be conttsantly run
        if event.type == pygame.QUIT:
            run = False

    score += 1

################################################################################################################################################
    # Input

    userInput = pygame.key.get_pressed()
################################################################################################################################################
    # Shoot

    player.shoot()

################################################################################################################################################
    # Movement

    player.move_AdamTheDefender(userInput)
    player.jump_motion(userInput)

################################################################################################################################################
    # Enemy
    if len(enemies) == 0:
        rand_nr = random.randint(0,1)
        if rand_nr == 1:
            enemy = Enemy(200, 50, left_AdamTheDefender) # This changes the zombie position
            enemies.append(enemy)
        if rand_nr == 0:
            enemy = Enemy(200, 50, right_AdamTheDefender)
            enemies.append(enemy)
    for enemy in enemies:
        enemy.move()
        if enemy.off_screen():
            print("Ill get you next time")
            pygame.time.delay(300)
            enemies.remove(enemy)

################################################################################################################################################
    # Draw Game in Window

    draw_game()

    # Cap the framerate to a sensible value to avoid the game running uncapped
    # which can make rendering appear unstable on some systems.
    clock.tick(60)

################################################################################################################################################
################################################################################################################################################
# End of source code                                                                                                                           #
################################################################################################################################################