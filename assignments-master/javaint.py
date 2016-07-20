#
#   @author: bill ebeling
#   @course: programming languages.  (375, or something like it)
#
#   @about:  Returns true if argument is a string of a valid java int literal 
#
#   @literals:
#
#   Decimal: Base 10, whose digits consists of the numbers 0 through 9; this is the number system you use every day
#   Hexadecimal: Base 16, whose digits consist of the numbers 0 through 9 and the letters A through F
#   Binary: Base 2, whose digits consists of the numbers 0 and 1 (you can create binary literals in Java SE 7 and later)
#   Octal: Base 8, 0 followed by the numbers 0 through 7
#   allow underscores inside 
#
#
#   Research Sources:
#   https://stuff.mit.edu/afs/sipb/user/marc/hotjava/doc/javaspec/javaspec_3.html#HEADING7
#   http://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html
#

def isJavaInt(txt):

    #   python has a really good type library, but this program requires I 
    #   not import anything, so here's a shameful hack to ensure we don't
    #   have a numeral
    try:
        txt[0] 
    except TypeError: # not a string
        return False
    except IndexError: # empty string
        return False

    # I don't *think* this is cheating, plus all upper is easier
    txt=txt.lstrip().rstrip().upper()

    # we have an empty string
    if len(txt) == 0: return False

    # we have a potential long, which is fine
    if txt[-1] == 'L': txt = txt[:-1]
    
    # most likely to get decimal chars, so test that first
    decimalChars = ['0','1','2','3','4','5','6','7','8','9']
    if not txt[0] == '0':
        for x in txt:
            if x not in decimalChars: # prob a word
                return False
    else: # txt[0] == '0'
        if txt[1] =='X':
            # test hex here
            hexChars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            for x in txt[2:]:
                if x not in hexChars:
                    return False
        elif txt[1] =='B':
            # test bin here 
            for x in txt[2:]:
                if x not in ['0','1']:
                    return False
        else:
            # test for oct
            octChars = ['0','1','2','3','4','5','6','7']
            for x in txt[1:]:
                if x not in octChars:
                    return False 
    

    return True


#########################
##  Just a way to test ##    
#########################
import unittest
class TestForJavaLiteralsUsingPython(unittest.TestCase):

    def test_vanilla_decimal_number(self):
        self.assertTrue(isJavaInt("10"))

    def test_weird_decimal_number(self):
        self.assertTrue(isJavaInt("  3456L"))

    def test_vanilla_binary(self):
        self.assertTrue(isJavaInt("0b1010101010101010"))

    def test_weird_binary_number(self):
        self.assertTrue(isJavaInt("  0b111 "))

    def test_vanilla_hex_number(self):
        self.assertTrue(isJavaInt("0xbeefcafe"))

    def test_weird_hex_number(self):
        self.assertTrue(isJavaInt("0xbee  "))

    def test_other_weird_hex_number(self):
        self.assertTrue(isJavaInt(' 0x123'))

    def test_vanilla_oct_number(self):
        self.assertTrue(isJavaInt('0234'))
    
    def test_weird_oct_number(self):
        self.assertTrue(isJavaInt("  0654234L  "))

    def test_long_dec(self):
        # that's a lower case 'L' on the end there
        self.assertTrue(isJavaInt('2347052304957234572390452093487520345l'))

    def test_dec_not_string(self):
        self.assertFalse(isJavaInt(208923))

    def test_bin_not_string(self):
        self.assertFalse(isJavaInt(0b0101))

    def test_hex_not_string(self):
        self.assertFalse(isJavaInt(0xbeefcafe))    

    def test_oct_not_string(self):
        self.assertFalse(isJavaInt(03456))

    def test_should_fail_dec_test(self):
        self.assertFalse(isJavaInt('ohaidere'))

    def test_just_an_l(self):
        self.assertFalse(isJavaInt('l'))

    def test_should_fail_oct_test(self):
        self.assertFalse(isJavaInt('0asdf'))

    def test_should_fail_hex_test(self):
        self.assertFalse(isJavaInt('0xakopsdf'))

    def test_should_fail_bin_test(self):
        self.assertFalse(isJavaInt('0b1234'))

    def test_almost_legal_decimal(self):
        self.assertFalse(isJavaInt('2354 324'))

    def test_bad_oct_good_dec(self):
        self.assertFalse(isJavaInt('089'))

    def test_a_negative_should_fail(self):
        self.assertFalse(isJavaInt('-3245'))

    def test_an_explicit_positive_should_fail(self):
        self.assertFalse(isJavaInt('+2345'))

    def test_empty_string(self):
        self.assertFalse(isJavaInt(""))

    def test_whitespace(self):
        self.assertFalse(isJavaInt("     "))



# if this file is run, run tests
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestForJavaLiteralsUsingPython)
    unittest.TextTestRunner(verbosity=2).run(suite)





