#  [A,B,C,D]
# X[1,2,3,4]
# Y[2,3,1,6]
#  [R,R,B,B]

#Predict(3,3)--> ?

import numpy as np
import math 

def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y'])**2 )

    return Ans

def MarvellousKNeighbourclassifier():
    Border = "-" * 50
    data = [
                {'point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
                {'point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
                {'point' : 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
                {'point' : 'D', 'X' : 4, 'Y' : 6, 'label' : 'Blue'}
            
            ]
    print(Border)
    print("Marvellous UserDefined KNN")
    print(Border)

    print(Border)
    print("Training Data Set")
    print(Border)

    for i in data:
        print(i)

    print(Border)

    new_point = {'X' : 3, 'Y' : 3}          # for Testing

    # Calculate all Distances

    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(Border)
    print("Calculated Distances are: ")
    print(Border)

    for d in data:
        print(d)

    sorted_data = sorted(data, key=lambda item : item['distance'])

    print(Border)
    print("Sorted Data is : ")
    print(Border)

    for d in sorted_data:
        print(d)

def main():
    MarvellousKNeighbourclassifier()

if __name__ == "__main__":
    main()