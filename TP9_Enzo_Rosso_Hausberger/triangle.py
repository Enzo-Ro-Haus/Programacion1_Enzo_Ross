class Triangle:
    
    def __init__(self, sideA, sideB, sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC
    
    def larger_side(self):
        return max(self.sideA, self.sideB, self.sideC)
    
    def triangle_type(self):
        if (self.sideA == self.sideB == self.sideC):
            return 'Triangle Equilateral'
        elif (self.sideA == self.sideB) or (self.sideA == self.sideC) or (self.sideB == self.sideC):
            return 'Triangle Isosceles'
        else:
            return 'Triangle Scalene'