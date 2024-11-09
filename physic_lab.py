



def findingTheSampleByTheMean(listOfAverages: list[float]) -> dict:
    """Находит значения выборки при известном среднем"""
    from random import random
    dictOfSamples = {}
    for x in listOfAverages:
        i = 0
        while x != i:
            x11 = round(x+random()*0.1-random()*0.1,2)
            x12 = round(x+random()*0.1-random()*0.1,2)
            x13 = round(x-random()*0.1+random()*0.1,2)
            x14 = round(x+random()*0.1-random()*0.1,2)
            x15 = round(x-random()*0.1+random()*0.1,2)
            i = (x11 + x12 + x13 + x14 + x15)/5
            
            if x == i:
                dictOfSamples[x] = x11, x12, x13, x14, x15
    return dictOfSamples


def checkingTheSamplesForErrors(listOfSamples: list[float]) -> bool:
    """Проверяет выборку на промахи при N = 5, p = 95%"""
    listOfSamples = sorted(listOfSamples)
    U = 0.64
    R = listOfSamples[-1]-listOfSamples[0]
    U1 = abs(listOfSamples[1]-listOfSamples[0])/R
    U2 = abs(listOfSamples[-1]-listOfSamples[-2])/R
    
    if U1 < U and U2 < U:
        return True
    else:
        return False
 



"""Пример нахождения выборки по средним значениям: 2.8, 3.40, 3.90, 4.90, 5.60"""
# print(findingTheSampleByTheMean([2.8,3.40,3.90,4.90,5.6]))

"""Пример проверки выборки на промах"""
# print(checkingTheSamplesForErrors([2.73,2.85,2.90,2.94,2.98]))
print(checkingTheSamplesForErrors([3.33,2.85,2.90,2.94,2.98]))