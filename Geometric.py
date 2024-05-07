class GeometricObject:
    """
    This class represents a generic geometric object.

    Attributes:
    __x (float): The x-coordinate of the object.
    __y (float): The y-coordinate of the object.
    color (str): The color of the object.
    filled (bool): Whether the object is filled or not.
    """

    def __init__(self, x=0, y=0, color='black', filled=False):
        """
        Initializes a GeometricObject with the given coordinates, color, and fill status.

        Args:
        x (float, int): The x-coordinate of the object.
        y (float, int): The y-coordinate of the object.
        color (str): The color of the object.
        filled (bool): Whether the object is filled or not.
        """

        if all(isinstance(value, (float, int)) for value in (x, y)):
            self.__x = x
            self.__y = y
        else:
            print('Координаты могут быть только числом')
        self.color = color
        self.filled = filled

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
        str: A string containing the object's coordinates, color, and fill status.
        """

        output = f'{(float(self.__x), float(self.__y))}\n'
        output += f'color: {self.color}\n'
        output += f'filled: {self.filled}'
        return output

    def __repr__(self):
        """
        Returns a more concise string representation of the object.

        Returns:
        str: A string containing the object's coordinates, color, and fill status in a compact format.
        """

        output = f'{(self.__x, self.__y)} '
        output += f'{self.color} '
        if self.filled:
            output += 'filled'
        else:
            output += 'no filed'
        return output

    def set_coordinate(self, x: float, y: float):
        """
        Sets the coordinates of the object.

        Args:
        x (float): The new x-coordinate.
        y (float): The new y-coordinate.
        """

        if all(isinstance(value, (float, int)) for value in (x, y)):
            self.__x = x
            self.__y = y
        else:
            print('Координаты могут быть только числом')

    def set_color(self, color: str):
        """
        Sets the color of the object.

        Args:
        color (str): The new color.
        """

        if isinstance(color, str):
            self.color = color
        else:
            print('Цвет может быть только строкой')

    def set_filled(self, value: bool):
        """
        Sets the fill status of the object.

        Args:
        value (bool): The new fill status.
        """

        if isinstance(value, bool):
            self.filled = value
        else:
            print('Заливка может принимать значение только True или False')

    def get_x(self):
        """
        Returns the x-coordinate of the object.

        Returns:
        float: The x-coordinate.
        """

        return float(self.__x)

    def get_y(self):
        """
        Returns the y-coordinate of the object.

        Returns:
        float: The y-coordinate.
        """

        return float(self.__y)

    def get_color(self):
        """
        Returns the color of the object.

        Returns:
        str: The color.
        """

        return self.color

    def is_filled(self):
        """
        Returns whether the object is filled or not.

        Returns:
        bool: True if the object is filled, False otherwise.
        """

        return self.filled


class Circle(GeometricObject):
    """
    This class represents a circle.

    Attributes:
    all_circles (list): A list of all Circle objects created.
    pi (float): The value of pi.
    __radius (float): The radius of the circle.
    """

    all_circles = []
    pi = 3.1415

    def __init__(self, x=0, y=0, radius=0, color='black', filled=False):
        """
        Initializes a Circle with the given coordinates, radius, color, and fill status.

        Args:
        x (float, int): The x-coordinate of the center of the circle.
        y (float, int): The y-coordinate of the center of the circle.
        radius (float, int): The radius of the circle.
        color (str): The color of the circle.
        filled (bool): Whether the circle is filled or not.
        """

        super().__init__(x, y, color, filled)
        if radius >= 0 and isinstance(radius, (float, int)):
            self.__radius = radius
        else:
            self.__radius = 0.0
        Circle.all_circles.append(self)

    @property
    def radius(self):
        """
        Gets the radius of the circle.

        Returns:
        float: The radius.
        """

        return float(self.__radius)

    @radius.setter
    def radius(self, radius):
        """
        Sets the radius of the circle.

        Args:
        radius (float, int): The new radius.
        """

        if radius >= 0 and isinstance(radius, (float, int)):
            self.__radius = radius
        else:
            self.__radius = 0.0

    def get_area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
        float: The area.
        """

        circle_area = Circle.pi * self.__radius ** 2
        return circle_area

    def get_perimetr(self):
        """
        Calculates and returns the perimeter (circumference) of the circle.

        Returns:
        float: The perimeter.
        """

        circle_perimetr = 2 * Circle.pi * self.__radius
        return circle_perimetr

    def get_diametr(self):
        """
        Calculates and returns the diameter of the circle.

        Returns:
        float: The diameter.
        """

        return float(self.__radius * 2)

    @staticmethod
    def total_area():
        """
        Calculates the sum of the areas of all Circle objects created.

        Returns:
        float: The total area.
        """

        sum_areas = 0
        for circle in Circle.all_circles:
            sum_areas += circle.area()
        return sum_areas

    def __str__(self):
        """
        Returns a string representation of the circle.

        Returns:
        str: A string containing the circle's radius and the properties inherited from GeometricObject.
        """

        output = f'radius: {self.radius}\n'
        output += super().__str__()
        return output

    def __repr__(self):
        """
        Returns a more concise string representation of the circle.

        Returns:
        str: A string containing the circle's radius and the properties inherited from GeometricObject in a compact format.
        """

        output = f'radius: {int(self.radius)} '
        output += super().__repr__()
        return output


class Rectangle(GeometricObject):
    """
    This class represents a rectangle.

    Attributes:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.
    """

    def __init__(self, x=0, y=0, width=0, height=0, color='black', filled=False):
        """
        Initializes a Rectangle with the given coordinates, width, height, color, and fill status.

        Args:
        x (float, int): The x-coordinate of the bottom-left corner of the rectangle.
        y (float, int): The y-coordinate of the bottom-left corner of the rectangle.
        width (float, int): The width of the rectangle.
        height (float, int): The height of the rectangle.
        color (str): The color of the rectangle.
        filled (bool): Whether the rectangle is filled or not.
        """

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
        """
        Sets the width of the rectangle.

        Args:
        value (float, int): The new width.
        """

        if isinstance(value, (int, float)) and value >= 0:
            self.width = value
        else:
            self.width = 0.0

    def set_height(self, value):
        """
        Sets the height of the rectangle.

        Args:
        value (float, int): The new height.
        """

        if isinstance(value, (int, float)) and value >= 0:
            self.height = value
        else:
            self.height = 0.0

    def get_width(self):
        """
        Returns the width of the rectangle.

        Returns:
        float: The width.
        """

        return float(self.width)

    def get_height(self):
        """
        Returns the height of the rectangle.

        Returns:
        float: The height.
        """

        return float(self.height)

    def get_area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        float: The area.
        """

        return float(self.width * self.height)

    def get_perimetr(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
        float: The perimeter.
        """

        return float(self.width * 2 + self.height * 2)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        str: A string containing the rectangle's width, height, and the properties inherited from GeometricObject.
        """

        output = f'width: {float(self.width)}\n'
        output += f'height: {float(self.height)}\n'
        output += super().__str__()
        return output

    def __repr__(self):
        """
        Returns a more concise string representation of the rectangle.

        Returns:
        str: A string containing the rectangle's width, height, and the properties inherited from GeometricObject in a compact format.
        """

        output = f'width: {self.width} '
        output += f'height: {self.height} '
        output += super().__repr__()
        return output