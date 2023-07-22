from pygame import *
from time import time as timer
mixer.init()
font.init()
back = (100,100,255)
font2 = font.Font(None,30)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
clock = time.Clock()
FPS = 60
game = True
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x, size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 60:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 60:
            self.rect.y += self.speed
rack2 = Player("rack.png",30,200,10,70,10)
rack1 = Player("rack.png",520,200,10,70,10)
ball = GameSprite("tennis.png",200,200,30,50,0)
speed_x = 3
speed_y = 3
finish =False
text_win1 = font2.render("Первый игрок побеждает!",1,(255,1,1))
text_win2 = font2.render("Второй игрок побеждает!",1,(1,255,1))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        rack1.update1()
        rack2.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(rack1,ball):
            speed_x *= -1
        if sprite.collide_rect(rack2,ball):
            speed_x *= -1
        if ball.rect.y > win_height-50:
                speed_y *= -1
        if ball.rect.y < 0:
                speed_y *= -1
        if ball.rect.x < 0 :
            finish = True
            window.blit(text_win2,(180,250))
        if ball.rect.x > win_width:
            finish = True
            window.blit(text_win1,(180,250))
        rack1.reset()
        rack2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)