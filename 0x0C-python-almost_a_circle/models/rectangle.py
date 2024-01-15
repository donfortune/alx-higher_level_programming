from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

     @property
    def width(self):
        return self.width
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError(f'{value} must be an integer')
        if value <= 0:
            raise ValueError(f'{value} must be > 0')

        self.width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError(f'{value} must be an integer')
        if value <= 0:
            raise ValueError(f'{value} must be > 0')
        self.height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError(f'{value} must be an integer')
        if value <= 0:
            raise ValueError(f'{value} must be > 0')
        self.x = value

    @property
    def y(self, value):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError(f'{value} must be an integer')
        if value <= 0:
            raise ValueError(f'{value} must be > 0')
        self.__y = value
