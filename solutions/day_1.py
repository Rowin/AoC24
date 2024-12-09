from utils.AOC import NumberLineAOC

class Day1(NumberLineAOC):
    DAY = 1
    
    def parse_input(self):
        super().parse_input()
        
        self.left, self.right = zip(*self.input)
    
    
    def part_1(self):            
        return sum([abs(a - b) for a, b in zip(sorted(self.left), sorted(self.right))])
    
    def part_2(self):
        return sum([i*self.right.count(i) for i in self.left])
        
        
if __name__ == "__main__":
    day_1 = Day1()
    print(day_1.part_1())
    print(day_1.part_2())
    