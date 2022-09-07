def makeDivisionBy(divisor: int):
    def div(dividend):
        return dividend / divisor
    return div

def run():
    print( makeDivisionBy(3)(18) )
    print( makeDivisionBy(5)(100) )
    print( makeDivisionBy(18)(54) )

if __name__=='__main__':
    run()