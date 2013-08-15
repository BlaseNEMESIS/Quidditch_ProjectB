# Source File Name: Quidditch.py
# Author's Name: Jonathan Hodder
# Last Modified By: Jonathan Hodder
# Date Last Modified: July 29th 2013

#Version 0.1 - Created the Harry Class that allows the character to move harry left right and down.
#Gravity affects Harry  Using old images for assignment 4.
#Version 0.2 - Created the Quaffle Class, One quaffle spawns from the right side and will fly up or straight.
#If it hits the left side or top of the screen they reset.


import pygame, random, sys
pygame.init()

screen = pygame.display.set_mode((640, 480))
gravity = 9.8


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
        self.rect.center= (self.x, self.y)
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

#class Quaffle creates a quaffle sprite
class Quaffle(pygame.sprite.Sprite):
    #method that initializes the quaffle sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("flying_bird.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
    #end of __init__ method

    #method that updates the quaffle sprite
    def update(self):
        self.rect.centerx -= self.dx
        self.rect.centery += self.dy
        #if the quaffle sprite hits the top of the screen or passes the left side of the screen run the reset method
        if self.rect.top > screen.get_height() or self.rect.bottom < 0 or self.rect.right < 0:
            self.reset()       
    #end of update method
    
    #method reset the quaffle sprite
    def reset(self):
        #randomly select the height the quaffle will be spawn from
        randomy = random.randint(0, 460)
        self.rect.center = (640, randomy)
        #set the speeds for the quaffle
        self.dx = random.randrange(12, 15)
        self.dy = random.randrange(-3, 0)
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
    quaffle = Quaffle()
    
    #store the sprite variables
    goodSprites = pygame.sprite.OrderedUpdates(harry, quaffle)
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
           
        goodSprites.update()

        goodSprites.draw(screen)

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