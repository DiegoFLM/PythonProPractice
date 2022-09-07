from datetime import datetime

def execTime(func):
    def wrapper(*args, **kwargs):
        initialTime = datetime.now()
        func(*args, **kwargs)
        finalTime = datetime.now()
        timeElapsed = finalTime - initialTime
        print('Elapsed time: ', timeElapsed.total_seconds(), 's')
    return wrapper

@execTime
def randomFunc():
    for _ in range (10000000):
        pass

@execTime
def sum(a: int, b: int) -> int:
    return (a + b)


randomFunc()
sum(2, 3)