import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        self.cell_size = cell_size
        self.rows, self.cols = life.rows, life.cols
        self.width, self.height = self.cols * cell_size, self.rows * cell_size

        self.speed = speed
        self.screen = pygame.display.set_mode((self.width, self.height))

        super().__init__(life)

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for x in range(0, self.height, self.cell_size):
            for y in range(0, self.width, self.cell_size):
                cell_x = x // self.cell_size
                cell_y = y // self.cell_size
                pygame.draw.rect(
                    self.screen,
                    pygame.Color("green" if self.life.curr_generation[cell_x][cell_y] else "white"),
                    (y + 1, x + 1, self.cell_size - 1, self.cell_size - 1)
                )

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        self.draw_lines()

        running = True
        paused = False
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = not paused
                if paused and event.type == pygame.MOUSEBUTTONDOWN:
                    y, x = event.pos
                    if event.button == 1:
                        cell_x = x // self.cell_size
                        cell_y = y // self.cell_size
                        y = y // self.cell_size * self.cell_size
                        x = x // self.cell_size * self.cell_size
                        pygame.draw.rect(
                            self.screen,
                            pygame.Color("white" if self.life.curr_generation[cell_x][cell_y] else "green"),
                            (y + 1, x + 1, self.cell_size - 1, self.cell_size - 1)
                        )
                        # 0 xor 1 = 1
                        # 1 xor 1 = 0
                        self.life.curr_generation[cell_x][cell_y] ^= 1

                        pygame.display.flip()
                        clock.tick(60)


            if not paused:
                self.draw_grid()

                # Выполнение одного шага игры (обновление состояния ячеек)
                self.life.step()

                pygame.display.flip()
                clock.tick(self.speed)

        pygame.quit()
