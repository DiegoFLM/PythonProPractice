import time

def fiboGen(max):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == max:
            return (n1 + n2)
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            counter += 1
            n1, n2 = n2, n1 + n2
            yield n2


if __name__ == '__main__':
    fibonacci = fiboGen(13)
    for element in fibonacci:
        print(element)
        time.sleep(0.1)

