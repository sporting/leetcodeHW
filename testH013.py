from H012IntegerToRoman.t01 import Solution as ItoR
from H013RomanToInteger.t01 import Solution as RtoI

itoR = ItoR()
rtoI = RtoI()

for num in xrange(1, 99999):
    s = itoR.intToRoman(num)
    i = rtoI.romanToInt(s)

    print '{:5d}: {:5d} {} '.format(num, i, s)

    if num != i:
        print 'ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ',str(num)
