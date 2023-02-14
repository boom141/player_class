from scripts import *
from scripts.entity.player import player
from scripts.world.map import map_manager


def main():
    last_time = time.time()

    rect = pygame.Rect(100,400,50,50)
    map = map_manager()
    player1 = player(rect,player_offset=[-16,-11])

    while 1:
        delta_time = time.time() - last_time
        delta_time *= 60
        last_time = time.time()

        SCREEN.fill((25,25,25))
        WINDOW.fill((25,25,25))

        map.render_tiles(SCREEN)

        player1.controller(delta_time,map.tile_rects)
        player1.player_event_handler()
        player1.player_particles(SCREEN)
        player1.render(SCREEN,delta_time)

        # SCREEN.blit(pygame.transform.scale(WINDOW, SCREEN_DIMENSION),(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(FPS)


if __name__ == "__main__":
    main()