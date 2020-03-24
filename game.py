#запуск пуп гейма=========================================

import pygame
import random
pygame.init()

#загрузка==================================================

def text (tex, rad, color):
    font2 = pygame.font.SysFont("FixEye", rad)
    text = font2.render(tex, True,color)
    textv_rect = text.get_rect()
    text_rect = text.get_rect().centerx
    return text

# получаем разрешение монитора
infoObject = pygame.display.Info()
x_size = infoObject.current_w
y_size = infoObject.current_h

#sc = pygame.display.set_mode ([1600,900], pygame.FULLSCREEN)
# делаем окно как монитор
sc = pygame.display.set_mode ([x_size, y_size], pygame.FULLSCREEN)

sc.blit(text("загрузка", 150, (255,255,255)), (300, 300))
pygame.display.update()

#классы====================================================

class meu (): #класс назван meu потому что кагда я писал menu он выдавал ошибку
    def __init__ (self, images):
        self.stage = 0
        self.images = images
        self.sprite = []
        self.colors= [(173, 199, 195), (139, 156, 158), (222, 184, 126)]

    def tooch(self, x, y, x1, y1):
        if pygame.mouse.get_pos()[0] > x and pygame.mouse.get_pos()[0] < x1 and pygame.mouse.get_pos()[1]>y and pygame.mouse.get_pos()[1] < y1 :
            return True
        else:
            return False

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
            if  self.tooch(860, 500, 1080, 540) and moused:
                self.stage = 1
            if  self.tooch(860, 550, 1080, 590) and moused:
                self.stage = 2
            if  self.tooch(860, 600, 1080, 640) and moused:
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

        if self.stage == 1:
            pygame.draw.rect(sc, self.colors[1], (0, 0, 1920, 1080))
            sc.blit(text("выбор персонажа", 70, (255,255,255)), (750, 250))
            if self.tooch(650, 300, 850, 700):
                pygame.draw.rect(sc, self.colors[2], (650, 300, 200, 400))
                sc.blit(text("антон", 70, (255,255,255)), (880, 710))
                sc.blit(text("занимаеться радиотехникой. может создовать особые предметы", 40, (255,255,255)), (480, 765))
            else:
                pygame.draw.rect(sc, self.colors[0], (650, 300, 200, 400))
            if self.tooch(1050, 300, 1250, 700):
                pygame.draw.rect(sc, self.colors[2], (1050, 300, 200, 400))
                sc.blit(text("наста", 70, (255,255,255)), (880, 710))
                sc.blit(text("атлетка. быстр бегает", 40, (255,255,255)), (800, 765))
            else:
                pygame.draw.rect(sc, self.colors[0], (1050, 300, 200, 400))
            sc.blit(self.sprite[1],  (650, 300))
            sc.blit(self.sprite[2],  (1050, 300))
            if self.tooch(650, 300, 850, 700) and moused:
                self.stage = 4
    def ch_start (self):
            return self.stage

class object ():
    def __init__(self, x, y, xw, yw, xr , yr, sprite):
        self.pos = [x, y, xw, yw, xr , yr]
        self.sprite = pygame.image.load(sprite)
        self.cam_move = [0, 0]
    def cam (self, xm, ym):
        self.cam_move[0] += xm
        self.cam_move[1] += ym
    def render (self):
        for x in range (0, self.pos[4]):
            for y in range (0, self.pos[5]):
                sc.blit(self.sprite,  (self.pos[0]+(self.pos[2]*x)+self.cam_move[0], self.pos[1]+(self.pos[3]*y)+self.cam_move[1]))

class square (): #просто вспомогательный класс
    def __init__ (self, x, y, xx, yy ,color):
        self.pos = (x, y, xx, yy)
        self.color = color
        self.cam_move = [0, 0]
    def cam (self, xm, ym):
        self.cam_move[0] += xm
        self.cam_move[1] += ym
    def render(self):
        pygame.draw.rect(sc, self.color, (self.pos[0]+self.cam_move[0],self.pos[1]+self.cam_move[1], self.pos[2], self.pos[3]))

class player ():
    def __init__(self, x, y, xx, yy, sprite):
        self.pos = [x, y, xx, yy]
        self.forcam = 0
        self.images = sprite
        self.anim_co = 0
        self.sanim = 1
        self.sprite = []
        self.forward = 1
        self.post = 0
        self.grav = 0
        self.cam_move = [0, 0]
        self.bp = [x, y]
    def imp(self):
        for x in range (0, len(self.images)):
            self.sprite.append(pygame.image.load(self.images[x]))
    def render (self,  mode, falling):
        self.anim_co += 1
        self.sanim = mode

        if self.anim_co > 60:
            self.anim_co = 0

        if self.sanim == 0:
            self.grav+=0.4
            self.keys = pygame.key.get_pressed()
            if self.keys [pygame.K_a]:
                self.pos[0] += -4
                self.forcam = -4
                self.forward=0
                self.post = 3
                if int(self.anim_co / 15) == 1 or int(self.anim_co / 15) == 3:
                    sc.blit(self.sprite[3],  (self.pos[0]+self.cam_move [0], self.pos[1]+self.cam_move [1]))
                elif self.anim_co / 15 == 2:
                    sc.blit(self.sprite[5],  (self.pos[0]+self.cam_move [0], self.pos[1]+self.cam_move [1]))
                else:
                    sc.blit(self.sprite[7],  (self.pos[0]+self.cam_move [0], self.pos[1]+self.cam_move [1]))
            elif self.keys [pygame.K_d]:
                self.pos[0] += 4
                self.forcam = 4
                self.post = 2
                if int(self.anim_co / 15) == 1 or int(self.anim_co / 15) == 3:
                    sc.blit(self.sprite[2],  (self.pos[0]+self.cam_move [0], self.pos[1]+self.cam_move [1]))
                elif self.anim_co / 15 == 2:
                    sc.blit(self.sprite[4],  (self.pos[0]+self.cam_move [0], self.pos[1]+self.cam_move [1]))
                else:
                    sc.blit(self.sprite[6],  (self.pos[0]+self.cam_move [0], self.pos[1]+self.cam_move [1]))
            else:
                self.forcam = 0
                if self.forward:
                    sc.blit(self.sprite[1],  (self.pos[0]+self.cam_move [0], self.pos[1]+self.cam_move [1]))
                else:
                    sc.blit(self.sprite[self.post],  (self.pos[0]+self.cam_move [0], self.pos[1]+self.cam_move [1]))
            if falling:
                self.grav = 0

            self.pos[1] += self.grav

            if self.keys [pygame.K_SPACE]:
                self.pos[1] -=13
        elif self.sanim == 1:
            self.forcam = 0
            sc.blit(self.sprite[0],  (self.pos[0]+self.cam_move [0], self.pos[1]+self.cam_move [1]))

    def ch_an (self):
        return self.sanim
    def cam (self, x, y):
        self.cam_move [0] += x
        self.cam_move [1] += y

class dialogue ():
    def __init__(self, text):
        self.text = text
    def render (self, text_count):
        pygame.draw.rect(sc, (88, 90, 99), (0, 720, 1920, 400))
        if len(self.text [text_count]) > 20:
            for f in range (0, int(len(self.text [text_count]) / 80)):
                sc.blit(text(self.text [text_count][80*f:80*(f+1)], 40, (255,255,255)), (230, 750+f*50))
        else:
            sc.blit(text(self.text [text_count], 40, (255,255,255)), (230, 750))

class material (object):
    def tooch(self, pos):
        if  pos[1]>self.pos[1]+(self.pos[3]) or pos[0]+pos[2]<self.pos[0] or self.pos[1]>pos[1]+pos[3] or pos[0]>self.pos[0]+(self.pos[2]):
            return True
        else:
            return False

class inv_box ():#невидимая коробка
    def __init__(self, x, y, xx, yy):
        self.pos = [x, y, xx, yy]
        self.cam_move =[0, 0]
    def tooch(self, pos):
        if  pos[1]>self.pos[1]+(self.pos[3]) or pos[0]+pos[2]<self.pos[0] or self.pos[1]>pos[1]+pos[3] or pos[0]>self.pos[0]+(self.pos[2]):
            return True
        else:
            return False
    def cam (self, xm, ym):
        self.pos[0] += xm
        self.pos[1] += ym

class trimer ():#при timer не работало
    def __init__ (self, long):
        self.count = long*60
        self.start = long*60
    def time (self):
        if self.count>0:
            self.count-=1
        return self.count
    def restart (self):
        self.count = self.start

class hitbox ():
    def __init__ (self, x, y ,xx, yy):
        self.pos = [x, y, xx, yy]

    def move (self ,x, y):
        self.pos[0] = x
        self.pos[1] = y

    def position(self):
        return self.pos

class inventory():
    def __init__(self, size, items):
        self.size = size
        self.inv = []
        self.unimp = items
        self.sprite =  []
        self.added = False
        for v in range(0, self.size):
            self.inv.append(0)

    def imp (self):
        for x in range (0, len(self.unimp)):
            self.sprite.append(pygame.image.load(self.unimp[x]))

    def render (self):
        for g in range(0, self.size):
            pygame.draw.rect(sc, (173, 199, 195), (200+g*100, 114, 80, 80))
            sc.blit(self.sprite[self.inv[g]],  (200+g*100, 114))
    def add (self, adding):
        if min(self.inv)< 1:
            for f in range(0, self.size):
                if self.inv[f] == 0 and self.added == False:
                    self.inv[f] = adding
                    self.added = True
            self.added = False

#изображеня==================================================

bg = [(".\\bg\\MENU BG.png"), (".\\obj\\abr\\adr-choose.png"), (".\\obj\\nst\\nst-choose.png")]
furniture = [(".\\obj\\frnt\\chair home.png"), (".\\obj\\frnt\\tumb home.png"),
(".\\obj\\frnt\\scaf home.png"), (".\\obj\\frnt\\window home.png"), (".\\obj\\frnt\\fridge home.png"),
 (".\\obj\\frnt\\oven home.png"), (".\\obj\\frnt\\range hood.png"), (".\\obj\\frnt\\boots1.png")]
abr = [(".\\obj\\abr\\adr-sit.png"), (".\\obj\\abr\\adr-front.png"),
 (".\\obj\\abr\\adr-right1.png"), (".\\obj\\abr\\adr-left1.png"),
 (".\\obj\\abr\\adr right2.png"), (".\\obj\\abr\\adr-left2.png"),
 (".\\obj\\abr\\adr right3.png"), (".\\obj\\abr\\adr-left3.png")]
items = [".\\obj\\none.png",".\\items\\food\\sosige-1.png"]

#переменные==================================================

menu = True
moused = False
keep_going = True
timer = pygame.time.Clock()
g_mode = 2
p_mode = 1
textes = ["""что случилось ? """]
dio = 0

 #объекты======================================================

mian_menu = meu(bg)
mian_menu.imp()
playerr = player(850, 450, 113, 300, abr)
playerr.imp()
win = dialogue(textes)
timerr1 = trimer(0.1)#здесь должно быть 2 но для отладки сделал меньше
sit = trimer(1)
down = hitbox(850, 650, 113, 100)
my = inventory(5, items)
my.imp()
S_fall = False
ocam = 0
ncam = 850
de = False
crutch1 = 1

    #1 комната================================================
window1 = object(650, 400, 100, 150, 1, 1, furniture[3])
windowb1 = square(650, 400, 100, 150,(20, 20, 30))
window2 = object(950, 400, 100, 150, 1, 1, furniture[3])
windowb2 = square(950, 400, 100, 150,(20, 20, 30))
frige1 = object(-500, 320, 300, 150, 1, 1, furniture[4])
chair1 = object(800, 550, 300, 150, 1, 1, furniture[0])
scaf1 = object(1150, 320, 300, 150, 1, 1, furniture[2])
tumb1 = object(690, 575, 300, 150, 1, 1, furniture[1])
oven1 = object(-345, 520, 300, 150, 1, 1, furniture[5])
fridge1 = object(-345, 340, 300, 150, 1, 1, furniture[6])
boots1 = object(1900, 640, 300, 150, 1, 1, furniture[7])

flor1 = square(-600, 600, 3220, 980, (116, 124, 130))
flor2 = square(-600, 800, 3220, 980, (104, 112, 117))

wall1 = square(200, 0, 1520, 600, (168, 167, 162))
wall2 = square(200, 0, 1520, 200, (158, 157, 152))
wall3 = square(-600, 0, 800, 600, (197, 203, 212))
wall4 = square(-600, 0, 800, 200, (184, 187, 191))
wall5 = square(175, 0, 50, 700, (184, 187, 191))
wall6 = square(1720, 0, 900, 600, (158, 112, 77))
wall7 = square(1720, 0, 900, 200, (128, 96, 73))
wall8 = square(1695, 0, 50, 700, (158, 157, 152))
wall9 = square(2920, 0, 50, 700, (128, 96, 73))


flor_box = inv_box(-4800, 750, 20200, 980)
interactive_chair = inv_box(650, 700, 330, 50)
fridgei = inv_box(-1900, 340, 300, 150)

interr1 = [interactive_chair, fridgei, flor_box]

interactives = [interr1]

room1 = [flor1, flor2, wall1, wall2,
wall3, wall4, wall5,windowb2, window2, frige1,
oven1, fridge1, boots1,
windowb1, window1, scaf1, tumb1, chair1, wall6, wall7, wall8]

rooms = [room1]

#ГЛАВНЫЙ ЦИКЛ================================================

while keep_going:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            keep_going = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            moused = True
        elif event.type == pygame.MOUSEBUTTONUP:
            moused = False

    if keys[pygame.K_e]:
        crutch1 += 1
    else:
        crutch1 = 0
    if crutch1 == 1:
        de = True
    else:
        de = False


    ocam = ncam
    ncam = playerr.pos[0]


    if not mian_menu.ch_start() == 4:
        mian_menu.render(moused)
    else:
        sc.fill((0, 0, 0))
        for g in range(0, len(rooms[0])):
            rooms[0][g].render()
        playerr.render(p_mode, S_fall)

        if playerr.cam_move[0] > -1050:
            for g in range(0, len(rooms[0])):
                rooms[0][g].cam(-(playerr.forcam), 0)
            for g in range(0, len(interactives[0])):
                interactives[0][g].cam(-(playerr.forcam), 0)
            playerr.cam(-(playerr.forcam), 0)
        #else :
            #playerr.cam(-(playerr.forcam), 0)


        down.move(playerr.pos[0], playerr.pos[1]+200)

        if flor_box.tooch(down.pos):
            S_fall = False
        else:
            S_fall = True
        if flor_box.tooch(down.pos):
            S_fall = False

        if timerr1.time()==1:
            dio = 1

        if dio == 1:
            win.render(0)
            if keys[pygame.K_f]:
                dio = 0
        if  sit.time()==0:
            if p_mode >0 and keys[pygame.K_e]:
                p_mode = 0
                sit.restart()


            elif de and p_mode == 0:
                if not interactive_chair.tooch(playerr.pos):
                    p_mode = 1
                    sit.restart()
                elif not fridgei.tooch(playerr.pos):
                    my.add(1)
        my.render()
        print (de)
        sc.blit(text(str(crutch1), 50, (255,255,255)), (875, 500))

    pygame.display.update()
    timer.tick(60)
