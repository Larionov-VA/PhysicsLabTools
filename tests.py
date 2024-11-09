import unittest
from tools import (
    findingTheSampleByTheMean,
    checkingTheSamplesForErrors,
    findingTheAverage,
    findingStandardDeviation,
    randomError,
    fullErrorOfTheResult,
    relativeError,
    answerInStandardForm
)

class TestTools(unittest.TestCase):

    def test_findingTheSampleByTheMean(self):
        result = findingTheSampleByTheMean([2.8, 3.40, 3.90, 4.90, 5.60])
        self.assertEqual(len(result), 5)  # Проверяем, что возвращается 5 выборок

    def test_checkingTheSamplesForErrors(self):
        self.assertTrue(checkingTheSamplesForErrors([2.73, 2.85, 2.90, 2.94, 2.98]))
        self.assertFalse(checkingTheSamplesForErrors([3.33, 2.85, 2.90, 2.94, 2.98]))

    def test_findingTheAverage(self):
        result = findingTheAverage([2.73, 2.85, 2.90, 2.94, 2.98])
        self.assertAlmostEqual(result, 2.88, places=2)

    def test_findingStandardDeviation(self):
        result = findingStandardDeviation([2.73, 2.85, 2.90, 2.94, 2.98])
        self.assertAlmostEqual(result, 0.04324, places=2)

    def test_randomError(self):
        result = randomError([2.73, 2.85, 2.90, 2.94, 2.98])
        self.assertGreater(result, 0)

    def test_fullErrorOfTheResult(self):
        result = fullErrorOfTheResult([2.73, 2.85, 2.90, 2.94, 2.98], 0.01)
        self.assertGreater(result, 0)

    def test_relativeError(self):
        result = relativeError([2.73, 2.85, 2.90, 2.94, 2.98])
        self.assertGreaterEqual(result, 0)

    def test_answerInStandardForm(self):
        average, full_error = answerInStandardForm([2.73, 2.85, 2.90, 2.94, 2.98], 0.01)
        self.assertIsInstance(average, float)
        self.assertIsInstance(full_error, float)

if __name__ == '__main__':
    unittest.main() 