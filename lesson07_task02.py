# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, attrs: int):
        self.value = attrs

    @abstractmethod
    def calc_fabric(self):
        print("Расчет расхода ткани")


class Coat(Clothes):
    @property
    def calc_fabric(self, ):
        return self.value / 6.5 + 0.5


class Costume(Clothes):
    @property
    def calc_fabric(self):
        return 2 * self.value + 0.3


class CalcTotal(Clothes):
    def __init__(self, attrs: int, attrs2: int):
        super().__init__(attrs)
        self.value = attrs
        self.value2 = attrs2

    @property
    def calc_fabric(self):
        return self.value / 6.5 + 0.5 + 2 * self.value2 + 0.3


size, height = 44, 3

obj_coat = Coat(size)
obj_costume = Costume(height)
obj_total = CalcTotal(size, height)

print(f"\n\x1b[34mРасход ткани для пальто  >>> \x1b[0m{obj_coat.calc_fabric:.2f}")
print(f"\x1b[34mРасход ткани для костюма >>> \x1b[0m{obj_costume.calc_fabric:.2f}")
print(f"\x1b[34mОбщий расход ткани  >>> \x1b[0m{obj_total.calc_fabric:.2f}")
