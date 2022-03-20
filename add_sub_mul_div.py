def add(col_a: list, col_b: list, copy: bool = True) -> list:

    return apply_operator(col_a=col_a, col_b=col_b, copy=copy, operator='+')


def sub(col_a: list, col_b: list, copy: bool = True) -> list:

    return apply_operator(col_a=col_a, col_b=col_b, copy=copy, operator='-')


def mul(col_a: list, col_b: list, copy: bool = True) -> list:

    return apply_operator(col_a=col_a, col_b=col_b, copy=copy, operator='*')


def div(col_a: list, col_b: list, copy: bool = True) -> list:

    return apply_operator(col_a=col_a, col_b=col_b, copy=copy, operator='/')
    

def apply_operator(col_a: list, col_b: list, copy: bool = True, operator: str = None) -> list:

    if type(col_a) != list or type(col_b) != list:
        raise TypeError("Столбцы должны быть переданы в виде списов")
  
    size_a = get_size(col_a)
    size_b = get_size(col_b)

    if size_a != size_b:
        raise ValueError("Столбцы имеют разные размерности, применить действие невозможно")

    if copy:
        col_a = col_a[:]

    for i in range(len(col_a)):
        try:
            if operator == '+':
                col_a[i] += col_b[i]
            elif operator == '-':
                col_a[i] -= col_b[i]
            elif operator == '*':
                col_a[i] *= col_b[i]
            elif operator == '/':
                col_a[i] /= col_b[i]
            else:
                raise ValueError('Неизвестный оператор, действие не определено')
        except TypeError:
            raise TypeError('Один из столбцов содержит нечисловой тип данных')
        except ZeroDivisionError:
            raise ZeroDivisionError('Второй столбец содержит нулевые значения, деление невозможно')
    
    return col_a


def get_size(table: list) -> int:
    nrows = len(table)
    if nrows == 0:
        raise ValueError("Пустой список")
    return nrows



if __name__ == '__main':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

    # print('a до', a)
    assert add(a, b, copy = True) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # print('a после', a)
    assert sub(a, b) == [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert mul(a, b) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert div(a, b) == [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    # print(add(5, [1, 2]))
    print('Все выполнилось успешно')

    # x = {'a': 1}
    # y = x.copy()
    # y['b'] = 2
    # print(x)

print('Из файла add_sub_mul_div.py переменная __name__ = ', __name__)