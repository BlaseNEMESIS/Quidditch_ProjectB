# Source File Name: Quidditch.py
# Author's Name: Jonathan Hodder
# Last Modified By: Jonathan Hodder
# Date Last Modified: July 30th 2013

#Version 0.1 - Created the Harry Class that allows the character to move harry left right and down.
#Gravity affects Harry  Using old images for assignment 4.
#Version 0.2 - Created the Quaffle Class, One quaffle spawns from the right side and will fly up or down.
#If it hits the left side or top of the screen they reset.  If a quaffle hits the floor it bounces back up
#Version 0.3 - Created the Enemy Flier Class, 5 Enemy Fliers spawns from the right side and will fly up or down.  If it hits the left side or
#top of the screen they reset.  If an Enemy Flier hits the bottom they fly back up.
#Version 0.4 - Created the Bludger Class, 2 Bludgers spawns from the right side and will fly up or down.  
#If it hits the left side or the top of the screen they reset.  If a bludger hits the bottom they fly back up.
#Version 0.5 - Create a Snitch Class, One fast snitch spawns.
#Version 0.6 - Added collision detection
#Version 0.7 - Added scoreboard class that shows both teams scores.  Added a health system for Harry and added a randomizer for enemy team scoring
#Version 0.8 - Added Intro Class, GameOver Class, Win Class, and Unconscious Class


import pygame, random, sys
pygame.init()

screen = pygame.display.set_mode((640, 480))
gravity = 9.8
healthStatus = "Healthy"

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
        self.dx = 10
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

#create the scoreboard sprite
class Scoreboard(pygame.sprite.Sprite):
    #initialize the scoreboard
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health ="Healthy"
        self.score = 0
        self.enemyScore = 0
        self.font = pygame.font.SysFont("None", 25)
    #end of __init__ method
    
    #update the scoreboard    
    def update(self):
        self.text = "Health: %s, Gryfindor Score: %d, Enemy Score: %d" % (self.health, self.score, self.enemyScore)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
    #end of update method
#end of Scoreboard Class

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
        self.dy = random.randrange(15)
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
    pygame.display.set_caption("Quidditch")
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    #create variables for the sprite classes
    #good sprites
    harry = Harry()
    quaffle = Quaffle()
    #enemey bludger sprites
    bludger1 = Bludger()
    bludger2 = Bludger()
    #enemy sprites
    enemyFlier1 = EnemyFlier()
    enemyFlier2 = EnemyFlier()
    enemyFlier3 = EnemyFlier()
    enemyFlier4 = EnemyFlier()
    enemyFlier5 = EnemyFlier()
    #snitch sprite
    snitch = Snitch()
    quaffle = Quaffle()
    #scoreboard sprite
    scoreboard = Scoreboard()
    
    #add counter variable
    counter = 0
    
    #store the sprite variables
    goodSprites = pygame.sprite.OrderedUpdates(harry, quaffle)
    enemySprites = pygame.sprite.Group(enemyFlier1, enemyFlier2) 
    enemyBludgerSprite = pygame.sprite.Group(bludger1, bludger2)
    snitchSprite = pygame.sprite.Group(snitch)
    scoreboardSprite = pygame.sprite.Group(scoreboard) 

    counterHealth = 5
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
       #check collisions if you hit the snitch add 150 points
        if harry.rect.colliderect(snitch.rect):
            harry.sndSnitchSound.play()
            snitch.reset()
            scoreboard.score +=150 
            score = scoreboard.score
            enemyScore = scoreboard.enemyScore
            if score < enemyScore:
                gameOver(score, enemyScore)
            else:
                win(score, enemyScore)  
        #check collision if you hit the quaffle  
        if harry.rect.colliderect(quaffle.rect):
            harry.sndQuaffleSound.play()
            quaffle.reset()
            randomScore = random.randint(0, 1)
            if randomScore == 0:
                scoreboard.score +=10
            counter += 1
        #check collision if you hit the bludger
        hitBludgers = pygame.sprite.spritecollide(harry, enemyBludgerSprite, False)
        if hitBludgers:
            harry.sndSnitchSound.play()
            for theBludger in hitBludgers:
                theBludger.reset()    
                counterHealth -= 1  
                if counterHealth == 5:
                    healthStatus = "Healthy"
                elif counterHealth == 4:
                    healthStatus = "Bruised"  
                elif counterHealth == 3:
                    healthStatus = "Injured"
                elif counterHealth == 2:
                    healthStatus = "Hurt"    
                elif counterHealth == 1:
                    healthStatus = "Crippled"        
                elif counterHealth == 0:
                    healthStatus = "Unconscious"
                scoreboard.health = healthStatus 
                
        #if an harry hits an enemy
        hitEnemies = pygame.sprite.spritecollide(harry, enemySprites, False)
        if hitEnemies:
            harry.sndQuaffleSound.play()
            for theEnemyFlier in hitEnemies:
                theEnemyFlier.reset()
                counterHealth -= 1  
                if counterHealth == 5:
                    healthStatus = "Healthy"
                elif counterHealth == 4:
                    healthStatus = "Bruised"  
                elif counterHealth == 3:
                    healthStatus = "Injured"
                elif counterHealth == 2:
                    healthStatus = "Hurt"    
                elif counterHealth == 1:
                    healthStatus = "Crippled"        
                elif counterHealth == 0:
                    healthStatus = "Unconscious"
                    score = scoreboard.score
                    enemyScore = scoreboard.enemyScore
                    unconscious(score, enemyScore)
                scoreboard.health = healthStatus               

        #check collision for hitting enemies    
        enemyCatchQuaffle = pygame.sprite.spritecollide(quaffle, enemySprites, False)
        if enemyCatchQuaffle:
            for theEnemyFlier in hitEnemies:
                theEnemyFlier.reset()
            quaffle.reset()
            randomScore = random.randint(0, 4)
            harry.sndQuaffleSound.play()
            scoreboard.enemyScore +=10
            counter += 1
        
        if counter == 10:
            counter = 0
            snitch.reset()
        #update the sprites and then drawn them     
        goodSprites.clear(screen, background)
        enemySprites.clear(screen, background)
        snitchSprite.clear(screen, background)
        enemyBludgerSprite.clear(screen, background)
        scoreboardSprite.clear(screen, background)
           
        goodSprites.update()
        enemySprites.update()
        snitchSprite.update()
        enemyBludgerSprite.update()
        scoreboardSprite.update()

        goodSprites.draw(screen)
        enemySprites.draw(screen)
        snitchSprite.draw(screen)
        enemyBludgerSprite.draw(screen)
        scoreboardSprite.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True)
#end of game method

def gameOver(score, enemyScore):
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    insFont = pygame.font.SysFont(None, 30)  
    #set the loss variable
    loss = (
    "You have lost.",
    "Final score is Gryffindor: %d, and Hufflepuff: %d" % (score, enemyScore),
    "",
    "Click the mouse to go back to the intro,", 
    "escape to quit..."
    )
    
    #add the instructions
    insLabels = []    
    for line in loss:
        tempLabel = insFont.render(line, 1, (0, 0, 0))
        insLabels.append(tempLabel)
    
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #if the user presses the mouse down start the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                intro()
            #if the user enter the escape key they are done playing
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        #display the loss message on the screen
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
    pygame.mouse.set_visible(True)
#end of gameOver method

def win(score, enemyScore):
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    insFont = pygame.font.SysFont(None, 30)  
    #set the win variable
    win = (
    "You have won.",
    "Final score is Gryffindor: %d, and Hufflepuff: %d" % (score, enemyScore),
    "",
    "Click the mouse to go back to the intro,", 
    "escape to quit..."
    )
    
    #add the instructions
    insLabels = []    
    for line in win:
        tempLabel = insFont.render(line, 1, (0, 0, 0))
        insLabels.append(tempLabel)
    
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #if the user presses the mouse down start the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                intro()
            #if the user enter the escape key they are done playing
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        #display the win message on the screen
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
    pygame.mouse.set_visible(True)
#end of win method

def unconscious(score, enemyScore):
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    insFont = pygame.font.SysFont(None, 30)  
    #set the loss variable
    loss = (
    "You have been knocked out of the game.",
    "Last seen score is Gryffindor: %d, and Hufflepuff: %d" % (score, enemyScore),
    "",
    "Click the mouse to go back to the intro,", 
    "escape to quit..."
    )
    
    #add the instructions
    insLabels = []    
    for line in loss:
        tempLabel = insFont.render(line, 1, (0, 0, 0))
        insLabels.append(tempLabel)
    
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #if the user presses the mouse down start the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                intro()
            #if the user enter the escape key they are done playing
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        #display the loss message on the screen
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
    pygame.mouse.set_visible(True)
#end of win method

#intro method runs the introduction to the game
def intro():
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    insFont = pygame.font.SysFont(None, 30)

    #set the instructions variable
    instructions = (
    "Qudditch.",
    "Instructions:  Pick a team to play against to start.",
    "Fly over the quaffle to help your team score,",
    "but be warned if the enemy team get the quaffle,",    
    "they can score too.  Watch out for bludgers and,",
    "enemy players running into them will injure yourself.", 
    "Watch out for the snitch grabbing it will get you 150 points,",
    "and end the game.  Be careful though the enemy team can", 
    "still win if they have enough points.",
    "",
    "Good Luck!",
    "",
    "Click the mouse to select a team, escape to quit..."
    )

    #add the instructions
    insLabels = []    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (0, 0, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #if the user presses the mouse down start the level select
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                game()
            #if the user enter the escape key they are done playing
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        #display the instructions on the screen
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()

    pygame.mouse.set_visible(True)
#end of intro method

#Main method    
def main():
    #load the music
    pygame.mixer.music.load('MGS3 Theme.wav')
    pygame.mixer.music.play(-1) 
    intro()
#end of main method

if __name__ == "__main__":
    main()