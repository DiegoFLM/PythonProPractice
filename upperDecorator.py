def upperDecorator(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper


def run():
    @upperDecorator
    def message(name):
        return f'{name}, you have a new message'

    print(message('Cesar'))

if __name__=='__main__':
    run()