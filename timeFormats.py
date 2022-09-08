from datetime import datetime


def run():
    my_datetime = datetime.now()
    print(my_datetime)

    my_str = my_datetime.strftime('%d/%m/%Y')
    print(f'LATAM format: \t{my_str}')

    my_str = my_datetime.strftime('%m/%d/%Y')
    print(f'USA format: \t{my_str}')

    my_str = my_datetime.strftime("Year of the penguin: %Y")
    print(f'Random format: \t{my_str}')

if __name__ == '__main__':
    run()