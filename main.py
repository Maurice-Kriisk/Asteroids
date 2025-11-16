import pygame
from constants import *
from logger import log_state
from player import *
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entities in updatable:
            entities.update(dt)
        for drawables in drawable:
            drawables.draw(screen)
        screen.fill("black")
        player.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
