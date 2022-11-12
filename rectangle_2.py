from rectangle import Rectangle, Square, Circle

# создаем два прямоугольника
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# вывод площади наших двух прямоугольников
print(rect_1. get_area())
print(rect_2. get_area())

# создаем два квадрата
square_1 = Square(5)
square_2 = Square(10)

# вывод площади наших двух квадратов
print(square_1.get_area_square(),
      square_2.get_area_square())

# создаем коллекцию фигуры
figures = [rect_1, rect_2, square_1, square_2]

# далее пройдемся по циклу For
for figure in figures:
      if isinstance(figure, Square):
            print(figure.get_area_square())
      else:
            print(figure.get_area())

# создаем два круга
circle_1 = Circle(7)
circle_2 = Circle(9)

# вывод площади наших двух кругов
print(circle_1. get_area_circle())
print(circle_2. get_area_circle())




