# Removendo emojis e corrigindo a versão final com interface amigável, sem usar caracteres especiais

import pygame
import sys
import queue

# Settings
WIDTH, HEIGHT = 800, 850
ROWS, COLS = 20, 20
TILE_SIZE = WIDTH // COLS

# Softer pastel colors
WHITE = (245, 245, 245)
GREY = (220, 220, 220)
BLUE = (100, 149, 237)
GREEN = (144, 238, 144)
BLACK = (30, 30, 30)
EXPLORED_COLOR = (200, 230, 255)
INFO_BG = (240, 240, 255)
BUTTON_COLOR = (180, 180, 255)
BUTTON_HOVER = (160, 160, 240)
TEXT_COLOR = (40, 40, 60)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cleaning Robot Simulation")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

def init_simulation():
    return {
        "grid": [['empty' for _ in range(COLS)] for _ in range(ROWS)],
        "start_pos": (0, 0),
        "robot_pos": (0, 0),
        "cleaned": set(),
        "explored": set(),
        "robot_targets": [],
        "robot_path": [],
        "robot_mode": "explore",
        "known_map": set(),
        "current_target_index": 0,
        "drawing": True,
        "steps": 0
    }

sim = init_simulation()

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pos = (row, col)
            color = WHITE
            if sim["grid"][row][col] == 'wall':
                color = BLACK
            elif pos in sim["cleaned"]:
                color = GREEN
            elif pos in sim["explored"]:
                color = EXPLORED_COLOR
            pygame.draw.rect(screen, color, rect, border_radius=4)
            pygame.draw.rect(screen, GREY, rect, 1, border_radius=4)

def draw_robot(pos):
    x = pos[1] * TILE_SIZE + TILE_SIZE // 2
    y = pos[0] * TILE_SIZE + TILE_SIZE // 2
    pygame.draw.circle(screen, BLUE, (x, y), TILE_SIZE // 3)

def draw_info():
    info_rect = pygame.Rect(0, HEIGHT - 150, WIDTH, 150)
    pygame.draw.rect(screen, INFO_BG, info_rect)

    stats = [
        f"Modo: {'Exploração' if sim['robot_mode'] == 'explore' else 'Limpeza'}",
        f"Explorados: {len(sim['explored'])}",
        f"Limpos: {len(sim['cleaned'])}",
        f"Acessíveis: {len(sim['known_map']) if sim['known_map'] else 'Desconhecido'}",
        f"Passos dados: {sim['steps']}"
    ]

    for i, text in enumerate(stats):
        render = font.render(text, True, TEXT_COLOR)
        screen.blit(render, (10, HEIGHT - 140 + i * 25))

def draw_button(text, rect, mouse_pos):
    color = BUTTON_HOVER if rect.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(screen, color, rect, border_radius=6)
    pygame.draw.rect(screen, GREY, rect, 2, border_radius=6)
    label = font.render(text, True, TEXT_COLOR)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)

def bfs_clean_order(start):
    q = queue.Queue()
    q.put(start)
    visited = set()
    visited.add(start)
    order = []

    while not q.empty():
        current = q.get()
        order.append(current)
        for d in [(0,1), (1,0), (-1,0), (0,-1)]:
            nr, nc = current[0] + d[0], current[1] + d[1]
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if sim["grid"][nr][nc] != 'wall' and (nr, nc) not in visited:
                    q.put((nr, nc))
                    visited.add((nr, nc))
    return order

def find_path(start, goal):
    q = queue.Queue()
    q.put((start, [start]))
    visited = set()
    visited.add(start)

    while not q.empty():
        current, path = q.get()
        if current == goal:
            return path[1:]

        for d in [(0,1), (1,0), (-1,0), (0,-1)]:
            nr, nc = current[0] + d[0], current[1] + d[1]
            neighbor = (nr, nc)
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if sim["grid"][nr][nc] != 'wall' and neighbor not in visited:
                    q.put((neighbor, path + [neighbor]))
                    visited.add(neighbor)
    return []

def plan_efficient_path(start, targets):
    path = []
    visited = set()
    current = start
    to_visit = list(targets)

    while to_visit:
        to_visit.sort(key=lambda pos: abs(pos[0] - current[0]) + abs(pos[1] - current[1]))
        next_tile = to_visit.pop(0)
        if next_tile not in visited:
            path.append(next_tile)
            visited.add(next_tile)
            current = next_tile
    return path

def update_robot():
    if sim["robot_mode"] == "explore":
        if not sim["robot_path"]:
            if sim["current_target_index"] == 0:
                sim["robot_targets"] = bfs_clean_order(sim["start_pos"])
            sim["current_target_index"] += 1
            if sim["current_target_index"] < len(sim["robot_targets"]):
                sim["robot_path"] = find_path(sim["robot_pos"], sim["robot_targets"][sim["current_target_index"]])
            else:
                sim["robot_mode"] = "clean"
                sim["robot_targets"] = plan_efficient_path(sim["robot_pos"], sim["known_map"])
                sim["current_target_index"] = 0
                if sim["robot_targets"]:
                    sim["robot_path"] = find_path(sim["robot_pos"], sim["robot_targets"][sim["current_target_index"]])
        if sim["robot_path"]:
            next_step = sim["robot_path"].pop(0)
            sim["robot_pos"] = next_step
            sim["known_map"].add(sim["robot_pos"])
            sim["explored"].add(sim["robot_pos"])
            sim["steps"] += 1
    elif sim["robot_mode"] == "clean":
        if not sim["robot_path"]:
            sim["current_target_index"] += 1
            if sim["current_target_index"] < len(sim["robot_targets"]):
                sim["robot_path"] = find_path(sim["robot_pos"], sim["robot_targets"][sim["current_target_index"]])
            else:
                sim["robot_targets"] = []
        if sim["robot_path"]:
            next_step = sim["robot_path"].pop(0)
            sim["robot_pos"] = next_step
            sim["cleaned"].add(sim["robot_pos"])
            sim["steps"] += 1

def main():
    global sim
    running = True
    reset_button = pygame.Rect(WIDTH - 120, HEIGHT - 60, 100, 35)

    while running:
        screen.fill(WHITE)
        draw_grid()
        draw_robot(sim["robot_pos"])
        draw_info()
        draw_button("Resetar", reset_button, pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_button.collidepoint((mouse_x, mouse_y)):
                    sim = init_simulation()

            if sim["drawing"]:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // TILE_SIZE, x // TILE_SIZE
                    if row < ROWS and (row, col) != sim["start_pos"]:
                        sim["grid"][row][col] = 'wall'
                if pygame.mouse.get_pressed()[2]:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // TILE_SIZE, x // TILE_SIZE
                    if row < ROWS and sim["grid"][row][col] != 'wall':
                        sim["start_pos"] = (row, col)
                        sim["robot_pos"] = sim["start_pos"]
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        sim["drawing"] = False
                        sim["robot_targets"] = bfs_clean_order(sim["start_pos"])
                        sim["current_target_index"] = 0
                        if sim["robot_targets"]:
                            sim["robot_path"] = find_path(sim["robot_pos"], sim["robot_targets"][sim["current_target_index"]])
                    if event.key == pygame.K_r:
                        sim = init_simulation()

        if not sim["drawing"]:
            update_robot()

main()
