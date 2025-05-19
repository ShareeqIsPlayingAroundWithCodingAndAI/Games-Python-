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
RED = (255, 0, 0)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)

# Player class
class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += self.speed

    def draw(self):
        SCREEN.blit(self.image, self.rect)

# Block class
class Block:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(random.randint(0, SCREEN_WIDTH-50), 0))
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.reset()

    def reset(self):
        self.rect.y = 0
        self.rect.x = random.randint(0, SCREEN_WIDTH-50)
        self.speed = random.randint(2, 5)

    def draw(self):
        SCREEN.blit(self.image, self.rect)

# Main game class
class Game:
    def __init__(self):
        self.player = Player()
        self.blocks = [Block() for _ in range(5)]
        self.score = 0

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

            for block in self.blocks:
                block.update()
                block.draw()
                if self.player.rect.colliderect(block.rect):
                    running = False
                    self.game_over()

            self.score += 1
            self.show_score()

            pygame.display.flip()
            clock.tick(FPS)

    def show_score(self):
        score_text = font.render("Score: " + str(self.score), True, WHITE)
        SCREEN.blit(score_text, (10, 10))

    def game_over(self):
        game_over_text = font.render("Game Over! Your Score: " + str(self.score), True, RED)
        SCREEN.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2000)

# Create and run the game instance
if __name__ == '__main__':
    game = Game()
    game.run()

