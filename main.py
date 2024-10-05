from app import get_number_list, calc_average

def run():
    number_list = get_number_list()
    try:
        average = calc_average(number_list)
        print(f'La lista de {len(number_list)} elementos tiene un promedio de {average}.')
    except Exception as error:
        print(error)


if __name__ == '__main__':
    run()
