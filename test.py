from options import Configuration
import objects
import pygame

confy = Configuration()
select = objects.Selection(confy)

pygame.init()
fps_clock = pygame.time.Clock()
surf = pygame.display.set_mode((confy.width, confy.height))
surf.fill((0, 0, 0))

for i in range(4):
    pygame.draw.lines(surf, confy.white, False, objects.Logo(confy).logo[i], 12)
for msg in select.text:
    select.font.render_to(surf, (select.starting, select.position), msg, fgcolor=confy.silver)
    select.position += select.gap

pygame.display.update()
fps_clock.tick(confy.fps)