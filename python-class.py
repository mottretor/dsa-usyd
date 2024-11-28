class A:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        x = 10

    def get_height(self):
        return self.height
    
    def set_height(self, height):
        self.height = height

x = A(12, 34)
x.set_height(100)
print(x.height)