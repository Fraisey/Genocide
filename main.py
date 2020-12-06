import pygame
import os
pygame.font.init()

# Load images
PLAYER = pygame.image.load(os.path.join("assets", "player.png"))
BG1 = pygame.image.load(os.path.join("assets", "fazolis.png"))
MINATO1 = pygame.image.load(os.path.join("assets", "minato1.png"))

WIDTH, HEIGHT = 1200, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Genocide 2")

class Characters:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.character_img = None
        self.projectile_img = None
        self.projectile = []
        self.cooldown_counter = 0

    def draw(self, window):
        window.blit(self.character_img, (self.x, self.y))

    def get_height(self):
        return self.character_img.get_height()

    def get_health(self):
        return self.health

class Player(Characters):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.character_img = PLAYER
        self.mask = pygame.mask.from_surface(self.character_img)
        self.max_health = health



class Enemy1(Characters):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.character_img = MINATO1
        self.mask = pygame.mask.from_surface(self.character_img)
        self.max_health = health

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    volume = 100
    phealth_font = pygame.font.SysFont("timesnewroman", 32)
    ehealth_font = pygame.font.SysFont("timesnewroman", 42)

    player_vel = 7

    player = Player(20, 300)
    enemy1 = Enemy1(780, 100)

    def redraw_window():
        WIN.blit(BG1, (0, 0))
        # Draw text
        phealth_label = phealth_font.render(f"{player.get_health()}", 1, (255, 255, 255))
        ehealth_label = ehealth_font.render(f"{enemy1.get_health()}", 1, (255, 255, 255))
        volume_label = phealth_font.render(f"{volume}", 1, (255, 255, 255))

        WIN.blit(phealth_label, (165, 11))
        WIN.blit(ehealth_label, (1100, 1))
        WIN.blit(volume_label, (275, 853))

        player.draw(WIN)
        enemy1.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y > 0: #up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player.get_height() < HEIGHT: # down
            player.y += player_vel

main()