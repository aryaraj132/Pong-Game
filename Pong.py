import pygame as pg
import time
import random
import os
pg.init()

width = 800
height = 500

screen = pg.display.set_mode((width, height+150))
pg.display.set_caption("By - Aryan")

icon = pg.image.load(os.path.dirname(os.path.realpath(__file__)) + '/pong.png')
pg.display.set_icon(icon)
clock = pg.time.Clock()
font_style = pg.font.SysFont("bahnschrift", 25)
score_font = pg.font.SysFont("comicsansms", 35)
def message(msg,color,height,width):
    info = font_style.render(msg, True, color)
    screen.blit(info, [width, height+60])

boxSize = 10
panelLength = 70


def Your_score(score1,score2):
    value1 = score_font.render("Player1 Score: " + str(score1), True, (255,255,0))
    screen.blit(value1, [10, height+10])
    value2 = score_font.render("Player2 Score: " + str(score2), True, (255,255,0))
    screen.blit(value2, [width/2, height+10])

running = True
x_cod = width/2
y_cod = height/2

x_change = 0
y_change = 0

score1 = 0
score2 = 0

allowMove = 1

direction_x = 1
direction_y = 1

y1 = height/2
y2 = height/2

x1 = width-20
x2 = 10

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
    x_change = boxSize
    y_change = boxSize
    if x_cod >= width:
        x_cod=width/2
        score1+=1
    if x_cod < 0:
        x_cod=width/2
        score2+=1
    if x_cod == x2+10 and y_cod>=y2 and y_cod<=y2+70:
        direction_x=-direction_x
        allowMove=0
    if x_cod == x1 and y_cod>=y1 and y_cod<=y1+70:
        direction_x=-direction_x
        allowMove=0
    if y_cod >= height or y_cod<0:
        direction_y=-direction_y
        allowMove=1
        
    x_cod -= x_change*direction_x
    y_cod -= y_change*direction_y
    keys=pg.key.get_pressed()
    if keys[pg.K_s] and y2<height-70 and allowMove==1:
        y2+=20
    if keys[pg.K_w] and y2>0 and allowMove==1:
        y2-=20
    if keys[pg.K_UP] and y1>0 and allowMove==1:
        y1-=20
    if keys[pg.K_DOWN] and y1<height-70 and allowMove==1:
        y1+=20
    

    screen.fill((0,0,0))
    pg.draw.circle(screen,(255,255,0),[x_cod,y_cod],10)
    pg.draw.rect(screen,(255,255,255),[x1,y1,boxSize,panelLength])
    pg.draw.rect(screen,(255,255,255),[x2,y2,boxSize,panelLength])
    pg.draw.line(screen,(0,0,0),(0,height+10),(width,height+10))
    Your_score(score1,score2)
    message("Press q to quit game", (255,0,0),height,width/3)
    message("Paddle will move only after it bounces back from top or bottom", (255,0,0),height+30,20)
    pg.display.update()
    clock.tick(15)

pg.quit()
quit()
