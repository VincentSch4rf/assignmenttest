import numpy.testing as test
from textwrap import dedent
from .test import Test

class TestSingleValue(Test):
    
    def __init__(self, value, expected, decimal=3):
        super(TestSingleValue, self).__init__('Single Value Test')
        self.value = value
        self.expected = expected
        self.decimal = decimal
        
    def error_msg(self):
        return dedent("""\
        Values are not equal rounded to {} decimals!
        Expected value is {}
        Actual value is   {}
        """).format(
            self.decimal,
            round(self.expected, self.decimal),
            round(self.value, self.decimal)
        )
        
    def test(self):
        try:
            assert round(self.expected, self.decimal) == round(self.value, self.decimal)
            return True, ''
        except AssertionError:
            return False, self.error_msg()


class TestNumericArrays(Test):
    
    def __init__(self, array, expected, decimal=3):
        super(TestNumericArrays, self).__init__('Numeric Array Test')
        self.array = array
        self.expected = expected
        self.decimal = decimal
        
    def error_msg(self):
        return dedent("""\
        Arrays are not equal rounded to {} decimals!
        Expected value is {}
        Actual value is   {}
        """).format(
            self.decimal,
            self.repr.repr(self.expected),
            self.repr.repr(self.array)
        )
    
    def test(self):
        try:
            test.assert_array_almost_equal(self.array, self.expected, decimal=self.decimal)
            return True, ''
        except AssertionError:
            return False, self.error_msg()


class TestString(Test):
    
    def __init__(self, value, expected, caseSensitive=True, strip=False):
        super(TestString, self).__init__('Single String Test')
        self.value = value
        self.expected = expected
        self.caseSensitive = caseSensitive
        self.strip = strip
        
    def error_msg(self):
        return dedent("""\
        Strings are not equal!
        Expected value is {}
        Actual value is   {}
        """).format(
            self.expected,
            self.array
        )
        
    def test(self):
        try:
            value = self.value
            expected = self.expected
            if not self.caseSensitive:
                value = value.lower()
                expected = expected.lower()
            if self.strip:
                value = value.strip()
                expected = expected.strip()
            assert value == expected
            return True, ''
        except:
            return False, self.error_msg()