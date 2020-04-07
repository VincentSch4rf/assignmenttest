import inspect

class FunctionTest:

    def __init__(self):
        pass

    def function_info(self, fun):
        """
        Extract information about a function

        Arguments:
            fun  -- Function
        Returns:
            info -- Dictionary containing:
                    name      -- The name of the function
                    argc      -- The number of arguments of the function
                    arg_names -- The ordered list of argument names
        """
        info = {
            'name': fun.__name__,
            'argc': fun.__code__.co_argcount,
            'arg_names': inspect.getfullargspec(fun).args
        }
        return info

    def test_signature(self, fun, fun_ref):
        """
        Test the signature of a function against 
        a reference function

        Arguments:
            fun_name -- The function to be tested
            fun_ref  -- The reference function to be tested against
        Returns:
            None
        """
        assert type(fun) == type(fun_ref), '{} is not a function.'.format(fun)
        info_ref = self.function_info(fun_ref)
        info = self.function_info(fun)
        assert info['argc'] == info_ref['argc'], 'Wrong number of arguments. Should be {}. Got {}.'.format(info_ref['argc'], info['argc'])
        assert info['arg_names'] == info_ref['arg_names'], 'Arguments are named wrongly. Should be {}. Got {}.'.format(info_ref['arg_names'], info['arg_names'])


    def test_input_output(self, fun, fun_ref, tests, verbose=True, compare_fun=None):
        """
        Test a function against a reference function using test inputs 

        Arguments:
            fun         -- The function to be tested
            fun_ref     -- The reference function to be tested against
            tests       -- List of inputs for the tests
            verbose     -- default is true
            compare_fun -- The function used to compare and test the outputs, default is assert equals
        Returns:
            None
        """
        for test in tests:
            is_iterable = False
            try:
                iter(test)
                is_iterable = True
            except TypeError as te:
                pass
            if is_iterable:
                expected = fun_ref(*test)
            else:
                expected = fun_ref(test)
            if verbose:
                print('f({}) --> {}'.format(test, expected))
                print('Test with inputs {}'.format(test))
                print('Expected output is {}'.format(expected))
            if is_iterable:
                actual = fun(*test)
            else:
                actual = fun(test)
            if verbose:
                print('Got output {}'.format(actual))
            if not compare_fun:
                assert expected == actual, 'Wrong output for test {}. Expected {}. Got {}.'.format(test, expected, actual)
            else:
                compare_fun(expected, actual)





