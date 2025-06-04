import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Crossy Road")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (100, 100, 100)

# Grid setup
GRID_SIZE = 50  # Each square size
ROWS = HEIGHT // GRID_SIZE
COLS = WIDTH // GRID_SIZE

# Player class
class Player:
    def __init__(self):
        self.x = COLS // 2
        self.y = ROWS - 1
        self.rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)

    def move(self, dx=0, dy=0):
        new_x = self.x + dx
        new_y = self.y + dy
        # Stay within bounds
        if 0 <= new_x < COLS and 0 <= new_y < ROWS:
            self.x = new_x
            self.y = new_y
            self.rect.topleft = (self.x * GRID_SIZE, self.y * GRID_SIZE)

    def draw(self):
        pygame.draw.rect(SCREEN, GREEN, self.rect)

# Car class
class Car:
    def __init__(self, y, speed, direction):
        self.y = y
        self.speed = speed
        self.direction = direction  # 1 = right, -1 = left
        if direction == 1:
            self.x = -1  # start offscreen left
        else:
            self.x = COLS  # start offscreen right
        self.width = 2  # cars occupy 2 grid squares
        self.rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, self.width * GRID_SIZE, GRID_SIZE)

    def update(self):
        self.x += self.speed * self.direction
        self.rect.x = int(self.x * GRID_SIZE)

    def offscreen(self):
        # Check if car is fully off screen
        if self.direction == 1:
            return self.x * GRID_SIZE > WIDTH
        else:
            return (self.x + self.width) * GRID_SIZE < 0

    def draw(self):
        pygame.draw.rect(SCREEN, RED, self.rect)

def main():
    clock = pygame.time.Clock()
    player = Player()

    # Lanes: y positions for cars (rows 1 to ROWS-2 are lanes)
    lanes = list(range(1, ROWS - 1))
    cars = []
    spawn_delay = 0
    score = 0

    run = True
    while run:
        clock.tick(60)
        SCREEN.fill(GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move(dy=-1)
                elif event.key == pygame.K_DOWN:
                    player.move(dy=1)
                elif event.key == pygame.K_LEFT:
                    player.move(dx=-1)
                elif event.key == pygame.K_RIGHT:
                    player.move(dx=1)

        # Spawn cars randomly
        spawn_delay += 1
        if spawn_delay > 30:
            spawn_delay = 0
            lane = random.choice(lanes)
            speed = random.uniform(0.05, 0.12)
            direction = random.choice([-1, 1])
            cars.append(Car(lane, speed, direction))

        # Update cars
        for car in cars:
            car.update()

        # Remove offscreen cars
        cars = [car for car in cars if not car.offscreen()]

        # Draw lanes (optional grid lines)
        for y in range(ROWS):
            pygame.draw.line(SCREEN, BLACK, (0, y * GRID_SIZE), (WIDTH, y * GRID_SIZE))
        for x in range(COLS):
            pygame.draw.line(SCREEN, BLACK, (x * GRID_SIZE, 0), (x * GRID_SIZE, HEIGHT))

        # Draw cars
        for car in cars:
            car.draw()

        # Draw player
        player.draw()

        # Collision detection
        for car in cars:
            if player.rect.colliderect(car.rect):
                # Reset game on collision
                player = Player()
                cars.clear()
                score = 0

        # Check if player reached top (safe crossing)
        if player.y == 0:
            score += 1
            player = Player()
            cars.clear()

        # Draw score
        font = pygame.font.SysFont("Arial", 30)
        score_text = font.render(f"Score: {score}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()