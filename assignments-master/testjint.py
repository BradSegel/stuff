from javaint_regex import regex_java_int

numerals = ['0l','0777L','0x100000000L','2_147_483_648L','0xC0B0L','0','2','0372','0xDada_Cafe','1996', '0x00_FF__00_FF']

with open("testdata", 'r') as f:
    td = f.read().replace('\n','').replace('"','').split(',')


for x in td: print '%s is a legal javaint: %s' % (str(x), regex_java_int(x))



