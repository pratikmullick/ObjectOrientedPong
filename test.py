from options import Configuration
import objects
import pygame
import time
import functions

confy = Configuration(".pong.conf")

pygame.init()

surface = pygame.display.set_mode((confy.width, confy.height))


select = objects.Selection(confy)
cursor = select.cursor
opening = functions.Opening(confy)
while True:
    text_init = select.position
    fps_clock = pygame.time.Clock()
    surface.fill(confy.black)
    for letter in objects.Logo(confy).logo:
        pygame.draw.lines(surface, confy.silver, False, letter, confy.line)
    for msg in select.text:
        select.font.render_to(surface, (select.starting,text_init), msg, fgcolor=confy.white)
        text_init += select.gap
        
    opening.check_event()
    if opening.state == 2:
        cursor.top = select.position + select.gap
    elif opening.state == 1:
        cursor.top = select.position
        
    if opening.state == 1 and opening.start == True:
        print("One Player Game")
        break
    elif opening.state == 2 and opening.start == True:
        print("Two Player Game")
        break
    pygame.draw.rect(surface, confy.white, cursor)
    pygame.display.update()
    fps_clock.tick(confy.fps)
