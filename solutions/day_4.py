import numpy as np
import itertools
from dataclasses import dataclass, astuple


from utils.AOC import GridAOC

@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

class Day4(GridAOC):
    DAY = 4
    
    def __init__(self):
        super().__init__()
        self.directions = [Point(*x) for x in itertools.product((-1, 0, 1), repeat=2) if x != (0, 0)]
    
    def part_1(self):
        xmax, ymax = self.input.shape
        
        count = 0
        for start_point in np.argwhere(self.input == "X"):
            for direction in self.directions:
                pos = Point(*start_point)
                for target in ("M", "A", "S"):
                    pos = pos + direction
                    if 0 <= pos.x < xmax and 0 <= pos.y < ymax:
                        if self.input[*astuple(pos)] == target:
                            continue
                        break
                    else:
                        break
                else:
                    count += 1
                    
        print(count)
            
        
    def part_2(self):
        ...
        
        
if __name__ == "__main__":
    day_4 = Day4()
    day_4.part_1()