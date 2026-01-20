class TestCase:
    def __init__(self,name) -> None:
        self.name = name
    def setUp(self):
        pass
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        


class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.wasRun = None
        TestCase.__init__(self, name)
    def testMethod(self):
        self.wasRun = True
    def setUp(self):
        self.wasRun = None
        self.wasSetup = 1

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testRunning(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasRun)
    def testSetup(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetup)

TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()

#test = WasRun("testMethod")
#print(test.wasRun)
#test.run()
#print(test.wasRun)
 
