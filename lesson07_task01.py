# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса метод init(),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц)
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix: list):
        self.attr_matrix = matrix

    def __getitem__(self, item):
        return self.attr_matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.attr_matrix])

    def __add__(self, add_matrix):
        for i in range(len(self.attr_matrix)):
            for x in range(len(add_matrix.attr_matrix[i])):
                self.attr_matrix[i][x] = self.attr_matrix[i][x] + add_matrix.attr_matrix[i][x]
        return Matrix.__str__(self)


obj_matrix_1 = Matrix([[31, 37, 51],
                       [3, 5, 32],
                       [-1, 64, -8]])
obj_matrix_2 = Matrix([[22, 43, 86],
                       [2, -15, 6],
                       [24, 8, 44]])

print(f"\n\x1b[34mМатрица 1 >>>\n\x1b[0m{obj_matrix_1['attr_matrix']}")
print(f"\x1b[34mи перегрузка метода str() для вывода Матрицы 1 в привычном виде >>>\x1b[0m")
print(f"{obj_matrix_1.__str__()}")

print(f"\n\x1b[34mМатрица 1 >>>\n\x1b[0m{obj_matrix_2['attr_matrix']}")
print(f"\x1b[34mи перегрузка метода str() для вывода Матрицы 2 в привычном виде >>>\x1b[0m")
print(f"{obj_matrix_2.__str__()}")

print(f"\n\x1b[34mПерегрузка метода add() для реализации операции сложения двух объектов(матриц) "
      f"класса Matrix - новая матрица>>>\x1b[0m")
print(obj_matrix_1.__add__(obj_matrix_2))
