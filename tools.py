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
    """Рассчитывает СКО (среднеквадратичное отклонение) выборки 5* элементов
       *update 12.11: выборка из N элементов
    """
    from math import sqrt
    average = findingTheAverage(listOfSamples)
    N = len(listOfSamples)
    summ = 0 #сумма всех (xi-average)**2
    for i in range(N):
        summ += (listOfSamples[i]-average)**2
    standardDeviation = sqrt((summ)/(N*(N-1)))
    return standardDeviation


def randomError(listOfSamples: list[float], confidence_error = 0.95) -> float:
    """Находит случайную погрешность при N = 5, p = 95%
       
       update 12.11: выборка из N>2 элементов 
       при доверительной погрешности 'p'= 0.68,'p'= 0.95,'p'= 0.99"""
    
    
    t_distribution_value = {0.99: {1: 0, 2: 63.7, 3: 9.92, 4: 5.84, 5: 4.60, 6: 4.03, 7: 3.71, 8: 3.5, 9: 3.36, 10: 3.25},
                            0.95: {1: 0, 2: 12.7, 3: 4.30, 4: 3.18, 5: 2.77, 6: 2.57, 7: 2.45, 8: 2.36, 9: 2.31, 10: 2.26},
                            0.68: {1: 0, 2: 1.82, 3: 1.31, 4: 1.19, 5: 1.13, 6: 1.10, 7: 1.08, 8: 1.07, 9: 1.06, 10: 1.05}
                            }
    t_distribution_infinityN_value = {0.99: 2.58,
                                      0.95: 1.96,
                                      0.68: 0.99
                                      }
    
    N = len(listOfSamples)
    if N <= 10:
        const = t_distribution_value[confidence_error][N]
    else:
        const = t_distribution_infinityN_value[confidence_error]
    
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


"""
list_1 = [2.8, 3.40, 3.90, 4.90, 5.6] #средние для создания выборки 
list_2 = [2.73, 2.85, 2.90, 2.94, 2.98] #выборка 
teta = 0.01 #погрешность
"""

"""Пример нахождения выборки по средним значениям: 2.8, 3.40, 3.90, 4.90, 5.60"""
# print(findingTheSampleByTheMean(list_1))

"""Пример проверки выборки на промах"""
# print(checkingTheSamplesForErrors(list_2))
# print(checkingTheSamplesForErrors(list_2))

"""Пример нахождения среднего значения по выборке"""
# print(findingTheAverage(list_2))

"""Пример рассчета СКО"""
# print(findingStandardDeviation(list_2))

"""Пример нахождения случайной погрешности по выборке"""
# print(randomError(list_2, confidence_error)

"""Пример нахождения полной погрешности, в данном случае приборная погрешность = 0.01"""
# print(fullErrorOfTheResult(list_2, teta))

"""Пример вычисления относительной погрешности, ответ в процентах"""
# print(relativeError(list_2))

"""Пример записи в стандартной форме"""
# print(answerInStandardForm(list_2, teta))