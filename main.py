import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 790
    screen = pygame.display.set_mode(size)
    x1, y1, w, h = 0, 0, 0, 0
    squares = []
    circles = []
    drawing = False

    running = True
    fps = 100
    clock = pygame.time.Clock()
    ctrl_flag = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                if w > 0 and h > 0:
                    squares.append(((x1, y1), (w, h)))
                if w < 0 and h < 0:
                    squares.append(((x1 - abs(w), y1 - abs(h)),
                                    (x1 - (x1 - abs(w)), y1 - (y1 - abs(h)))))
                if w > 0 and h < 0:
                    squares.append(((x1, y1 - abs(h)), (w, y1 - (y1 - abs(h)))))
                if w < 0 and h > 0:
                    squares.append(((x1 - abs(w), y1), (x1 - (x1 - abs(w)), h)))
                x1, y1, w, h = 0, 0, 0, 0
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    w, h = event.pos[0] - x1, event.pos[1] - y1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    ctrl_flag = True
                if event.key == pygame.K_z and ctrl_flag and len(squares) > 0:
                    squares.pop(len(squares) - 1)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    ctrl_flag = False
        screen.fill((0, 0, 0))
        for i in squares:
            pygame.draw.rect(screen, (255, 255, 255), i, 5)
        if drawing:
            if w > 0 and h > 0:
                pygame.draw.rect(screen, (255, 255, 255),
                                 ((x1, y1), (w, h)), 5)
            if w < 0 and h < 0:
                pygame.draw.rect(screen, (255, 255, 255), ((
                                                               x1 - abs(w), y1 - abs(h)),
                                                           (x1 - (x1 - abs(w)), y1 - (y1 - abs(h)))), 5)
            if w > 0 and h < 0:
                pygame.draw.rect(screen, (255, 255, 255), ((
                                                               x1, y1 - abs(h)), (w, y1 - (y1 - abs(h)))), 5)
            if w < 0 and h > 0:
                pygame.draw.rect(screen, (255, 255, 255), ((
                                                               x1 - abs(w), y1), (x1 - (x1 - abs(w)), h)), 5)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
