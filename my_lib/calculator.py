class Calculator:
    x = 0
    y = 0
    z = 0
    
    a = 0
    b = 0
    c = 0
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        return
    
    def multiply(self):
        self.z = self.x * self.y
        
    def add(self):
        self.c = self.a + self.b