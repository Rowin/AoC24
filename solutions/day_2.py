from utils.AOC import NumberLineAOC

class Day2(NumberLineAOC):
    DAY = 2
    
    @staticmethod
    def is_valid(diff):
        _max = max(diff)
        _min = min(diff)
        return (_max <= 3 and _min >= 1) or (_max <= -1 and _min >= -3)
    
    def part_1(self):
        return sum([self.is_valid([b-a for a, b in zip(line, line[1:])]) for line in self.input])
    
    def part_2(self):
        counter = 0
        for line in self.input:
            diff = [b-a for a, b in zip(line, line[1:])]
            if self.is_valid(diff):
                counter += 1
            elif (self.is_valid(diff[1:]) or self.is_valid(diff[:-1])):
                counter += 1
            else:
                for i in range(len(diff)-1):
                    if self.is_valid(diff[:i] +[diff[i]+diff[i+1]] + diff[i+2:]):
                        counter += 1
                        break
    
        return counter
        
if __name__ == "__main__":
    day_2 = Day2()
    print(day_2.part_1())
    print(day_2.part_2())