import pygame as pg

print('hello world!')

pg.init()
pg.mixer.init()
pg.mixer.music.load('ummu.wav')

running = True
while running:
    pg.display.set_mode(size=(800,600))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                pg.mixer.music.play()
                print('music will now start')
