from make_docx import inputs_makeDocument
from sample_input import inputSamples
from tools import (findingTheSampleByTheMean,
                   checkingTheSamplesForErrors, 
                   findingTheAverage, 
                   findingStandardDeviation, 
                   randomError, 
                   fullErrorOfTheResult, 
                   relativeError, 
                   answerInStandardForm)


def gen_answer(s, manual=True):
    print(checkingTheSamplesForErrors(s))
    print(findingTheAverage(s))
    print(findingStandardDeviation(s))
    print(randomError(s))
    print(fullErrorOfTheResult(s, 0.01))
    print(relativeError(s))
    print(answerInStandardForm(s, 0.01))
    if manual:
        inputs_makeDocument()


if __name__ == "__main__":
    gen_answer(inputSamples())