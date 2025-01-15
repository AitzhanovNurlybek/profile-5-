import pygame, sys, os
pygame.init()
clock = pygame.time.Clock()

size = (450, 600)
screen = pygame.display.set_mode(size,flags=pygame.NOFRAME)
pygame.display.set_caption('Yandex')

background_img = pygame.image.load("../image/n8te0prpeq0yrxf25tbt5bt2af5b9ht3.png")
image = pygame.image.load("../image/1.png")
music = [f.name for f in os.scandir('.') if f.is_file() and f.name.endswith('.mp3')]
font = pygame.font.SysFont('Tahoma', 19, True)

surf_1 = pygame.Surface((380, 55))
surf_1.blit(background_img, (0, 0))

is_playing = False
begin = False
i, vol = 0, 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                begin = True
                pygame.mixer.music.load(music[i])
                pygame.mixer.music.play()
                i = 0

            if event.key == pygame.K_SPACE and begin:
                if not is_playing:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()

            if event.key == pygame.K_RIGHT and begin:
                i = (i + 1) % len(music)
                pygame.mixer.music.load(music[i])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT and begin:
                i = (i - 1) % len(music)
                pygame.mixer.music.load(music[i])
                pygame.mixer.music.play()

            if event.key == pygame.K_UP:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)

            if event.key == pygame.K_DOWN:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)

            is_playing = pygame.mixer.music.get_busy()

    screen.blit(background_img, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(surf_1, (33, 395))

    s = font.render(music[i][:-4], True, 'white') 
    screen.blit(s, (78, 405))

    clock.tick(144)
    pygame.display.flip()