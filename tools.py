def findingTheSampleByTheMean(listOfAverages: list[float]) -> dict:
    """Находит значения выборки при известном среднем"""
    from random import random
    dictOfSamples = {}
    for x in listOfAverages:
        i = 0
        while x != i:
            x11 = round(x+random()*0.1-random()*0.1,2)
            x12 = round(x+random()*0.1-random()*0.1,2)
            x13 = round(x+random()*0.1-random()*0.1,2)
            x14 = round(x+random()*0.1-random()*0.1,2)
            x15 = round(x+random()*0.1-random()*0.1,2)
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
 

def findingTheAverage(listOfSamples: list[float]) -> float:
    """Возвращает среднее значение выборки"""
    average = sum(listOfSamples)/len(listOfSamples)
    return average


def findingStandardDeviation(listOfSamples: list[float]) -> float:
    """Рассчитывает СКО (среднеквадратичное отклонение) выборки 5 элементов"""
    from math import sqrt
    average = findingTheAverage(listOfSamples)
    x1, x2, x3, x4, x5 = listOfSamples
    standardDeviation = sqrt(((x1-average)**2+(x2-average)**2+(x3-average)**2+(x4-average)**2+(x5-average)**2)/20)
    return standardDeviation


def randomError(listOfSamples: list[float]) -> float:
    """Находит случайную погрешность при N = 5, p = 95%"""
    const = 2.78
    error = const*findingStandardDeviation(listOfSamples)
    return error


def fullErrorOfTheResult(listOfSamples: list[float], instrumentError: float) -> float:
    """Находит полную погрешность результата измерений"""
    from math import sqrt
    randomErr = randomError(listOfSamples)
    teta = instrumentError
    fullError = sqrt(randomErr**2+teta**2)
    return fullError
    

def relativeError(listOfSamples: list[float]) -> float:
    """Возвращает относительную погрешность в процентах"""
    relativeErr = (randomError(listOfSamples)/findingTheAverage(listOfSamples))*100
    return relativeErr


def answerInStandardForm(listOfSamples: list[float], instrumentError: float) -> tuple:
    """ У КАЖДОГО ПРЕПОДАВАТЕЛЯ СВОИ ПРАВИЛА, БУДЬТЕ ОСТОРОЖНЫ
    Возвращает ответ в стандартной форме, первое значение - среднее выборки, второй - полная погрешность, округление происходит по правилу:
        1. Если полная погрешность результата меньше 1, то ищет в числе первую значущую цифру (не ноль):
            a. Если это 1, то записывает ее и следующую за ней значащую цифру (если такая существует).
            б. Если это число больше 1, то записывает число до него включительно.
        2. Если полная погрешность результата больше или ровна 1, то округляет до десятых.
        3. Округляет среднее выборки до того же порядка, что была округлена полная погрешность, если порядок погрешности больше, заполняет порядки нулями
    """
    theAverage = findingTheAverage(listOfSamples)
    fullError = fullErrorOfTheResult(listOfSamples, instrumentError)
    if fullError < 1:
        for i in range(len(str(fullError)[2:])):
            if str(fullError)[2:][i] != 1:
                fullError = float(str(fullError)[:i+4])
                theAverage = float(str(theAverage)[:i+4])
                break;
    else:
        fullError = round(fullError,1)
        theAverage = round(theAverage,1)
    return theAverage, fullError



"""Пример нахождения выборки по средним значениям: 2.8, 3.40, 3.90, 4.90, 5.60"""
# print(findingTheSampleByTheMean([2.8,3.40,3.90,4.90,5.6]))

"""Пример проверки выборки на промах"""
# print(checkingTheSamplesForErrors([2.73,2.85,2.90,2.94,2.98]))
# print(checkingTheSamplesForErrors([3.33,2.85,2.90,2.94,2.98]))

"""Пример нахождения среднего значения по выборке"""
# print(findingTheAverage([2.73,2.85,2.90,2.94,2.98]))

"""Пример рассчета СКО"""
# print(findingStandardDeviation([2.73,2.85,2.90,2.94,2.98]))

"""Пример нахождения случайной погрешности по выборке"""
# print(randomError([2.73,2.85,2.90,2.94,2.98]))

"""Пример нахождения полной погрешности, в данном случае приборная погрешность = 0.01"""
# print(fullErrorOfTheResult([2.73,2.85,2.90,2.94,2.98], 0.01))

"""Пример вычисления относительной погрешности, ответ в процентах"""
# print(relativeError([2.73,2.85,2.90,2.94,2.98]))

"""Пример записи в стандартной форме"""
# print(answerInStandardForm([2.73,2.85,2.90,2.94,2.98], 0.01))