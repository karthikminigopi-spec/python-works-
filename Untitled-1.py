class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        area = self.length * self.breadth
        print("Area of rectangle:", area)

    def update_dimensions(self, new_length, new_breadth):
        if new_length > 0 and new_breadth > 0:
            self.length = new_length
            self.breadth = new_breadth
            print("Dimensions updated successfully")
        else:
            print("Length and breadth must be positive")


# Create object and test
rect = Rectangle(10, 5)
rect.calculate_area()
rect.update_dimensions(20, 8)
rect.calculate_area()