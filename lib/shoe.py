# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size  
        self.condition = "New"  

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value > 0:
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
