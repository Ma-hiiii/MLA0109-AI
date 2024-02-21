class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.current_position = (0, 0)
        self.clean_count = 0

    def move(self, direction):
        x, y = self.current_position
        if direction == 'up' and x > 0:
            x -= 1
        elif direction == 'down' and x < self.rows - 1:
            x += 1
        elif direction == 'left' and y > 0:
            y -= 1
        elif direction == 'right' and y < self.cols - 1:
            y += 1
        self.current_position = (x, y)

    def clean(self):
        while self.clean_count < self.rows * self.cols:
            if self.grid[self.current_position[0]][self.current_position[1]] == 'dirty':
                self.grid[self.current_position[0]][self.current_position[1]] = 'clean'
                self.clean_count += 1
            if self.current_position[1] < self.cols - 1:
                self.move('right')
            elif self.current_position[0] < self.rows - 1:
                self.move('down')
            elif self.current_position[1] > 0:
                self.move('left')
            elif self.current_position[0] > 0:
                self.move('up')

grid = [
    ['clean', 'clean', 'dirty', 'clean'],
    ['dirty', 'clean', 'clean', 'dirty'],
    ['clean', 'dirty', 'clean', 'clean'],
    ['dirty', 'clean', 'clean', 'clean']
]

vacuum = VacuumCleaner(grid)
vacuum.clean()
print(vacuum.grid)
