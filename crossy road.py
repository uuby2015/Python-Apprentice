import pygame
import random

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
GREEN = (0, 255, 0)

# Game constants
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_SPEED = 3
PIPE_WIDTH = 70
PIPE_GAP = 150

# Fonts
font = pygame.font.SysFont("Arial", 32)

class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.width = 34
        self.height = 24
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.y = int(self.y)

    def draw(self):
        pygame.draw.rect(screen, BLACK, self.rect)

class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.top_height = random.randint(50, HEIGHT - PIPE_GAP - 50)
        self.bottom_height = HEIGHT - self.top_height - PIPE_GAP
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.top_height)
        self.bottom_rect = pygame.Rect(self.x, HEIGHT - self.bottom_height, PIPE_WIDTH, self.bottom_height)
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = int(self.x)
        self.bottom_rect.x = int(self.x)

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = []
    score = 0

    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1500)

    running = True
    while running:
        clock.tick(60)
        screen.fill(SKY_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
            if event.type == SPAWNPIPE:
                pipes.append(Pipe())

        bird.update()
        bird.draw()

        for pipe in pipes:
            pipe.update()
            pipe.draw()

            # Collision check
            if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                running = False

            # Scoring
            if not pipe.passed and pipe.x + PIPE_WIDTH < bird.x:
                pipe.passed = True
                score += 1

        # Remove pipes off screen
        pipes = [pipe for pipe in pipes if pipe.x + PIPE_WIDTH > 0]

        # Check if bird hit ground or flew off screen
        if bird.y > HEIGHT or bird.y < 0:
            running = False

        # Draw score
        score_surface = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_surface, (10, 10))

        pygame.display.flip()

    # Game Over screen
    screen.fill(WHITE)
    game_over_surface = font.render("Game Over!", True, BLACK)
    final_score_surface = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(game_over_surface, (WIDTH//2 - game_over_surface.get_width()//2, HEIGHT//3))
    screen.blit(final_score_surface, (WIDTH//2 - final_score_surface.get_width()//2, HEIGHT//2))
    pygame.display.flip()
    pygame.time.delay(3000)

    pygame.quit()

if __name__ == "__main__":
    main()