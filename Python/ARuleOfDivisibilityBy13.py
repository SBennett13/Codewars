#!/usr/bin/env python3
"""
Scott Bennett, scottbennett027@gmail.com

Problem: When you divide the successive powers of 10 by 13 you get the following remainders of the integer divisions:

1, 10, 9, 12, 3, 4.

Then the whole pattern repeats.

Hence the following method: Multiply the right most digit of the number with the left most number in the sequence shown above, the second right most digit to the second left most digit of the number in the sequence. The cycle goes on and you sum all these products. Repeat this process until the sequence of sums is stationary.

...........................................................................

Example: What is the remainder when 1234567 is divided by 13?

7×1 + 6×10 + 5×9 + 4×12 + 3×3 + 2×4 + 1×1 = 178

We repeat the process with 178:

8x1 + 7x10 + 1x9 = 87

and again with 87:

7x1 + 8x10 = 87

...........................................................................

From now on the sequence is stationary and the remainder of 1234567 by 13 is the same as the remainder of 87 by 13: 9

Call thirt the function which processes this sequence of operations on an integer n (>=0). thirt will return the stationary number.

thirt(1234567) calculates 178, then 87, then 87 and returns 87.

thirt(321) calculates 48, 48 and returns 48

Link: https://www.codewars.com/kata/564057bc348c7200bd0000ff
"""
import unittest

def thirt(n):
    seq = [1,10,9,12,3,4]
    lastV = n
    while (1):
        valS = str(lastV)
        newV = 0
        for v in range(len(valS)):
            newV += seq[v%len(seq)]*int(valS[len(valS)-1-v])
        if newV == lastV:
            return lastV
        else:
            lastV = newV

class UnitTests(unittest.TestCase):

    def test_kata(self):
        self.assertEqual(thirt(1234567), 87)
        self.assertEqual(thirt(85299258), 31)
        self.assertEqual(thirt(5634), 57)
        self.assertEqual(thirt(1111111111), 71)
        self.assertEqual(thirt(987654321), 30)

if __name__ == '__main__':
    unittest.main()