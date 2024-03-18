import pygame
import sys
from settings import *
from car import Car
from obs import Obstacle
from text_obj import Text_Obj
from text_ob import Text_Ob
from bg import Background
from lol import Lol
# создание объектов
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()

ddd = 0
#groops
all_sprites = pygame.sprite.Group()
items = pygame.sprite.Group() 

car = Car(PLAYER_Y, PLAYER_X, 'zane.png', pygame.K_RIGHT, pygame.K_LEFT)
all_sprites.add(car)

##lol = Lol(pygame.K_DOWN, ddd)


for i in range(5):
    obs = Obstacle('flower.png', True)
    all_sprites.add(obs)
    items.add(obs)
for i in range(2):
    obs = Obstacle('fire.png', False)
    all_sprites.add(obs)
    items.add(obs)

game_over_bg = Background("game_over.jpg")

game_start_bg = Background("start.jpg")

#peremenn

score = 0
health = 100
score_text = Text_Obj(10,10, str(score), screen)
health_text = Text_Ob(745, 10, str(health), screen)






print("hi")
            
run = True

while True:
    for i in pygame.event.get():
        if ddd == 0:
            screen.fill(BLACK)
            game_start_bg.draw(screen)
            pygame.display.update()
        if ddd == 1:
            screen.fill(BLACK)
            car.draw(screen)
            all_sprites.draw(screen)
            score_text.draw()
            health_text.draw()
            pygame.display.update()


##    keys = pygame.key.get_pressed()
##    if keys[self.down_key]:
##        self.rect.ddd = 1

# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # изменение объектов, update
    all_sprites.update()
    score_text.update(score)
    if health <= 0:
        run = False   
    car.update()
    all_sprites.update()
    score_text.update(score)
    health_text.update(health)



    #пересечение объектов, collisions
    eats = pygame.sprite.spritecollide(car, items, True)
    for eat in eats:
        if eat.get_edible() == True:
            score += 1
            obs = Obstacle('flower.png', True)
            all_sprites.add(obs)
            items.add(obs)

        if eat.get_edible() == False:
            health -= 10
            obs = Obstacle('fire.png', False)
            all_sprites.add(obs)
            items.add(obs)

##        if health == 0:
##            pygame.quit()
##            sys.exit()


    # обновление экрана
    screen.fill(BLACK)
    car.draw(screen)
    all_sprites.draw(screen)
    score_text.draw()
    health_text.draw()
    pygame.display.update()
while True:
    for i in pygame.event.get():
        if run == False:
            screen.fill(BLACK)
            game_over_bg.draw(screen)
            pygame.display.update()
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    

    


