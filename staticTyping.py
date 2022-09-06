def run():
    print('Hello world')
    #a = 1
    a: int = 1
    print(type(a))
    a = 'bear'
    print(type(a))


    def sum(a: int,  b: int) -> int:
        return (a + b)

    print(sum('1', '2'))


if __name__ == '__main__':
    run()
