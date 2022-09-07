import math

def setList(lst):
    def mapDeco(func):
        def wrapper(*args, **kwargs):
            results = list( map(func, lst) )
            print(results)
            with open('./results.txt', 'a') as f:
                f.write(str(results[0]))
                for r in results:
                    f.write(',')
                    f.write(str(r)) 
                f.write('\n')
        return wrapper
    return mapDeco


lst = [i for i in range (2, 15)]

@setList(lst)
def isPrime(num):
    for i in range (2, 1 + math.floor(math.sqrt(num))):
        print(i)
        if ( num % i == 0 ):
            return False
    return True


def run():
    isPrime(25)


if __name__ == '__main__':
    run()