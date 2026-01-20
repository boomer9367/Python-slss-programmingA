# Pygame Drawing
# Author: Justin L
# 5 January 2026
import heapq
import random

import pygame

# ---------------- CONSTANTS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

TILE_SIZE = 40
SPRITE_SIZE = 32


# ---------------- MAZE GENERATOR
def generate_maze(rows, cols):
    maze = [["1" for _ in range(cols)] for _ in range(rows)]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    dirs = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    def carve(r, c):
        maze[r][c] = "0"
        random.shuffle(dirs)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and maze[nr][nc] == "1":
                wall_r, wall_c = r + dr // 2, c + dc // 2
                maze[wall_r][wall_c] = "0"
                carve(nr, nc)

    start_r = random.randrange(1, rows, 2)
    start_c = random.randrange(1, cols, 2)
    carve(start_r, start_c)

    maze[1][0] = "0"  # Entrance
    maze[rows - 2][cols - 1] = "0"  # Exit

    return maze


# ---------------- CAMERA
class Camera:
    def __init__(self, world_width, world_height, screen_width, screen_height):
        self.camera = pygame.Rect(0, 0, world_width, world_height)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + self.screen_width // 2
        y = -target.rect.centery + self.screen_height // 2
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.camera.width - self.screen_width), x)
        y = max(-(self.camera.height - self.screen_height), y)
        self.camera.topleft = (x, y)


# ---------------- GRASS BACKGROUND
class Grass:
    def __init__(self):
        self.image = pygame.image.load("data/grass.png").convert()
        self.tile_w = self.image.get_width()
        self.tile_h = self.image.get_height()

    def draw(self, screen, camera):
        start_x = -camera.camera.x // self.tile_w * self.tile_w
        start_y = -camera.camera.y // self.tile_h * self.tile_h

        for x in range(
            start_x, start_x + camera.screen_width + self.tile_w, self.tile_w
        ):
            for y in range(
                start_y, start_y + camera.screen_height + self.tile_h, self.tile_h
            ):
                screen.blit(self.image, (x, y))


# ---------------- WALL
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREY)
        self.rect = self.image.get_rect(topleft=(x, y))


# ---------------- BLOCK (COIN)
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(x, y))
        self.point_value = 1


# ---------------- PLAYER
class Mario(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_right = pygame.image.load("data/mario-snes.png").convert_alpha()
        self.image_right = pygame.transform.smoothscale(
            self.image_right, (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.health = 100
        self.points = 0

    def update(self, walls):
        keys = pygame.key.get_pressed()
        speed = 4

        old_x = self.rect.x
        if keys[pygame.K_a]:
            self.rect.x -= speed
            self.image = self.image_left
        if keys[pygame.K_d]:
            self.rect.x += speed
            self.image = self.image_right
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x = old_x

        old_y = self.rect.y
        if keys[pygame.K_w]:
            self.rect.y -= speed
        if keys[pygame.K_s]:
            self.rect.y += speed
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.y = old_y

    def incr_score(self, amt):
        self.points += amt

    def calc_damage(self, amt):
        self.health -= amt


# ---------------- ASTAR PATHFINDING
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start, [start]))
    visited = set()
    while open_set:
        _, cost, current, path = heapq.heappop(open_set)
        if current == goal:
            return path[1:]
        if current in visited:
            continue
        visited.add(current)
        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                heapq.heappush(
                    open_set,
                    (
                        cost + 1 + heuristic((nr, nc), goal),
                        cost + 1,
                        (nr, nc),
                        path + [(nr, nc)],
                    ),
                )
    return []


# ---------------- ENEMY (PATHFINDING GOOMBA)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("data/goomba.png").convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image, (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.damage = 1
        self.path = []
        self.speed = 2

    def update(self, grid, player):
        start_tile = (self.rect.centery // TILE_SIZE, self.rect.centerx // TILE_SIZE)
        goal_tile = (player.rect.centery // TILE_SIZE, player.rect.centerx // TILE_SIZE)

        if not self.path or random.random() < 0.02:
            self.path = astar(grid, start_tile, goal_tile)

        if self.path:
            target_r, target_c = self.path[0]
            target_x = target_c * TILE_SIZE + TILE_SIZE // 2
            target_y = target_r * TILE_SIZE + TILE_SIZE // 2

            dx = target_x - self.rect.centerx
            dy = target_y - self.rect.centery
            dist = (dx**2 + dy**2) ** 0.5

            if dist < self.speed:
                self.rect.center = (target_x, target_y)
                self.path.pop(0)
            else:
                self.rect.x += self.speed * dx / dist
                self.rect.y += self.speed * dy / dist


# ---------------- HEALTH BAR
class HealthBar(pygame.Surface):
    def __init__(self, width, height):
        super().__init__((width, height))
        self.width = width
        self.height = height

    def update_info(self, percentage):
        self.fill(RED)
        pygame.draw.rect(self, GREEN, (0, 0, int(self.width * percentage), self.height))


# ---------------- GAME
def game():
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    ROWS = 21
    COLS = 31
    MAZE = generate_maze(ROWS, COLS)
    WORLD_WIDTH = COLS * TILE_SIZE
    WORLD_HEIGHT = ROWS * TILE_SIZE

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Maze Game")

    clock = pygame.time.Clock()
    done = False

    camera = Camera(WORLD_WIDTH, WORLD_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)
    grass = Grass()

    wall_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    # Build maze
    for row, line in enumerate(MAZE):
        for col, char in enumerate(line):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            if char == "1":
                wall_sprites.add(Wall(x, y))
            elif char == "0" and random.random() < 0.15:
                block_sprites.add(Block(x + TILE_SIZE // 2, y + TILE_SIZE // 2))

    # Pathfinding grid
    path_grid = [[1 if char == "1" else 0 for char in row] for row in MAZE]

    # Player spawn
    player = Mario(TILE_SIZE * 1 + TILE_SIZE // 2, TILE_SIZE * 1 + TILE_SIZE)
    # Enemy spawn
    enemy_sprites.add(
        Enemy(WORLD_WIDTH - TILE_SIZE * 1.5, WORLD_HEIGHT - TILE_SIZE * 1.5)
    )

    health_bar = HealthBar(200, 10)

    # ---------------- LOOP
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        player.update(wall_sprites)
        for enemy in enemy_sprites:
            enemy.update(path_grid, player)
        camera.update(player)

        # Player collects blocks
        for block in pygame.sprite.spritecollide(player, block_sprites, True):
            player.incr_score(block.point_value)

        # Enemy hits player
        for enemy in pygame.sprite.spritecollide(player, enemy_sprites, False):
            player.calc_damage(enemy.damage)

        if player.health <= 0:
            done = True

        health_bar.update_info(player.health / 100)

        # ---------------- DRAW
        grass.draw(screen, camera)
        for wall in wall_sprites:
            screen.blit(wall.image, camera.apply(wall))
        for block in block_sprites:
            screen.blit(block.image, camera.apply(block))
        for enemy in enemy_sprites:
            screen.blit(enemy.image, camera.apply(enemy))
        screen.blit(player.image, camera.apply(player))
        screen.blit(health_bar, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    print("Game Over")
    print("Score:", player.points)
    pygame.quit()


if __name__ == "__main__":
    game()
