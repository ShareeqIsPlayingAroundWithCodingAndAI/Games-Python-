import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Load images
spaceship_img = pygame.image.load('spaceship.png')  # Add path to your spaceship image
asteroid_img = pygame.image.load('asteroid.png')    # Add path to your asteroid image
star_img = pygame.image.load('star.png')            # Add path to your star image

# Player class
class Player:
    def __init__(self):
        self.image = pygame.transform.scale(spaceship_img, (50, 50))
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 10))
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self):
        SCREEN.blit(self.image, self.rect)

# Falling objects class
class FallingObject:
    def __init__(self, img):
        self.image = pygame.transform.scale(img, (30, 30))
        self.rect = self.image.get_rect(midtop=(random.randint(0, SCREEN_WIDTH), 0))
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def reset(self):
        self.rect.midtop = (random.randint(0, SCREEN_WIDTH), 0)
        self.speed = random.randint(3, 6)

    def draw(self):
        SCREEN.blit(self.image, self.rect)

# Main game class
class Game:
    def __init__(self):
        self.player = Player()
        self.asteroids = [FallingObject(asteroid_img) for _ in range(5)]
        self.stars = [FallingObject(star_img) for _ in range(3)]
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            SCREEN.fill(BLACK)
            self.player.move()
            self.player.draw()

            for asteroid in self.asteroids:
                asteroid.update()
                asteroid.draw()
                if self.player.rect.colliderect(asteroid.rect):
                    running = False
                    self.game_over()

            for star in self.stars:
                star.update()
                star.draw()
                if self.player.rect.colliderect(star.rect):
                    self.score += 10
                    star.reset()

            self.show_score()

            pygame.display.flip()
            clock.tick(FPS)

    def show_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))

    def game_over(self):
        game_over_text = self.font.render("Game Over!", True, GREY)
        SCREEN.blit(game_over_text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)

# Create and run the game instance
if __name__ == '__main__':
    game = Game()
    game.run()
