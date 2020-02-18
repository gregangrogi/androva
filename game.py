#запуск пуп гейма=========================================

import pygame
pygame.init()

#загрузка==================================================

def text (tex, rad, color):
    font2 = pygame.font.SysFont("FixEye", rad)
    text = font2.render(tex, True,color)
    text_rect = text.get_rect()
    text_rect = text.get_rect().centerx
    return text

sc = pygame.display.set_mode ([1280,720])

sc.blit(text("загрузка", 150, (255,255,255)), (300, 300))
pygame.display.update()

#классы====================================================

class meu ():
    def __init__ (self, images):
        self.stage = 0
        self.images = images
        self.sprite = []

    def imp(self):
        for x in range (0, len(self.images)):
            self.sprite.append(pygame.image.load(self.images[x]))
    def render (self):
        if self.stage == 0:
            sc.blit(self.sprite[0],  (0, 0))
            pygame.draw.rect(sc, (173, 199, 195), (510, 300, 220, 40))

        #if


#изображеня==================================================

bg = [(".\\bg\\MENU BG.png")]

#переменные==================================================

menu = True
moused = False
keep_going = True

 #объекты======================================================

mian_menu = meu(bg)
mian_menu.imp()


#ГЛАВНЫЙ ЦИКЛ================================================

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            moused = True
        if event.type == pygame.MOUSEBUTTONUP:
            moused = False

    mian_menu.render()
    sc.blit(text("новая игра", 50, (255,255,255)), (525, 300))
    pygame.display.update()
