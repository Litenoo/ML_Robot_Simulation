from PIL import Image
import logging as log

class World:
    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)

    def is_obstructed(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return True
        return self.grid[y][x] == 0


    @classmethod
    def load_png(cls, route):
        if not route:
            raise ValueError("No file_path specified")

        print(str(route))
        im = Image.open(str(route))

        pixels = im.load()
        w,h = im.size ## width, height

        grid =[[0 for _ in range(w)] for _ in range(h)]

        for i in range(h): ## y
            for j in range(w): ## x
                grid[i][j] = 1 if pixels[j, i][0] == 0 else 0

        return cls(grid)