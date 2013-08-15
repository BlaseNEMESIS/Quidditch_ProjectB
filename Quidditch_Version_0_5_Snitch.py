# Source File Name: Quidditch.py
# Author's Name: Jonathan Hodder
# Last Modified By: Jonathan Hodder
# Date Last Modified: July 29th 2013

#Version 0.1 - Created the Harry Class that allows the character to move harry left right and down.
#Gravity affects Harry  Using old images for assignment 4.
#Version 0.2 - Created the Quaffle Class, One quaffle spawns from the right side and will fly up or down.
#If it hits the left side or top of the screen they reset.  If a quaffle hits the floor it bounces back up
#Version 0.3 - Created the Enemy Flier Class, 5 Enemy Fliers spawns from the right side and will fly up or down.  If it hits the left side or
#top of the screen they reset.  If an Enemy Flier hits the bottom they fly back up.
#Version 0.4 - Created the Bludger Class, 2 Bludgers spawns from the right side and will fly up or down.  
#If it hits the left side or the top of the screen they reset.  If a bludger hits the bottom they fly back up.
#Version 0.5 - Create a Snitch Class, One fast snitch spawns.


import pygame, random, sys
pygame.init()

screen = pygame.display.set_mode((640, 480))
gravity = 9.8

#class Bludger creates a quaffle sprite
class Bludger(pygame.sprite.Sprite):
    #method that initializes the Bludger sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("flying_bird_red.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
    #end of __init__ method

    #method that updates the Bludger sprite
    def update(self):
        #if the Bludger sprite hits the top of the screen or passes the left side of the screen run the reset method
        if self.rect.bottom < 0 or self.rect.right < 0:
            self.reset()      
        elif self.rect.top > screen.get_height():
            self.dy = -self.dy
        self.rect.centerx -= self.dx
        self.rect.centery += self.dy            
    #end of update method
    
    #method reset the Bludger sprite
    def reset(self):
        #randomly select the height the Bludger will be spawn from
        randomy = random.randint(0, 460)
        self.rect.center = (640, randomy)
        #set the speeds for the Bludger
        self.dx = random.randrange(17, 20)
        self.dy = random.randrange(-9, 9)
    #end of reset method
#end of Bludger class



#class EnemyFlyer creates a quaffle sprite
class EnemyFlier(pygame.sprite.Sprite):
    #method that initializes the EnemyFlier sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("flying_bird.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
    #end of __init__ method

    #method that updates the EnemyFlier sprite
    def update(self):
        #if the EnemyFlier sprite hits the top of the screen or passes the left side of the screen run the reset method
        if self.rect.bottom < 0 or self.rect.right < 0:
            self.reset()      
        elif self.rect.top > screen.get_height():
            self.dy = -self.dy
        self.rect.centerx -= self.dx
        self.rect.centery += self.dy            
    #end of update method
    
    #method reset the EnemyFlier sprite
    def reset(self):
        #randomly select the height the EnemyFlier will be spawn from
        randomy = random.randint(0, 460)
        self.rect.center = (640, randomy)
        #set the speeds for the EnemyFlier
        self.dx = random.randrange(7, 10)
        self.dy = random.randrange(-3, 3)
    #end of reset method
#end of EnemyFlier class

#Creates the Harry sprite and its controls
class Harry(pygame.sprite.Sprite):
    #initializtion of the ballon man
    def __init__(self):
        #load the sprite onto the screen
        pygame.sprite.Sprite.__init__(self)
        #load variables and image for Harry
        self.image = pygame.image.load("balloon_man.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.x = 30
        self.y = 40
        self.currentx = self.x
        self.currenty = self.y
        self.dx = 5
        self.dy = 5
        self.flying = False
        #if there is no pygame.mixer sound will not work
        if not pygame.mixer:
            print("problem with sound")
        else:
            #initialize the sounds
            pygame.mixer.init()
            self.sndSnitchSound = pygame.mixer.Sound("snitchBlow.wav")
            self.sndQuaffleSound = pygame.mixer.Sound("CoinSound.wav")
            self.sndBalloonPop = pygame.mixer.Sound("balloonPop.wav")  
    #end of __init__ method
    
    #runs Harry update method    
    def update(self):
        #check if user has entered any keys
        self.checkKeys()
        self.rect.center = (self.x, self.y)
        #depending on where harry is effects how Harry is effected by gravity
        if self.rect.bottom > screen.get_height():
            self.x = self.currentx
        elif self.rect.top < 0:
            self.y = self.currenty
        elif self.rect.left < 0 or self.rect.right > 640:   
            self.x = self.currentx
            self.y += (gravity)
        else:
            self.currentx = self.x
            self.currenty = self.y
            self.y += (gravity)       
    #end of update method 
      
    #runs the check keys method    
    def checkKeys(self):
        keys = pygame.key.get_pressed()
        #if you click the right key harry movies right
        if keys[pygame.K_RIGHT]:
            self.x += self.dx
        #end of if statement keys K_RIGHT
        
        #if you click the left key harry moves left    
        if keys[pygame.K_LEFT]:
            self.x -= self.dx
        #end of if statement keys K_LEFT
        
        #if you click the spacebar or the up button run the fly method    
        if keys[pygame.K_SPACE]:
            self.flying = True
            self.fly(self.flying)
        #end of if statement keys K_SPACE
        
        elif keys[pygame.K_UP]:
            self.flying = True
            self.fly(self.flying)
        #end of if statement keys K_UP
    #end of checkKeys method
        
    #Fly method that allows Harry to fly            
    def fly(self, flying):
       #if flying is true harry flys
       if flying:
           self.y -= (gravity * 2)  
    #end of fly method              
#end of the harry class

#class Snitch creates a quaffle sprite
class Snitch(pygame.sprite.Sprite):
    #method that initializes the Snitch sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("balloon.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
    #end of __init__ method

    #method that updates the Snitch sprite
    def update(self):
        self.rect.centerx -= self.dx
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.dy = -self.dy
    #end of update method
    
    #method reset the Snitch sprite
    def reset(self):
        #randomly select the height the Snitch will be spawn from
        randomy = random.randint(0, 460)
        randomx = random.randint(0, 620)
        self.rect.center = (randomx, randomy)
        #set the speeds for the quaffle
        self.dx = random.randrange(-20, 20)
        self.dy = random.randrange(30)
    #end of reset method
#end of Snitch class

#class Quaffle creates a quaffle sprite
class Quaffle(pygame.sprite.Sprite):
    #method that initializes the quaffle sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coin.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
    #end of __init__ method

    #method that updates the quaffle sprite
    def update(self):
        #if the quaffle sprite hits the top of the screen or passes the left side of the screen run the reset method
        if self.rect.bottom < 0 or self.rect.right < 0:
            self.reset() 
        elif self.rect.top > screen.get_height():
            self.dy = -self.dy
        self.rect.centerx -= self.dx
        self.rect.centery += self.dy
    #end of update method
    
    #method reset the quaffle sprite
    def reset(self):
        #randomly select the height the quaffle will be spawn from
        randomy = random.randint(0, 460)
        self.rect.center = (640, randomy)
        #set the speeds for the quaffle
        self.dx = random.randrange(12, 15)
        self.dy = random.randrange(-9, 9)
    #end of reset method
#end of Quaffle class

#game method runs the game
def game():
    pygame.display.set_caption("Quidditch.py - Game On")
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    #create variables for the sprite classes
    harry = Harry()
    bludger1 = Bludger()
    bludger2 = Bludger()
    enemyFlier1 = EnemyFlier()
    enemyFlier2 = EnemyFlier()
    enemyFlier3 = EnemyFlier()
    enemyFlier4 = EnemyFlier()
    enemyFlier5 = EnemyFlier()
    snitch = Snitch()
    quaffle = Quaffle()
    randomSnitch = random.randint(0, 1)
    
    #store the sprite variables
    goodSprites = pygame.sprite.OrderedUpdates(harry, quaffle)
    enemySprites = pygame.sprite.Group(enemyFlier1, enemyFlier2, enemyFlier3, enemyFlier4, enemyFlier5, bludger1, bludger2)
    snitchSprite = pygame.sprite.Group(snitch)
    
    #set the fps
    clock = pygame.time.Clock()
    keepGoing = True
    #run the game until the game is over
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
       
        #update the sprites and then drawn them     
        goodSprites.clear(screen, background)
        enemySprites.clear(screen, background)
        snitchSprite.clear(screen, background)
           
        goodSprites.update()
        enemySprites.update()
        snitchSprite.update()

        goodSprites.draw(screen)
        enemySprites.draw(screen)
        snitchSprite.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True)
#end of game method

#Main method    
def main():
    #load the music
    pygame.mixer.music.load('MGS3 Theme.wav')
    pygame.mixer.music.play(-1)
    game()   
#end of main method

if __name__ == "__main__":
    main()