import pygame
from settings import Settings


def update_squares():
    if w > 0 and h > 0:
        squares.append(((x1, y1), (w, h)))
    if w < 0 and h < 0:
        squares.append(((x1 - abs(w), y1 - abs(h)),
                        (x1 - (x1 - abs(w)), y1 - (y1 - abs(h)))))
    if w > 0 and h < 0:
        squares.append(((x1, y1 - abs(h)), (w, y1 - (y1 - abs(h)))))
    if w < 0 and h > 0:
        squares.append(((x1 - abs(w), y1), (x1 - (x1 - abs(w)), h)))


def update_circles():
    if w > 0 and h > 0:
        circles.append(((x1, y1), (w, h)))
    if w < 0 and h < 0:
        circles.append(((x1 - abs(w), y1 - abs(h)),
                        (x1 - (x1 - abs(w)), y1 - (y1 - abs(h)))))
    if w > 0 and h < 0:
        circles.append(((x1, y1 - abs(h)), (w, y1 - (y1 - abs(h)))))
    if w < 0 and h > 0:
        circles.append(((x1 - abs(w), y1), (x1 - (x1 - abs(w)), h)))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 790
    screen = pygame.display.set_mode(size)
    x1, y1, w, h = 0, 0, 0, 0
    squares = []
    circles = []
    figure = 'square'
    pop_figure = []
    drawing = False

    running = True
    settings = Settings()
    fps = settings.fps
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
                if figure == 'square':
                    pop_figure.append('square')
                    update_squares()
                elif figure == 'circle':
                    pop_figure.append('circle')
                    update_circles()
                x1, y1, w, h = 0, 0, 0, 0
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    w, h = event.pos[0] - x1, event.pos[1] - y1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    ctrl_flag = True
                if event.key == pygame.K_z and ctrl_flag:
                    if pop_figure != []:
                        if pop_figure[-1] == 'square':
                            if len(squares) > 0:
                                squares.pop()
                                pop_figure.pop()
                        elif pop_figure[-1] == 'circle':
                            if len(circles) > 0:
                                circles.pop()
                                pop_figure.pop()
                if event.key == pygame.K_r:
                    if figure == 'square':
                        figure = 'circle'
                    elif figure == 'circle':
                        figure = 'square'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    ctrl_flag = False
        screen.fill((0, 0, 0))
        for i in squares:
            pygame.draw.rect(screen, (255, 255, 255), i, 5)
        for i in circles:
            pygame.draw.ellipse(screen, (255, 255, 255), i, 5)
        if drawing:
            if figure == 'square':
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
            elif figure == 'circle':
                if w > 0 and h > 0:
                    pygame.draw.ellipse(screen, (255, 255, 255),
                                     (x1, y1, w, h), 5)
                if w < 0 and h < 0:
                    pygame.draw.ellipse(screen, (255, 255, 255), (x1 - abs(w), y1 - abs(h), x1 - (x1 - abs(w)), y1 - (y1 - abs(h))), 5)
                if w > 0 and h < 0:
                    pygame.draw.ellipse(screen, (255, 255, 255), (x1, y1 - abs(h), w, y1 - (y1 - abs(h))), 5)
                if w < 0 and h > 0:
                    pygame.draw.ellipse(screen, (255, 255, 255), (x1 - abs(w), y1, x1 - (x1 - abs(w)), h), 5)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
