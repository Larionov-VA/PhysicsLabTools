from tools import (findingTheSampleByTheMean, 
                   checkingTheSamplesForErrors, 
                   findingTheAverage, 
                   findingStandardDeviation, 
                   randomError, 
                   fullErrorOfTheResult, 
                   relativeError, 
                   answerInStandardForm)


def inputSamples():
    samples = []
    i = 1
    print("Значения выборки печатайте поочередно в формате float, после каждого значения нажимайте Enter")
    while True:
        sample = input(f"Введите {i} значение: \n")
        if sample == "" or sample == "\t" or sample == "\n":
            print(f"Вы записали значения {samples}, прервать запись?")
            n = input("Y/N\n")
            if n == "Y":
                break
            else:
                continue
        sample = sample.replace(",",".")
        samples.append(float(sample))
        i += 1
    return samples


if __name__ == "__main__":
    s = inputSamples()
    print(checkingTheSamplesForErrors(s))
    print(findingTheAverage(s))
    print(findingStandardDeviation(s))
    print(randomError(s))
    print(fullErrorOfTheResult(s, 0.01))
    print(relativeError(s))
    print(answerInStandardForm(s, 0.01))
    # makeDocument(t="v", average=findingTheAverage(inputSamples()))

