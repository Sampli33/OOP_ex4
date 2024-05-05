class GeometricObject:

    def __init__(self, x=0, y=0, color='black', filled=False):
        if all(isinstance(value, (float, int)) for value in (x, y)):
            self.__x = x
            self.__y = y
        else:
            print('Координаты могут быть только числом')
        self.color = color
        self.filled = filled

    def __str__(self):
        output = f'{(float(self.__x), float(self.__y))}\n'
        output += f'color: {self.color}\n'
        output += f'filled: {self.filled}'
        return output

    def __repr__(self):
        output = f'{(self.__x, self.__y)} '
        output += f'{self.color} '
        if self.filled:
            output += 'filled'
        else:
            output += 'no filed'
        return output

    def set_coordinate(self, x: float, y: float):
        if all(isinstance(value, (float, int)) for value in (x, y)):
            self.__x = x
            self.__y = y
        else:
            print('Координаты могут быть только числом')

    def set_color(self, color: str):
        if isinstance(color, str):
            self.color = color
        else:
            print('Цвет может быть только строкой')

    def set_filled(self, value: bool):
        if isinstance(value, bool):
            self.filled = value
        else:
            print('Заливка может принимать значение только True или False')

    def get_x(self):
        return float(self.__x)

    def get_y(self):
        return float(self.__y)

    def get_color(self):
        return self.color

    def is_filled(self):
        return self.filled


class Circle(GeometricObject):
    all_circles = []
    pi = 3.1415

    def __init__(self, x=0, y=0, radius=0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        if radius >= 0 and isinstance(radius, (float, int)):
            self.__radius = radius
        else:
            self.__radius = 0.0
        Circle.all_circles.append(self)

    @property
    def radius(self):
        return float(self.__radius)

    @radius.setter
    def radius(self, radius):
        if radius >= 0 and isinstance(radius, (float, int)):
            self.__radius = radius
        else:
            self.__radius = 0.0

    def get_area(self):
        circle_area = Circle.pi * self.__radius ** 2
        return circle_area

    def get_perimetr(self):
        circle_perimetr = 2 * Circle.pi * self.__radius
        return circle_perimetr

    def get_diametr(self):
        return float(self.__radius * 2)

    @staticmethod
    def total_area():
        sum_areas = 0
        for circle in Circle.all_circles:
            sum_areas += circle.area()
        return sum_areas

    def __str__(self):
        output = f'radius: {self.radius}\n'
        output += super().__str__()
        return output

    def __repr__(self):
        output = f'radius: {int(self.radius)} '
        output += super().__repr__()
        return output


class Rectangle(GeometricObject):

    def __init__(self, x=0, y=0, width=0, height=0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        if isinstance(width, (int, float)) and width >= 0:
            self.width = width
        else:
            self.width = 0.0
        if isinstance(height, (int, float)) and height >= 0:
            self.height = height
        else:
            self.height = 0.0

    def set_width(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.width = value
        else:
            self.width = 0.0

    def set_height(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.height = value
        else:
            self.height = 0.0

    def get_width(self):
        return float(self.width)

    def get_height(self):
        return float(self.height)

    def get_area(self):
        return float(self.width * self.height)

    def get_perimetr(self):
        return float(self.width * 2 + self.height * 2)

    def __str__(self):
        output = f'width: {float(self.width)}\n'
        output += f'height: {float(self.height)}\n'
        output += super().__str__()
        return output

    def __repr__(self):
        output = f'width: {self.width} '
        output += f'height: {self.height} '
        output += super().__repr__()
        return output
