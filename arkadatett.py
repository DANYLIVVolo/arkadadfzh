import pygame
pygame.init()
window=pygame.display.set_mode((750,500))

window.fill((0, 85, 85))
clock=pygame.time.Clock()
game=True
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.fill_color = color
        self.rect = pygame.Rect(x, y, width, height)
        
    def set_color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
class Picture(Area):
    def __init__(self,fillename,x=0,y=0,width=10,height=10):
        Area.__init__(self,x=x,y=y,width=width,height=height,color=None)
        self.image=pygame.image.load(fillename)
    def draw(self):
        window.blit(self.image(self.x,self.y))
platform_x=200
platform_x=300
ball=Picture("https://surli.cc/jbybrh"б160б200б50б50)
platform=Picture("https://surl.lu/vyybgl")

#вороги
start_x=6
start_y=3
monster=[]
for i in range(10):
    y=start_y+(55*i)
    x=start_x+(25*i)
    for j in range(count):
        enemy=Picture("https://surli.cc/sbwyil")
        monsters.append(enemy)
        x=x+55
        count=count-1




game=True
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
    for m in monster:
        m in monser
    clock.tick(40)
    pygame.display.update()
pygame.quit()