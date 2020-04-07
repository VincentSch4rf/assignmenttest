class TestSuite:
    
    def __init__(self, name=''):
        self.line = '='*50
        self.thin_line = '-'*50
        self.tests = []
        self.name = name
    
    def add_test(self, test):
        self.tests.append(test)
        
    def run(self):
        print(self.line)
        print('Test Suite {}'.format(self.name))
        print('Found {} test(s).'.format(len(self.tests)))
        print(self.thin_line)
        total = len(self.tests)
        passed = 0
        for test in self.tests:
            status, msg = test.test()
            print('{}\nStatus: {}'.format(
                test.name,
                'Passed' if status else 'Failed'
            ))
            if not status:
                print(msg)
            else:
                print()
                passed += 1
        print('Ran {} test(s). {} / {} passed.'.format(total, passed, total))
        print(self.line)
        return total == passed