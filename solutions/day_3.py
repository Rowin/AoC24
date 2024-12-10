import re
import math

from utils.AOC import LinearAOC


class Day3(LinearAOC):
    DAY = 3
    
    def part_1(self):
        acc = 0
        for line in self.input:
            acc += sum([math.prod(map(int, mul.groups())) for  mul in re.finditer(r"mul\((\d+),(\d+)\)", line)])
            
        return acc
    
    def part_2(self):
        acc = 0
        enabled_mul = True
        for line in self.input:
            for match in re.finditer(r"(?>mul\((\d+),(\d+)\)|do\(\)|don't\(\))", line):
                if match.group(0) == "do()":
                    enabled_mul = True
                elif match.group(0) == "don't()":
                    enabled_mul = False
                elif enabled_mul:
                    acc += math.prod(map(int, match.groups()))
                    
        return acc
        
if __name__ == '__main__':
    day_3 = Day3()
    print("Part 1:", day_3.part_1())
    print("Part 2:", day_3.part_2())