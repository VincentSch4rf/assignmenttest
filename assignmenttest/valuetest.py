import numpy.testing as test
import reprlib

class ValueTest:

    def __init__(self):
        self.line = '='*50
        self.repr = reprlib.Repr()
        self.repr.maxlist = 10
        self.repr.maxstring = 20

    def compare_single_value(self, value, expected, decimal=3, raise_exception=True):
        print(self.line)
        print('Single Value Test')
        print('Expected value is {:.{}f}'.format(expected, decimal))
        print('Actual value is   {:.{}f}'.format(value, decimal))
        passed = False
        try:
            assert round(expected, decimal) == round(value, decimal)
            passed = True
        except AssertionError:
            passed = False

        if passed:
            print('Result: Passed')
        else:
            print('Result: Failed!')
        print(self.line)
        if raise_exception and not passed:
            raise AssertionError('Values are not equal rounded to {} decimals!'.format(decimal))
        return passed

    def compare_numeric_arrays(self, array, expected, decimal=3, raise_exception=True):
        print(self.line)
        print('Numeric Array Test')
        print('Expected value is {}'.format(self.repr.repr(expected)))
        print('Actual value is   {}'.format(self.repr.repr(array)))
        passed = False
        try:
            test.assert_array_almost_equal(array, expected, decimal=decimal)
            passed = True
        except AssertionError:
            passed = False

        if passed:
            print('Result: Passed')
        else:
            print('Result: Failed!')
        print(self.line)
        if raise_exception and not passed:
            raise AssertionError('Arrays are not equal rounded to {} decimals!'.format(decimal))
        return passed


