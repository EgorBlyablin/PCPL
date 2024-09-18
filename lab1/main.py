import sys
import math


def get_coefficient(index: int, prompt: str) -> float:
    """Возвращает коэффициент биквадратного уравнения

    Если значение с указанным индексов существует в аргументах запуска и имеет корректный тип - возвращает его.
    В противном случае запрашивает значение у пользователя, пока не будет введено верное значение.

    Args:
        index (int): Индекс коэффициента в аргументах командной строки
        prompt (str): Подсказка пользователю о запрашиваемом коэффициенте

    Returns:
        float: Коэффициент
    """
    result = None

    try:  # пробуем извлечь коэффициент из аргументов запуска
        result = float(sys.argv[index + 1])
    except (ValueError, IndexError):
        # в случае отсутствия (IndexError) или некорректности (ValueError) - запрашиваем пользовательский ввод
        while result is None:  # пока результату не будет присвоено значение
            try:  # запрашиваем ввод
                result = float(input(prompt))
            except ValueError:  # в случае некорректного ввода сообщаем об ошибке
                print("Введено некорректное значение")

    return result  # возвращаем коэффициент


def get_coefficients() -> tuple[float, float, float]:
    """Возвращает три коэффициента биквадратного уравнения, получая их из аргументов запуска или от пользователя

    Returns:
        tuple[float, float, float]: Три коэффициента биквадратного уравнения
    """

    a = get_coefficient(0, "Введите коэффициент А: ")
    b = get_coefficient(1, "Введите коэффициент B: ")
    c = get_coefficient(2, "Введите коэффициент C: ")

    return a, b, c  # возвращаем коэффициенты


def main() -> None:
    a, b, c = get_coefficients()  # получаем коэффициент
    d = b**2 - 4 * a * c  # считаем дискриминант

    roots = set()  # объявляем множество корней

    if d >= 0:  # если дискриминант неотрицателен - ищем корни
        # считаем подкоренное выражение, добавляя дискриминант
        sub_sqrt_equation1 = (-b + math.sqrt(d)) / (2 * a)
        # считаем подкоренное выражение, вычитая дискриминант
        sub_sqrt_equation2 = (-b - math.sqrt(d)) / (2 * a)

        for sub_sqrt_equation in (sub_sqrt_equation1, sub_sqrt_equation2):
            if sub_sqrt_equation >= 0:
                # при положительности подкоренного выражения ищем корни
                roots.add(math.sqrt(sub_sqrt_equation))
                roots.add(-math.sqrt(sub_sqrt_equation))

    if roots:
        print(f"Корни: {', '.join(str(root) for root in roots)}")
    else:
        print("Корней нет")


if __name__ == "__main__":
    main()
