import math

def isPrime(num: int) -> bool:
    for i in range (2, 1 + math.floor(math.sqrt(num))):
        if(num % i == 0):
            return False
    return True


def run():
    print(isPrime(37))


if __name__ == '__main__':
    run()
