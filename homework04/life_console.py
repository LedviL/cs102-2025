import curses

from life import GameOfLife
from ui import UI

from time import sleep


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        rows = self.life.rows
        cols = self.life.cols

        for r in range(rows+1):
            y = r * 2
            for c in range(cols):
                x = c * 2
                screen.addstr(y, x, '+')
                screen.addstr(y, x+1, '-')
            screen.addstr(y, cols * 2, '+')

        for r in range(rows):
            y = 2 * r + 1
            for c in range(cols + 1):
                x = c * 2
                screen.addstr(y, x, "|")

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        grid = self.life.curr_generation
        rows = self.life.rows
        cols = self.life.cols

        for r in range(rows):
            y = r * 2 + 1
            for c in range(cols):
                x = c * 2 + 1
                alive = grid[r][c]
                screen.addstr(y, x, 'O' if alive else ' ')


    def run(self) -> None:
        screen = curses.initscr()

        curses.curs_set(0)
        screen.clear()

        self.draw_borders(screen)
        self.draw_grid(screen)
        screen.nodelay(True)

        while self.life.is_changing and self.life.is_max_generations_exceeded:
            key = screen.getch()
            if key == ord('q'):
                break

            self.draw_grid(screen)
            self.life.step()
            screen.refresh()

            sleep(1)

        curses.endwin()
