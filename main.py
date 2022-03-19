
class Hero(pygame, sprite.Sprite):
    def __init__(self, filename, speed_x=0, speed_y=0, x=start_x, y=start_y, width=100, height=100):
        pygame.srite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.stands_on = False
    def gravitate(self):
        self.speed_y += 0.25
    def jump(self, y):
        if self.stands_on:
            self.speed_y = y

    def update(self):
        self.rect.x += self.speed_x
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.speed_x > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.speed_x < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.gravitate()

        self.rect.y += self.speed_y
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.speed_y > 0:
            for p in platforms_touched:
                self.speed_y = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
                    self.stands_on = p
                elif self.speed_y < 0:
                    self.stands_on = False
                    for p in platform_touched:
                        self.speed_y = 0
                        self.rect.top = max(self.rect.top, p.rect.bottom)
                
            