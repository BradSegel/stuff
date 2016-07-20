import re, unittest

def regex_java_flt(candidate):
    try:
        candidate = candidate.strip()
    except:
        # we get here by not getting a string as arg
        return False


    rgx = re.compile(r'[0-9][0-9_]*\.[0-9_]+([eE][\+\-]{0,1}[0-9]+){0,1}[dDfF]?')

    isFlt = False
    rst = re.match(rgx, candidate)
    if rst and rst.group() == candidate: isFlt = True

    return isFlt

# if this file is run, run tests
class TestforJavaLiterals(unittest.TestCase):

    def test_is_float(self):
        self.assertTrue(regex_java_flt('       35_326_234.54'))

    def test_is_sci_note(self):
        self.assertTrue(regex_java_flt('35_326_234.54e+345'))


    def test_is_float_sm_sci_note(self):
        self.assertTrue(regex_java_flt('35_326_234.54E-246'))


    def test_is_float_f(self):
        self.assertTrue(regex_java_flt('35_326_234.54325f         '))


    def test_is_float_sci_note_f(self):
        self.assertTrue(regex_java_flt('  35_326_234.54E32633F     '))

    def test_for_zero(self):
        self.assertTrue(regex_java_flt('0.0'))

    def test_for_bad_zero(self):
        self.assertFalse(regex_java_flt('0'))


    def test_is_not_int(self):
        self.assertFalse(regex_java_flt('23634'))

    def test_is_not_str(self):
        self.assertFalse(regex_java_flt('ohaidere'))


    def test_is_silly_hex_a_flt(self):
        self.assertFalse(regex_java_flt('babeface'))

    def test_for_start_underscore(self):
        self.assertFalse(regex_java_flt('_4563e345f'))

    def test_for_end_underscore(self):
        self.assertFalse(regex_java_flt('236e265_'))

    def test_for_just_f(self):
        self.assertFalse(regex_java_flt('f'))

    def test_for_so_many_fs(self):
        self.assertFalse(regex_java_flt('546.435ffFF'))

    def test_for_empty_string(self):
        self.assertFalse(regex_java_flt(''))

    def test_for_dumb_sci_note(self):
        self.assertFalse(regex_java_flt('1e0'))


    def test_for_sans_point(self):
        self.assertTrue(regex_java_flt('1F'))

    def test_for_point_stuff(self):
        self.assertTrue(regex_java_flt('.1f'))
    
    def test_for_sci_note_sans_point(self):
        self.assertTrue(regex_java_flt('1e4'))



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestforJavaLiterals)
    unittest.TextTestRunner(verbosity=2).run(suite)
 
