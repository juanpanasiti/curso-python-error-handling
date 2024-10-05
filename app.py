def get_number() -> float:
    try:
        return float(input('Ingrese un número: '))
    except ValueError as error:
        print('Valor erroneo', error)
        return get_number()
    # finally:
    #     print('bloque finally')


def get_number_list() -> list[float]:
    number_list: list[float] = []
    while True:
        number = get_number()
        if number == 0:
            break
        number_list.append(number)
    return number_list


def calc_average(number_list: list[float]) -> float:
    try:
        return sum(number_list) / len(number_list)
    except ZeroDivisionError:
        print('No se puede calcular el promedio de una lista vacía')
        raise Exception('La lista está vacía')
