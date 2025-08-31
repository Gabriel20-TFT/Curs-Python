class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return 3.14159 * (self.__radius ** 2)

if __name__ == '__main__':
    # Using the property
    c = Circle(5)
    print(c.radius)
    print(c.area)
    c.radius = 10
    print(c.area)
