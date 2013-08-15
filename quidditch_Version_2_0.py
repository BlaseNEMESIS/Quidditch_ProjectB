#Source File Name: quidditch.py
#Author's Name: Paige Harvey, Jonathon Hodder
#Last Modified By: Paige Harvey
#Last Modified On: 2013-08-12
#Program Description: A side-scrolling game based on Harry Potter's Quidditch

#Version 2.0: Create boss levels
# - Have buttons on level select working for Bosses

import pygame, random, sys, Buttons,time
pygame.init()

screen = pygame.display.set_mode((900,600))
gravity = 9.8

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

#start of Boss Class
class Boss(pygame.sprite.Sprite):
    #method that initializes the Boss Sprite
    def __init__(self,imagePath):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagePath)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (-150,300)
        self.onScreen = False
    #end of __init__ method

    #update method of the Boss
    def update(self):
        if self.onScreen == False:
            self.rect.centerx += 1
        if self.rect.center == (150,300):
            self.onScreen = True
    #end of update method
#end of Boss Class
        
#class FireBall creates a FireBall sprite
class FireBall(pygame.sprite.Sprite):
    #method that initializes the FireBall sprite
    def __init__(self,waitTime):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Fireball.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.isVisible = False
        self.waitMaster = waitTime
        self.wait = self.waitMaster
        self.rect.center = (1000,1000)
    #end of __init__ method

    #method that updates the FireBall sprite
    def update(self):
        if self.isVisible == True:
            #if the FireBall sprite hits the top of the screen or passes the left side of the screen run the reset method
            if self.rect.bottom < 0 or self.rect.left > 900:
                self.isVisible = False
                self.wait = self.waitMaster
            elif self.rect.top > screen.get_height():
                self.dy = -self.dy
            self.rect.centerx += self.dx
            self.rect.centery -= self.dy
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
        self.rect.center = (150,100)
        #set the speeds for the FireBall
        self.dx = random.randrange(17, 20)
        self.dy = random.randrange(-19, 5)
    #end of appear method
#end of FireBall class

#class Ice creates an Ice sprite
class Ice(pygame.sprite.Sprite):
    #method that initializes the Ice sprite
    def __init__(self,waitTime):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Ice.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (1000,1000)
        self.isVisible = False
        self.waitMaster = waitTime
        self.wait = self.waitMaster
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
##            self.rect.centery += self.dy
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

#class GoldenEgg creates a GoldenEgg sprite
class GoldenEgg(pygame.sprite.Sprite):
    #method that initializes the GoldenEgg sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Egg.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (1000,1000)
        self.isVisible = False
    #end of __init__ method

    #method that updates the GoldenEgg sprite
        #GoldenEgg is to stay on screen until counter runs out
    def update(self):
        if self.isVisible:
            self.rect.centerx -= 1
        if self.rect.center == (800,500):
            self.isVisible = False
    #end of update method

    #Method shows the egg on screen
    def appear(self):
        self.isVisible = True
        self.rect.center = (950,500)
    #end of appear method
#end of GoldenEgg Class

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
        self.x = 600
        self.y = 500
        self.currentx = self.x
        self.currenty = self.y
        self.dx = 10
        self.dy = 5
        self.rect.center = (self.x,self.y)
        self.flying = False
        #if there is no pygame.mixer sound will not work
        if not pygame.mixer:
            print("problem with sound")
        else:
            #initialize the sounds
            pygame.mixer.init()
            self.sndWinSound = pygame.mixer.Sound("CoinSound.wav")
            self.sndQuaffleSound = pygame.mixer.Sound("Score.wav")
            self.sndBludger = pygame.mixer.Sound("bludgerHit.wav")
            self.sndOpp = pygame.mixer.Sound("Boo.wav")
            self.sndDemt = pygame.mixer.Sound("scream.wav")
            self.sndDrgn = pygame.mixer.Sound("Crunch.wav")
            self.sndIce = pygame.mixer.Sound("IceShatter.wav")
            self.sndFireball = pygame.mixer.Sound("Fireball.wav")
            
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

    #hitIce method runs when Harry hits Ice
    def hitIce(self):
        self.x -= 100
    #end of hitIce method
#end of the harry class

#class Patronus creates a Patronus sprite
class Patronus(pygame.sprite.Sprite):
    #method that initializes the Patronus sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Patronus.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (1000,1000)
        self.isVisible = False
    #end of __init__ method

    #method that updates the Patronus sprite
    def update(self):
        if self.isVisible:
            self.rect.centerx -= 1
        if self.rect.center == (750,300):
            self.isVisible = False
    #end of update method

    #Method shows the shield on screen
    def appear(self):
        self.rect.center = (1050,300)
        self.isVisible = True
    #end of appear method
#end of Patronus Class

#create the scoreboard sprite
class Scoreboard(pygame.sprite.Sprite):
    #initialize the scoreboard
    def __init__(self, version):
        pygame.sprite.Sprite.__init__(self)
        self.health ="Healthy"
        self.score = 0
        self.oppScore = 0
        self.version = version
        self.font = pygame.font.SysFont("None", 25)
    #end of __init__ method
    
    #update the scoreboard
    def update(self):
        if self.version == 1:
            self.text = "Health: %s, Gryfindor Score: %d, Opponent Score: %d" % (self.health, self.score, self.oppScore)
        elif self.version == 2:
            self.text = "Health: %s" % self.health
        self.image = self.font.render(self.text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.right = 900
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
    def __init__(self, weather):
        pygame.sprite.Sprite.__init__(self)
        if weather == 1:
            self.image = pygame.image.load("pitch.png")
        else:
            self.image = pygame.image.load("pitchStormy.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 20
        self.counter = 0
        self.reset()
    #end of initialization method

    #method updates the background
    def update(self):
        self.rect.left -= self.dx
        if self.rect.left <= -12000:
            self.counter += 1
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

    healthbar = pygame.Surface((475,20))
    healthbar = healthbar.convert()
    healthbar.fill((0,0,0))

    #load the music
    pygame.mixer.music.load('earth.wav')
    pygame.mixer.music.play(-1) 

    #creates the sprites
    harry = Harry()
    snitch = Snitch()
    scoreboard = Scoreboard(1)
    pitch = pitchBackground(1)

    #create opponent sprites depending on chosen difficulty
    #and sets sprite groups accordingly
    if difficulty == 1:     # Hufflepuff
        opp1 = OppFlier("H1.png",20)
        opp2 = OppFlier("H2.png",50)
        quaffle = Quaffle(10)   
        bludger1 = Bludger(100)
        bludgerSprites = pygame.sprite.Group(bludger1)
        oppSprites = pygame.sprite.Group(opp1,opp2)
    elif difficulty == 2:   #Ravenclaw
        opp1 = OppFlier("R1.png",20)
        opp2 = OppFlier("R2.png",100)
        opp3 = OppFlier("R3.png",150)
        opp4 = OppFlier("R4.png",225)
        quaffle = Quaffle(30)
        bludger1 = Bludger(50)
        bludgerSprites = pygame.sprite.Group(bludger1)
        oppSprites = pygame.sprite.Group(opp1,opp2,opp3,opp4)
    elif difficulty == 3:   #Slytherin
        opp1 = OppFlier("S1.png", 20)
        opp2 = OppFlier("S2.png",100)
        opp3 = OppFlier("S3.png",150)
        opp4 = OppFlier("S4.png",225)
        opp5 = OppFlier("S5.png",364)
        quaffle = Quaffle(50)
        bludger1 = Bludger(40)
        bludger2 = Bludger(50)
        bludgerSprites = pygame.sprite.Group(bludger1,bludger2)
        oppSprites = pygame.sprite.Group(opp1,opp2,opp3,opp4,opp5)

    #sprite groupings
    pitchSprites = pygame.sprite.OrderedUpdates(pitch)
    goodSprites = pygame.sprite.Group(scoreboard, harry)
    ballSprites = pygame.sprite.Group(quaffle, snitch)
    
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
            harry.sndWinSound.play()
            scoreboard.score += 150
            snitch.disappear()
            keepGoing = False
            gameOver(scoreboard.score, scoreboard.oppScore, health, difficulty)

            #Harry and Quaffle
        if harry.rect.colliderect(quaffle.rect):
            harry.sndQuaffleSound.play()
            quaffle.hit()
            scoreboard.score += 10

            #Harry and Bludgers
        hitBludgers = pygame.sprite.spritecollide(harry,bludgerSprites,False)
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
                    gameOver(scoreboard.score, scoreboard.oppScore,health, difficulty)

            #Harry and Opponents
                    #Hitting an opponent gives them a penalty shot
        hitOpps = pygame.sprite.spritecollide(harry, oppSprites,False)
        if hitOpps:
            harry.sndOpp.play()
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

        pitchSprites.clear(screen, background)
        goodSprites.clear(screen, background)
        ballSprites.clear(screen, background)
        bludgerSprites.clear(screen, background)
        oppSprites.clear(screen, background)

        pitchSprites.update()
        goodSprites.update()
        ballSprites.update()
        bludgerSprites.update()
        oppSprites.update()

        pitchSprites.draw(screen)
        screen.blit(healthbar,(425,0))
        goodSprites.draw(screen)
        ballSprites.draw(screen)
        bludgerSprites.draw(screen)
        oppSprites.draw(screen)

        pygame.display.flip()

    pygame.mouse.set_visible(True)
#End of game method

#start of Boss Method
def boss(difficulty):
    #set up the screen
    pygame.display.set_caption("Quidditch")
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,255))

    healthbar = pygame.Surface((150,20))
    healthbar = healthbar.convert()
    healthbar.fill((0,0,0))

    #creates the sprites
    harry = Harry()
    scoreboard = Scoreboard(2)

    #create opponent sprites depending on chosen difficulty
    #and sets sprite groups accordingly
    if difficulty == 4:     # Dementors
        pitch = pitchBackground(2)
        ice1 = Ice(10)
        ice2 = Ice(30)
        ice3 = Ice(47)
        ice4 = Ice(86)
        ice5 = Ice(104)
        boss = Boss("Dementors.png")
        goal = Patronus()
        objSprites = pygame.sprite.Group(ice1,ice2,ice3,ice4,ice5)
    elif difficulty == 5:   #Dragon
        pitch = pitchBackground(1)
        fire1 = FireBall(10)
        fire2 = FireBall(47)
        fire3 = FireBall(115)
        boss = Boss("Dragon.png")
        goal = GoldenEgg()
        objSprites = pygame.sprite.Group(fire1,fire2,fire3)
        
    pitchSprites = pygame.sprite.OrderedUpdates(pitch)
    goodSprites = pygame.sprite.Group(harry,scoreboard)
    bossSprites = pygame.sprite.OrderedUpdates(boss)
    goalSprites = pygame.sprite.Group(goal)

    health = 10
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #After harry makes x laps of the pitch the goal item appears on screen
        if pitch.counter == 2:
            goal.appear()

        #Collisions
                #Harry and the boss
        if harry.rect.colliderect(boss.rect):
            if difficulty == 4:
                harry.sndDemt.play()
            elif difficulty == 5:
                harry.sndDrgn.play()
            health = 0
            keepGoing = False
            gameOver(0,0,health,difficulty)

            #harry and the goal item
        if harry.rect.colliderect(goal.rect):
            harry.sndWinSound.play()
            keepGoing = False
            gameOver(0,0,health, difficulty)
            
            #harry and bad objects
        hitObj = pygame.sprite.spritecollide(harry,objSprites,False)
        if hitObj and difficulty == 4:
            harry.sndIce.play()
            for theIce in hitObj:
                theIce.hit()
                harry.hitIce()
        if hitObj and difficulty == 5:
            harry.sndFireball.play()
            for theFire in hitObj:
                theFire.hit()
                health -= 1
                if health == 10:
                    scoreboard.health = "Healthy"
                elif health == 8:
                    scoreboard.health = "Singed"
                elif health == 6:
                    scoreboard.health = "Toasted"
                elif health == 4:
                    scoreboard.health = "Roasted"
                elif health == 2:
                    scoreboard.health = "Charcoal"
                elif health == 0:
                    scoreboard.health = "Ashes"
                    keepGoing = False
                    gameOver(0,0,0,difficulty)

        #blit EVERYTHING!!!
        screen.blit(background,(0,0))

        pitchSprites.clear(screen,background)
        goodSprites.clear(screen,background)
        objSprites.clear(screen,background)
        bossSprites.clear(screen,background)
        goalSprites.clear(screen,background)

        pitchSprites.update()
        goodSprites.update()
        objSprites.update()
        bossSprites.update()
        goalSprites.update()

        pitchSprites.draw(screen)
        screen.blit(healthbar,(750,0))
        goodSprites.draw(screen)
        objSprites.draw(screen)
        bossSprites.draw(screen)
        goalSprites.draw(screen)

        pygame.display.flip()

#intro method runs the introduction to the game
def intro(lastWin):
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    insFont = pygame.font.SysFont(None, 30)

    #create the Buttons for level choice
    huff = Buttons.Button()
    claw = Buttons.Button()
    slyt = Buttons.Button()
    huffLabel = labels("Hufflepuff")
    clawLabel = labels("Ravenclaw")
    slytLabel = labels("Slytherin")

    #Buttons for Boss Levels
    demt = Buttons.Button()
    drgn = Buttons.Button()
    demtLabel = labels("Boss 1")
    drgnLabel = labels("Boss 2")

    #Set button colours
    colourH = (255,255,0)
    colourR = (0,0,255)
    colourS = (0,200,0)
    colourB = (255,0,0)
    colourDisable = (150,150,150)

    #Create background sprite
    pitch = pitchBackground(1)

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

    huffWin = False
    clawWin = False
    slytWin = False
    demtWin = False
    drgnWin = False

    if lastWin == 1:
        huffWin = True
    elif lastWin == 2:
        huffWin = True
        clawWin = True
    elif lastWin == 3:
        huffWin = True
        clawWIn = True
        slytWin = True
    elif lastWin == 4:
        huffWin = True
        clawWIn = True
        slytWin = True
        dementr = True
    elif lastWin == 5:
        huffWin = True
        clawWIn = True
        slytWin = True
        demtWin = True
        drgnWin = True
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    huffWin = True
                    clawWin = True
                    slytWin = True
                    demtWin = True
                    drgnWin = True
            #if the user clicks on a button, start the level select
            if event.type == pygame.MOUSEBUTTONDOWN:
                if huff.onClick(pygame.mouse.get_pos()):
                    keepGoing = False
                    game(1)
                elif claw.onClick(pygame.mouse.get_pos()) and huffWin == True:
                    keepGoing = False
                    game(2)
                elif slyt.onClick(pygame.mouse.get_pos()) and clawWin == True:
                    keepGoing = False
                    game(3)
                elif demt.onClick(pygame.mouse.get_pos()):
                    keepGoing = False
                    bossIntro(4)
                elif drgn.onClick(pygame.mouse.get_pos()):
                    keepGoing = False
                    bossIntro(5)
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

        huff.alphaSquare(screen,colourH,100,50,100,400)
        if huffWin:
            claw.alphaSquare(screen,colourR,100,50,350,400)
        else:
            claw.alphaSquare(screen,colourDisable,100,50,350,400)
        if clawWin:
            slyt.alphaSquare(screen,colourS,100,50,225,475)
        else:
            slyt.alphaSquare(screen,colourDisable,100,50,225,475)
        screen.blit(huffLabel,(108,415))
        screen.blit(clawLabel,(358,415))
        screen.blit(slytLabel,(235,490))

        #Show the boss Levels
        if slytWin:
            demt.alphaSquare(screen,colourB,100,50,625,375)
            screen.blit(demtLabel,(648,391))
        
        if demtWin:
            drgn.alphaSquare(screen,colourB,100,50,625,450)
            screen.blit(drgnLabel,(648,466))

        pygame.display.flip()

#end of intro method

#Start of Boss Intro Method
def bossIntro(difficulty):
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,255))
    screen.blit(background, (0,0))
    insFont = pygame.font.SysFont(None,30)

    #create the message that shows fo each outcome
    demt = (
    "Dementors have interrupted the game!",
    "Outfly the Dementor until Dumbledore can errect a Patronus Shield",
    "Beware, ice cyrstals will slow you down.",
    "",
    "Click the mouse to start the boss level,",
    "press 'Escape' to quit."
    )
    drgn = (
    "Harry's First Task in the Tri-Wizard Tournament!",
    "Outfly the Dragon, get the Golden Egg",
    "",
    "Click the mouse to start this level,",
    "pres 'Esacpe' to quit."
    )

    insLabels = []

    if difficulty == 4:    
        #load the music
        pygame.mixer.music.load('knife.wav')
        pygame.mixer.music.play(-1) 
        pitch = pitchBackground(2)
        for line in demt:
            tempLabel = insFont.render(line,1,(255,255,255))
            insLabels.append(tempLabel)
    elif difficulty == 5:
        #load the music
        pygame.mixer.music.load('tower.wav')
        pygame.mixer.music.play(-1) 
        pitch = pitchBackground(1)
        for line in drgn:
            tempLabel = insFont.render(line,1,(0,0,0))
            insLabels.append(tempLabel)

    allSprites = pygame.sprite.Group(pitch)

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
                boss(difficulty)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        allSprites.update()
        allSprites.draw(screen)
        
        #Display the message on the screen
        for i in range(len(insLabels)):
            screen.blit(insLabels[i],(50,30*i))

        pygame.display.flip()
#end of bossIntro method

#method that runs when gameplay is over
def gameOver(score, oppScore, health, difficulty):
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,255))
    screen.blit(background, (0,0))
    insFont = pygame.font.SysFont(None,30)

    pitch = pitchBackground(1)

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
    demtWon = (
    "You made it to the Patronus Shield!",
    "The hoard of Dementors have been run off!",
    "",
    "Click the mouse to return to game start,",
    "press 'Escape' to quit."
    )
    demtLoss = (
    "You were caught by the Dementors!",
    "Harry heard his Mother's scream before he too dies.",
    "",
    "Click the mouse to return to game start,",
    "Press 'Escape' to quit."
    )
    drgnWon = (
    "You've survived the Dragon and the First Task!!",
    "Now you have the clue to the Second Task",
    "",
    "Click the mouse to return to game start,",
    "Press 'Escape' to quit."
    )
    drgnLoss = (
    "You were killed by the dragon!",
    "Due to Harry's death the TriWizard Tournament is again banned.",
    "",
    "Click the mouse to return to game start,",
    "Press 'Escape' to quit."
    )

    insLabels = []
    #use the score to determine which ending is given to User
    if health == 0:
        if difficulty == 4:
            for line in demtLoss:
                tempLabel = insFont.render(line,1,(0,0,0))
                insLabels.append(tempLabel)
        elif difficulty == 5:
            for line in drgnLoss:
                tempLabel = insFont.render(line,1,(0,0,0))
                insLabels.append(tempLabel)
        else:
            for line in knockOut:
                tempLabel = insFont.render(line,1,(0,0,0))
                insLabels.append(tempLabel)
    elif difficulty == 4:
        for line in demtWon:
            tempLabel = insFont.render(line,1,(0,0,0))
            insLabels.append(tempLabel)
    elif difficulty == 5:
        for line in drgnWon:
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
                intro(difficulty)
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

#Method for the Splash Screen
def splash():
    pygame.display.set_caption("Quidditch")
    background = pygame.Surface(screen.get_size())
    background.fill((255,255,255))

    #Image for the splash screen
    splash = pygame.Surface((800,500))
    splash = splash.convert()
    splash = pygame.image.load("splash.png")

    screen.blit(background,(0,0))
    screen.blit(splash, (100,50))

    pygame.display.flip()

    time.sleep(8)
    intro(0)
#end of Splash Screen

#Main method    
def main():
    pygame.display.set_caption("Quidditch")
    #load the music
    pygame.mixer.music.load('earth.wav')
    pygame.mixer.music.play(-1) 
    splash()
#end of main method

if __name__ == "__main__":
    main()
