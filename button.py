import pygame

class Button:
    def __init__(self, x, y, image1, image2, scale):
        width = image1.get_width()
        height = image1.get_height()
        self.image1 = pygame.transform.scale(image1, (int(width * scale), int(height * scale)))
        self.image2 = pygame.transform.scale(image2, (int(width * scale), int(height * scale)))
        self.rect = self.image1.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.hover = False
        
    def draw(self, surface):
        action = False
        self.hover = False
        
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check if mouse collides with button
        if self.rect.collidepoint(pos):
            self.hover = True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
            
        if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
            self.clicked = False
                
        #draw button on screen
        if self.hover:
            surface.blit(self.image2, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.image1, (self.rect.x, self.rect.y))
        
        return action