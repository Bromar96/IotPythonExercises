from SquareManager import *
from Point import *
if __name__=="__main__":
    print("SQUARE EXERCISE")
    sm=SquareManager(5)

    print('Area: ', sm.area())
    print('Perimeter: ', sm.perimeter())
    print('Diagonal: ', sm.diagonale())

    print('\nPOINT EXERCISE\n')
    a=Point(7,1)
    b=Point(1,1)
    print(f'distance from a to b is: {a.distance(b)}')
    
