from utils.AOC import LinearAOC

class Day1(LinearAOC):
    DAY = 1
    
    def parse_input(self):
        super().parse_input()
        
        left, right = [], []
        
        line: str
        for line in self.input:
            a, b = [int(i) for i in line.split()]
            left.append(a)
            right.append(b)
            
        self.left = left
        self.right = right
    
    def part_1(self):            
        return sum([abs(a - b) for a, b in zip(sorted(self.left), sorted(self.right))])
    
    def part_2(self):
        return sum([i*self.right.count(i) for i in self.left])
        
        
if __name__ == "__main__":
    day_1 = Day1()
    print(day_1.part_1())
    print(day_1.part_2())
    