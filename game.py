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

sc = pygame.display.set_mode ([1920,1080], pygame.FULLSCREEN)

sc.blit(text("загрузка", 150, (255,255,255)), (300, 300))
pygame.display.update()

#классы====================================================

class meu ():
    def __init__ (self, images):
        self.stage = 0
        self.images = images
        self.sprite = []
        self.colors= [(173, 199, 195), (139, 156, 158)]

    def imp(self):
        for x in range (0, len(self.images)):
            self.sprite.append(pygame.image.load(self.images[x]))
    def render (self, moused):
        if self.stage == 0:
            sc.blit(self.sprite[0],  (0, 0))
            pygame.draw.rect(sc, self.colors[0], (860, 500, 220, 40))
            pygame.draw.rect(sc, self.colors[0], (860, 550, 220, 40))
            pygame.draw.rect(sc, self.colors[0], (860, 600, 220, 40))
            sc.blit(text("новая игра", 50, (255,255,255)), (875, 500))
            sc.blit(text("настройки", 50, (255,255,255)), (880, 550))
            sc.blit(text("выйти", 50, (255,255,255)), (910, 600))
            if pygame.mouse.get_pos()[0] > 860 and pygame.mouse.get_pos()[0] <1080:
                if pygame.mouse.get_pos()[1]>500 and pygame.mouse.get_pos()[1] <540 and moused:
                    self.stage = 1
                if pygame.mouse.get_pos()[1]>550 and pygame.mouse.get_pos()[1] <590 and moused:
                    self.stage = 2
                if pygame.mouse.get_pos()[1]>600 and pygame.mouse.get_pos()[1] <640 and moused:
                    self.stage = 3


        if self.stage == 2:
            sc.blit(self.sprite[0],  (0, 0))
            pygame.draw.rect(sc, self.colors[1], (400, 200, 1120, 680))
            sc.blit(text("настройки", 70, (255,255,255)), (850, 250))
            sc.blit(text("выйти", 40, (255,255,255)), (1250, 260))
            if pygame.mouse.get_pos()[0] > 1250 and pygame.mouse.get_pos()[0] <1350:
                if pygame.mouse.get_pos()[1]>260 and pygame.mouse.get_pos()[1] <310 and moused:
                    self.stage = 0

        if self.stage == 3:
            pygame.quit()





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

    mian_menu.render(moused)

    pygame.display.update()
