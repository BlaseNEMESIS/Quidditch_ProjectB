#Source File Name: quidditch.py
#Author's Name: Paige Harvey, Jonathon Hodder
#Last Modified By: Jonathan Hodder
#Last Modified On: 2013-08-13
#Program Description: A side-scrolling game based on Harry Potter's Quidditch

#Version 2.0: Incorporated level difficulty, stream-lined some methods

import pygame, random, sys, Buttons
pygame.init()

screen = pygame.display.set_mode((900,600))
gravity = 9.8
difficulty = 0

#class Bludger creates a bludger sprite
class Bludger(pygame.sprite.Sprite):
    #method that initializes the Bludger sprite
    def __init__(self,waitTime):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bludger.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.isVisible = False
        self.waitMaster = waitTime
        self.wait = self.waitMaster
        self.appear()
    #end of __init__ method

    #method that updates the Bludger sprite
    def update(self):
        if self.isVisible == True:
            #if the Bludger sprite hits the top of the screen or passes the left side of the screen run the reset method
            if self.rect.bottom < 0 or self.rect.right < 0:
                self.isVisible = False
                self.wait = self.waitMaster
            elif self.rect.top > screen.get_height():
                self.dy = -self.dy
            self.rect.centerx -= self.dx
            self.rect.centery += self.dy
        if self.isVisible == False:
            self.wait -= 1
            if self.wait == 0:
                self.appear()
    #end of update method

    #when collided with, method removes Bludger from screen
    def hit(self):
        self.isVisible = False
        self.wait = self.waitMaster
        self.rect.center = (1000,1000)
    #end of hit method
    
    #method that runs the Bludger
    def appear(self):
        self.isVisible = True
        #randomly select the height the Bludger will be spawn from
        randomy = random.randint(0, 600)
        self.rect.center = (900, randomy)
        #set the speeds for the Bludger
        self.dx = random.randrange(17, 20)
        self.dy = random.randrange(-9, 9)
    #end of appear method
#end of Bludger class

#class Dementor creates an opponent(enemy) sprite
class Dementor(pygame.sprite.Sprite):
    #method that initializes the OppFlier sprite
    def __init__(self,imagePath,waitTime):
        pygame.sprite.Sprite.__init__(self)
        self.x = 150
        self.y = 150
        self.image = pygame.image.load("dementor.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
    #end of __init__ method
#end of Dementor class

class Dragon(pygame.sprite.Sprite):
    #method that initializes the OppFlier sprite
    def __init__(self,imagePath,waitTime):
        pygame.sprite.Sprite.__init__(self)
        self.x = 150
        self.y = 150
        self.image = pygame.image.load("Dragon.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
    #end of __init__ method
#end of Dragon class

#class FireBall creates a bludger sprite
class FireBall(pygame.sprite.Sprite):
    #method that initializes the FireBall sprite
    def __init__(self,waitTime):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("FireBall.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.isVisible = False
        self.waitMaster = waitTime
        self.wait = self.waitMaster
        self.appear()
    #end of __init__ method

    #method that updates the FireBall sprite
    def update(self):
        if self.isVisible == True:
            #if the FireBall sprite hits the top of the screen or passes the left side of the screen run the reset method
            if self.rect.bottom < 0 or self.rect.right < 0:
                self.isVisible = False
                self.wait = self.waitMaster
            elif self.rect.top > screen.get_height():
                self.dy = -self.dy
            self.rect.centerx -= self.dx
            self.rect.centery += self.dy
        if self.isVisible == False:
            self.wait -= 1
            if self.wait == 0:
                self.appear()
    #end of update method

    #when collided with, method removes FireBall from screen
    def hit(self):
        self.isVisible = False
        self.wait = self.waitMaster
        self.rect.center = (1000,1000)
    #end of hit method
    
    #method that runs the FireBall
    def appear(self):
        self.isVisible = True
        #randomly select the height the FireBall will be spawn from
        randomy = random.randint(0, 600)
        self.rect.center = (900, randomy)
        #set the speeds for the FireBall
        self.dx = random.randrange(17, 20)
        self.dy = random.randrange(-9, 9)
    #end of appear method
#end of FireBall class

#class Ice creates a bludger sprite
class Ice(pygame.sprite.Sprite):
    #method that initializes the Ice sprite
    def __init__(self,waitTime):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Ice.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.isVisible = False
        self.waitMaster = waitTime
        self.wait = self.waitMaster
        self.appear()
    #end of __init__ method

    #method that updates the Ice sprite
    def update(self):
        if self.isVisible == True:
            #if the Ice sprite hits the top of the screen or passes the left side of the screen run the reset method
            if self.rect.bottom < 0 or self.rect.right < 0:
                self.isVisible = False
                self.wait = self.waitMaster
            elif self.rect.top > screen.get_height():
                self.dy = -self.dy
            self.rect.centerx -= self.dx
            self.rect.centery += self.dy
        if self.isVisible == False:
            self.wait -= 1
            if self.wait == 0:
                self.appear()
    #end of update method

    #when collided with, method removes Ice from screen
    def hit(self):
        self.isVisible = False
        self.wait = self.waitMaster
        self.rect.center = (1000,1000)
    #end of hit method
    
    #method that runs the Ice
    def appear(self):
        self.isVisible = True
        #randomly select the height the Ice will be spawn from
        randomy = random.randint(0, 600)
        self.rect.center = (900, randomy)
        #set the speeds for the Ice
        self.dx = random.randrange(17, 20)
        self.dy = random.randrange(-9, 9)
    #end of appear method
#end of Ice class

#class GoldenEgg creates a GoldenEgg sprite
class GoldenEgg(pygame.sprite.Sprite):
    #method that initializes the GoldenEgg sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("GoldenEgg.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (1000,1000)
        self.counterReset = 75
        self.counter = self.counterReset
        self.isVisible = False
    #end of __init__ method

    #method that updates the GoldenEgg sprite
        #GoldenEgg is to stay on screen until counter runs out
    def update(self):
        self.counter -= 1
        if self.counter == 0:
            self.disappear()
    #end of update method

    #method makes the GoldenEgg disappear from the screen
    def disappear(self):
        self.x = 1000
        self.y = 1000
        self.rect.center = (self.x, self.y)
        self.counter = self.counterReset
        self.isVisible = False
    #end of disappear method
    
    #method makes the GoldenEgg appear randomly
    def appear(self):
        #randomly select the height the GoldenEgg will be spawn from
        randomy = random.randint(0, 600)
        randomx = random.randint(0, 900)
        self.rect.center = (randomx, randomy)
        self.isVisible = True
    #end of appear method
#end of GoldenEgg class

#class OppFlier creates an opponent(enemy) sprite
class OppFlier(pygame.sprite.Sprite):
    #method that initializes the OppFlier sprite
    def __init__(self,imagePath,waitTime):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagePath)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.isVisible = False
        self.waitMaster = waitTime
        self.wait = self.waitMaster
        self.rect.center = (1000,1000)
    #end of __init__ method

    #method that updates the OppFlier sprite
    def update(self):
        if self.isVisible == True:
            #if the OppFlier sprite hits the top of the screen or passes the left side of the screen run the reset method
            if self.rect.bottom < 0 or self.rect.right < 0:
                self.isVisible = False
                self.wait = self.waitMaster
            elif self.rect.top > screen.get_height():
                self.dy = -self.dy
            self.rect.centerx -= self.dx
            self.rect.centery += self.dy
        if self.isVisible == False:
            self.wait -= 1
            if self.wait == 0:
                self.appear()
    #end of update method

    #when collided with, method removes flier from screen
    def hit(self):
        self.isVisible = False
        self.wait = self.waitMaster
        self.rect.center = (1000,1000)
    #end of hit method
    
    #method that runs the OppFlier
    def appear(self):
        self.isVisible = True
        #randomly select the height the OppFlier will be spawn from
        randomy = random.randint(0, 600)
        self.rect.center = (900, randomy)
        #set the speeds for the OppFlier
        self.dx = random.randrange(7, 10)
        self.dy = random.randrange(-3, 3)
    #end of appear method
#end of OppFlier class

#class Patronus creates a Patronus sprite
class GoldenEgg(pygame.sprite.Sprite):
    #method that initializes the Patronus sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Patronus.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (1000,1000)
        self.counterReset = 75
        self.counter = self.counterReset
        self.isVisible = False
    #end of __init__ method

    #method that updates the Patronus sprite
        #Patronus is to stay on screen until counter runs out
    def update(self):
        self.counter -= 1
        if self.counter == 0:
            self.disappear()
    #end of update method

    #method makes the Patronus disappear from the screen
    def disappear(self):
        self.x = 1000
        self.y = 1000
        self.rect.center = (self.x, self.y)
        self.counter = self.counterReset
        self.isVisible = False
    #end of disappear method
    
    #method makes the Patronus appear randomly
    def appear(self):
        #randomly select the height the Patronus will be spawn from
        randomy = random.randint(0, 600)
        randomx = random.randint(0, 900)
        self.rect.center = (randomx, randomy)
        self.isVisible = True
    #end of appear method
#end of Patronus class

#Creates the Harry sprite and its controls
class Harry(pygame.sprite.Sprite):
    #initializtion of harry
    def __init__(self):
        #load the sprite onto the screen
        pygame.sprite.Sprite.__init__(self)
        #load variables and image for Harry
        self.image = pygame.image.load("harry.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.x = 150
        self.y = 150
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
            self.sndBludger = pygame.mixer.Sound("balloonPop.wav")  
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
        elif self.rect.left < 0 or self.rect.right > 900:   
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
        self.oppScore = 0
        self.font = pygame.font.SysFont("None", 25)
    #end of __init__ method
    
    #update the scoreboard    
    def update(self):
        self.text = "Health: %s, Gryfindor Score: %d, Opponent Score: %d" % (self.health, self.score, self.oppScore)
        self.image = self.font.render(self.text, 1, (150, 150, 150))
        self.rect = self.image.get_rect()
    #end of update method
#end of Scoreboard Class

#class Snitch creates a quaffle sprite
class Snitch(pygame.sprite.Sprite):
    #method that initializes the Snitch sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Snitch.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (1000,1000)
        self.counterReset = 75
        self.counter = self.counterReset
        self.isVisible = False
    #end of __init__ method

    #method that updates the Snitch sprite
        #Snitch is to stay on screen until counter runs out
    def update(self):
        self.counter -= 1
        if self.counter == 0:
            self.disappear()
    #end of update method

    #method makes the Snitch disappear from the screen
    def disappear(self):
        self.x = 1000
        self.y = 1000
        self.rect.center = (self.x, self.y)
        self.counter = self.counterReset
        self.isVisible = False
    #end of disappear method
    
    #method makes the Snitch appear randomly
    def appear(self):
        #randomly select the height the Snitch will be spawn from
        randomy = random.randint(0, 600)
        randomx = random.randint(0, 900)
        self.rect.center = (randomx, randomy)
        self.isVisible = True
    #end of appear method
#end of Snitch class

#class Quaffle creates a quaffle sprite
class Quaffle(pygame.sprite.Sprite):
    #method that initializes the quaffle sprite
    def __init__(self, waitTime):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("quaffle.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.isVisible = False
        self.waitMaster = waitTime
        self.wait = self.waitMaster
        self.appear()
    #end of __init__ method

    #method that updates the quaffle sprite
    def update(self):
        if self.isVisible == True:
            #if the quaffle sprite hits the top of the screen or passes the left side of the screen run the reset method
            if self.rect.bottom < 0 or self.rect.right < 0:
                self.isVisible = False
                self.wait = self.waitMaster
            elif self.rect.top > screen.get_height():
                self.dy = -self.dy
            self.rect.centerx -= self.dx
            self.rect.centery += self.dy
        if self.isVisible == False:
            self.wait -= 1
            if self.wait == 0:
                self.appear()
    #end of update method

    #When collided with, method removes quaffle from screen
    def hit(self):
        self.isVisible = False
        self.wait = self.waitMaster
        self.rect.center = (1000,1000)
    #end of hit method
    
    #method runs the Quaffle's movements
    def appear(self):
        self.isVisible = True
        #randomly select the height the quaffle will be spawn from
        randomy = random.randint(0, 600)
        self.rect.center = (900, randomy)
        #set the speeds for the quaffle
        self.dx = random.randrange(12, 15)
        self.dy = random.randrange(-9, 9)
    #end of appear method
#end of Quaffle class

#Start of the background class
class pitchBackground(pygame.sprite.Sprite):
    #method initializes the sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pitch.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 20
        self.reset()
    #end of initialization method

    #method updates the background
    def update(self):
        self.rect.left -= self.dx
        if self.rect.left <= -12000:
            self.reset()
    #end of update method

    #method resets the background
    def reset(self):
        self.rect.left = 0
    #end of reset method

#Start of game method - is given level of difficulty
def game(difficulty):
    #set up the screen
    pygame.display.set_caption("Quidditch")
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,255))

    #creates the sprites
    harry = Harry()
    snitch = Snitch()
    scoreboard = Scoreboard()
    pitch = pitchBackground()

    #create opponent sprites depending on chosen difficulty
    #and sets sprite groups accordingly
    if difficulty == 1:     # Hufflepuff
        opp1 = OppFlier("H1.png",20)
        opp2 = OppFlier("H2.png",50)
        quaffle = Quaffle(10)   
        bludger1 = Bludger(100)
        badObjectSprites = pygame.sprite.OrderedUpdates(bludger1)
        oppSprites = pygame.sprite.Group(opp1, opp2)
        scoreSprites = pygame.sprite.Group(quaffle, snitch)
    
    elif difficulty == 2:   #Ravenclaw
        opp1 = OppFlier("R1.png",20)
        opp2 = OppFlier("R2.png",100)
        opp3 = OppFlier("R3.png",150)
        opp4 = OppFlier("R4.png",225)
        quaffle = Quaffle(30)
        bludger1 = Bludger(50)
        badObjectSprites = pygame.sprite.OrderedUpdates(bludger1)
        oppSprites = pygame.sprite.Group(opp1, opp2, opp3, opp4)
        scoreSprites = pygame.sprite.Group(quaffle, snitch) 
              
    elif difficulty == 3:   #Slytherin
        opp1 = OppFlier("S1.png", 20)
        opp2 = OppFlier("S2.png",100)
        opp3 = OppFlier("S3.png",150)
        opp4 = OppFlier("S4.png",225)
        opp5 = OppFlier("S5.png",364)
        quaffle = Quaffle(50)
        bludger1 = Bludger(40)
        bludger2 = Bludger(50)
        badObjectSprites = pygame.sprite.Group(bludger1,bludger2)
        oppSprites = pygame.sprite.Group(opp1, opp2, opp3, opp4, opp5)
        scoreSprites = pygame.sprite.Group(quaffle, snitch)   
            
    elif difficulty == 4:    #Dementors
        dementors = Dementor()
        ice1 = Ice()
        ice2 = Ice()
        ice3 = Ice()
        ice4 = Ice()
        ice5 = Ice()
        patronus = Patronus()
        oppSprites = pygame.sprite.OrderedUpdates(dementors)
        badObjectSprites = pygame.sprite.Group(ice1, ice2, ice3, ice4, ice5)
        scoreSprites = pygame.sprite.OrderedUpdates(patronus) 
               
    elif difficulty == 5:    #Dragon
        dragon = Dragon()
        fireball = Fireball()
        goldEgg = GoldEgg()
        oppSprites = pygame.sprite.OrderedUpdates(dragon)
        badObjectSprites = pygame.sprite.OrderedUpdates(fireBall)
        scoreSprites = pygame.sprite.OrderedUpdates(goldEgg)

    #sprite groupings
    neutralSprites = pygame.sprite.Group(pitch, scoreboard)
    goodSprites = pygame.sprite.OrderedUpdates(harry)
    
    #set variables
    health = 5
    clock = pygame.time.Clock()
    keepGoing = True

    #Gameplay loop
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #collisions
            #Harry and Snitch
        if harry.rect.colliderect(snitch.rect):
            harry.sndSnitchSound.play()
            scoreboard.score += 150
            snitch.disappear()
            keepGoing = False
            gameOver(scoreboard.score, scoreboard.oppScore, health)

            #Harry and Quaffle
        if harry.rect.colliderect(quaffle.rect):
            harry.sndQuaffleSound.play()
            quaffle.hit()
            scoreboard.score += 10
		
        if harry.rect.colliderect(dementor.rect):
			harry.snd.SnitchSound.play()
			keepGoing = False
			gameOver(scoreboard.score, scoreboard.oppScore, health)
		
        if harry.rect.colliderect(dragon.rect):
			harry.snd.SnitchSound.play()
			keepGoing = False
			gameOver(scoreboard.score, scoreboard.oppScore, health)
		
					
        if difficulty == 4:
			hitIce = pygame.sprite.spritecollide(harry,badObjectSprites,False)
			if hitBludgers:
				harry.sndBludger.play()
					#Bludgers damage health
				for theBludger in hitBludgers:
					theBludger.hit()
					health -= 1
					if health == 5:
						scoreboard.health = "Healthy"
					elif health == 4:
						scoreboard.health = "Bruised"
					elif health == 3:
						scoreboard.health = "Injured"
					elif health == 2:
						scoreboard.health = "Hurt"
					elif health == 1:
						scoreboard.health = "Crippled"
					elif health == 0:
						scoreboard.health = "Unconscious"
						keepGoing = False
						scoreboard.oppScore += 150
						gameOver(scoreboard.score, scoreboard.oppScore,health)
        else:
			#Harry and Bludgers
			hitBludgers = pygame.sprite.spritecollide(harry,badObjectSprites,False)
			if hitBludgers:
				harry.sndBludger.play()
					#Bludgers damage health
				for theBludger in hitBludgers:
					theBludger.hit()
					health -= 1
					if health == 5:
						scoreboard.health = "Healthy"
					elif health == 4:
						scoreboard.health = "Bruised"
					elif health == 3:
						scoreboard.health = "Injured"
					elif health == 2:
						scoreboard.health = "Hurt"
					elif health == 1:
						scoreboard.health = "Crippled"
					elif health == 0:
						scoreboard.health = "Unconscious"
						keepGoing = False
						scoreboard.oppScore += 150
						gameOver(scoreboard.score, scoreboard.oppScore,health)

		
        if harry.rect.colliderect(fireBall.rect):	
			health -= 1
			if health == 5:
				scoreboard.health = "Healthy"
			elif health == 4:
				scoreboard.health = "Bruised"
			elif health == 3:
				scoreboard.health = "Injured"
			elif health == 2:
				scoreboard.health = "Hurt"
			elif health == 1:
				scoreboard.health = "Crippled"
			elif health == 0:
				scoreboard.health = "Unconscious"
				keepGoing = False
				scoreboard.oppScore += 150
				gameOver(scoreboard.score, scoreboard.oppScore,health)		
						
        #Harry and Opponents
        #Hitting an opponent gives them a penalty shot
        hitOpps = pygame.sprite.spritecollide(harry, oppSprites,False)
        if hitOpps:
            harry.sndBludger.play()
            for theOppFlyer in hitOpps:
                theOppFlyer.hit()
                scoreboard.oppScore += 10
                

        #determine if the snitch appears
                #When the two numbers match, Snitch shows
        if snitch.isVisible == False:
            snitchAttempt = random.randrange(1,150,1)
            snitchWin = random.randrange(1,150,1)
            if snitchAttempt == snitchWin:
                snitch.appear()  

        #Blit EVERYTHING!!!
        screen.blit(background,(0,0))        

        neutralSprites.clear(screen, background)
        goodSprites.clear(screen, background)
        scoreSprites.clear(screen, background)
        badObjectSprites.clear(screen, background)
        oppSprites.clear(screen, background)

        neutralSprites.update()
        goodSprites.update()
        scoreSprites.update()
        badObjectSprites.update()
        oppSprites.update()

        neutralSprites.draw(screen)
        goodSprites.draw(screen)
        scoreSprites.draw(screen)
        badObjectSprites.draw(screen)
        oppSprites.draw(screen)

        pygame.display.flip()

    pygame.mouse.set_visible(True)
#End of game method

#intro method runs the introduction to the game
def intro():
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    insFont = pygame.font.SysFont(None, 30)

    #create the Buttons for level choice
    huff = Buttons.Button()
    claw = Buttons.Button()
    slyt = Buttons.Button()
    demen = Buttons.Button()
    dragon = Buttons.Button()
    huffLabel = labels("Hufflepuff")
    clawLabel = labels("Ravenclaw")
    slytLabel = labels("Slytherin")
    demenLabel = labels("Dementors")
    dragonLabel = labels("Dragon")

    #Create background sprite
    pitch = pitchBackground()

    allSprites = pygame.sprite.Group(pitch)

    #set the instructions variable
    instructions = (
    "Qudditch.",
    "Instructions:  You are Harry Potter, Gryffindor's Seeker. To win, your team",
    "must have more points when the game ends. Catching the Snitch will end the ",
    "game and grant 150 points. The Red Quaffle earns 10 points. Colliding with ",
    "an opponent gives them a penalty shot!",
    "Beware the Black Bludgers, they'll knock out right out the game and into the",
    "hospital.",
    "",
    "Good Luck!",
    "",
    "Click the mouse to select a team, escape to quit..."
    )

    #add the instructions
    insLabels = []    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (50, 50, 50))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #if the user clicks on a button, start the level select
            if event.type == pygame.MOUSEBUTTONDOWN:
                if huff.onClick(pygame.mouse.get_pos()):
                    keepGoing = False
                    game(1)
                elif claw.onClick(pygame.mouse.get_pos()):
                    keepGoing = False
                    game(2)
                elif slyt.onClick(pygame.mouse.get_pos()):
                    keepGoing = False
                    game(3)
                elif demen.onClick(pygame.mouse.get_pos()):
					demenIntro(4)
                elif dragon.onClick(pygame.mouse.get_pos()):
					dragonIntro(5)
                else:
                    keepGoing = True
            #if the user enter the escape key they are done playing
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    #Blit EVERYTHING!!!
        allSprites.update()
        allSprites.draw(screen)

        #display the instructions on the screen
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        huff.alphaSquare(screen,(255,255,0),100,50,100,400)
        claw.alphaSquare(screen,(0,0,255),100,50,350,400)
        slyt.alphaSquare(screen,(0,200,0),100,50,225,475)
        screen.blit(huffLabel,(108,415))
        screen.blit(clawLabel,(358,415))
        screen.blit(slytLabel,(235,490))

        pygame.display.flip()

#end of intro method

#method that runs when gameplay is over
def gameOver(score, oppScore, health):
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,255))
    screen.blit(background, (0,0))
    insFont = pygame.font.SysFont(None,30)

    pitch = pitchBackground()

    allSprites = pygame.sprite.Group(pitch)

    #create the message that shows for each outcome
    won = (
    "You caught the Snitch!",
    "Gryffindor won the game %d to %d" %(score, oppScore),
    "",
    "Click the mouse to return to game start,",
    "press 'Escape' to quit."
    )
    techLoss = (
    "You caught the Snitch! But your opponents have more points.",
    "Gryffindor loses %d to %d" %(score, oppScore),
    "",
    "Click the mouse to return to game start,",
    "press 'Escape' to quit."
    )
    knockOut = (
    "You've been knocked unconscious!",
    "With no replacement Seeker the other team caught the Snitch.",
    "The final score was Gryffindor %d to %d" %(score,oppScore),
    "",
    "Click the mouse to return to game start,",
    "press 'Escape' to quit."
    )
    tie = (
    "Well now this is odd, you've tied the game!",
    "Both teams have %d points!" %(score),
    "",
    "Click the mouse to return to game start,",
    "press 'Escape' to quit."
    )

    insLabels = []
    #use the score to determine which ending is given to User
    if health == 0:
        for line in knockOut:
            tempLabel = insFont.render(line,1,(0,0,0))
            insLabels.append(tempLabel)
    elif score > oppScore:
        for line in won:
            tempLabel = insFont.render(line,1,(0,0,0))
            insLabels.append(tempLabel)
    elif score < oppScore:
        for line in techLoss:
            tempLabel = insFont.render(line,1,(0,0,0))
            insLabels.append(tempLabel)
    elif score == oppScore:
        for line in tie:
            tempLabel = insFont.render(line,1,(0,0,0))
            insLabels.append(tempLabel)

    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                intro()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        allSprites.update()
        allSprites.draw(screen)
        
        #Display the message on the screen
        for i in range(len(insLabels)):
            screen.blit(insLabels[i],(50,30*i))

        pygame.display.flip()
#end of gameOver method

#Method that creates labels
def labels(toPrint):
    font = pygame.font.SysFont(None, 25)
    label = font.render(toPrint, 1, (0,0,0))
    return label
#end of labels method

#Main method    
def main():
    pygame.display.set_caption("Quidditch")
    #load the music
    pygame.mixer.music.load('earth.wav')
    pygame.mixer.music.play(-1)
    splash()
#end of main method

#Splash Screen
def splash():
    pygame.display.set_caption("Quidditch")
    time.sleep(10)
    intro()
#End of Splash Screen

#demenIntro method	
def demenIntro(difficulty):
    pygame.display.set_caption("Dementors")
	#create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,255))
    screen.blit(background, (0,0))
    insFont = pygame.font.SysFont(None,30)

    pitch = pitchBackground()

    allSprites = pygame.sprite.Group(pitch)

    #create the message that shows for each outcome
    dementors = (
    "You caught the Snitch!",
    "Gryffindor won the game %d to %d" %(score, oppScore),
    "",
    "Click the mouse to return to game start,",
    "press 'Escape' to quit."
    )
	#add the instructions
    insLabels = []    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (50, 50, 50))
        insLabels.append(tempLabel)
	game(4)
#end of demenIntro method

#dragonIntro method	
def dragonIntro(difficulty):	
    pygame.display.set_caption("Dragon")
	#create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,255))
    screen.blit(background, (0,0))
    insFont = pygame.font.SysFont(None,30)

    pitch = pitchBackground()

    allSprites = pygame.sprite.Group(pitch)

    #create the message that shows for each outcome
    dragon = (
    "You caught the Snitch!",
    "Gryffindor won the game %d to %d" %(score, oppScore),
    "",
    "Click the mouse to return to game start,",
    "press 'Escape' to quit."
    )
	#add the instructions
    insLabels = []    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (50, 50, 50))
        insLabels.append(tempLabel)
		
	game(5)
#End of dragonIntro method
	
if __name__ == "__main__":
    main()
