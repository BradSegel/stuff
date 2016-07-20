import re, unittest

def regex_java_int(candidate):
    candidate = candidate.strip()

    binReg = r'0[bB]([01]+[_]*[01]+)*[lL]?'
    octReg = r'0[0-7]([_]*[0-7]+)*[lL]{0,1}|0[lL]?'
    decReg = r'[1-9]([_]*[0-9]+)*[lL]?'
    hexReg = r'0[xX][0-9a-fA-F]+([_]*[0-9a-fA-F]+)*[lL]?'
    allReg = [binReg,octReg,decReg,hexReg,]

    isInt = False
    for reg in allReg:
        rst = re.match(reg, candidate)
        if rst and rst.group() == candidate: isInt = True

    return isInt



# if this file is run, run tests
class TestforJavaLiterals(unittest.TestCase):

    def test_is_bin_true(self):
        self.assertTrue(regex_java_int('0b1010101'))


    def test_is_dec_true(self):
        self.assertTrue(regex_java_int('5463456'))

    def test_is_dec_w_underscore(self):
        self.assertTrue(regex_java_int('35_326_234'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestforJavaLiterals)
    unittest.TextTestRunner(verbosity=2).run(suite)
 
