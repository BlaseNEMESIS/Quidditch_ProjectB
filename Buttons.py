#Source File Name: Buttons.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-06-10
#Program Description: A buttons class for import
# Will have methods to create clickable rectangle, ellipses, and texts.

# Full working method list:
#   square + text
#   circle + text
#   square
#   circle
#   text
#   alpha square
#   alpha circle
#   invisiable square

import pygame

pygame.init()

class Button:

    #a funct for square & text
    def labeledButton(self, surface, colour, length,height,x,y,text,textColour):
        self.square(surface,colour,length,height,x,y)
        self.text(surface, text, textColour,x,y,length,height)
        self.rect = pygame.Rect(x,y,length,height)
        return surface


    #a funct for circle & text
    def labeledCircle(self,surface,colour,length,height,x,y,text,textColour):
        pygame.draw.ellipse(surface, colour, (x,y,length,height),0)
        self.text(surface, text, textColour,x,y,length,height)
        self.rect = pygame.Rect(x,y,length,height)
        return surface


    #a funct for square
    def square(self, surface, colour, length, height, x, y):
        pygame.draw.rect(surface, colour, (x,y,length,height), 0)
        self.rect = pygame.Rect(x,y,length,height)
        return surface

    #a funct for circle
    def circle(self, surface, colour, length, height, x, y):
        pygame.draw.ellipse(surface, colour, (x,y,length,height),0)
        self.rect = pygame.Rect(x,y,length,height)
        return surface

    #a funct for text
    def text(self, surface, text, colour, x, y, length, height):
        size = int(length//len(text))
        font = pygame.font.SysFont("None", size)
        myText = font.render(text, 1, colour)
        # These calcs work bc text should be center on button
        # so center, use length to find mid-length
        # then find the middle of the text (should be shorter then mid-len
        # find diff btw two.  This diff must be added to x to be on button
        text_x = (length/2 - myText.get_height()/2)+x
        text_y = (height/2 - myText.get_height()/2)+y
        surface.blit(myText, (text_x,text_y))
        return surface

    #a funct for text + invisi square
    def invisiSquare(self, surface, length,height,x,y,text,textColour):
        #make the square invisible
        s = pygame.Surface((length,height))
        s.fill((255,255,255))
        s.set_alpha(1)
        pygame.draw.rect(s,(255,255,255),(x,y,length,height),1)
        self.text(surface, text, textColour,x,y,length,height)
        self.rect = pygame.Rect(x,y,length,height)
        return surface


    #an alpha square
    def alphaSquare(self, surface, colour, length, height, x, y):
        for i in range(1,10):
            s = pygame.Surface((length+(i*2), height+(i*2)))
            s.fill(colour)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, colour, (x-i,y-i,length+i,height+i),0)
            surface.blit(s,(x-i,y-i))
        pygame.draw.rect(surface, colour,(x,y,length,height),0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height),1)
        self.rect = pygame.Rect(x,y,length,height)
        return surface

    #an alpha circle
    def alphaCircle(self, surface, colour, length, height, x, y):
        for i in range(1,10):
            s = pygame.Surface((length+(i*2), height+(i*2)))
            s.fill(colour)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.ellipse(s, colour, (x-i,y-i,length+i,height+i),0)
            surface.blit(s,(x-i,y-i))
        pygame.draw.ellipse(surface, colour,(x,y,length,height),0)
        pygame.draw.ellipse(surface, (190,190,190), (x,y,length,height),1)
        self.rect = pygame.Rect(x,y,length,height)
        return surface

    def graphic(self, surface, length, height, x, y, imageFile):
        image = pygame.Surface((length,height))
        image = image.convert()
        image = pygame.image.load(imageFile)
        surface.blit(image,(x,y))
        self.rect = pygame.Rect(x,y,length,height)
        return surface
        
        
    
    def onClick(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
