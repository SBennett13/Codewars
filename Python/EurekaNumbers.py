#!/usr/bin/env python3
"""
Scott Bennett, scottbennett027@gmail.com

Problem: Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....Eureka!!

The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Let's see some cases:

sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range [a, b] the function should output an empty list.

sum_dig_pow(90, 100) == []
Enjoy it!!

Link: www.codewars.com/kata/take-a-number-and-sum-its-digits-raised-to-the-consecutive-powers-and-dot-dot-dot-eureka
"""

import unittest

def sum_dig_pow(a, b):

    # Make an empty results list
    results = []

    for i in range(a, b+1):

        # If the number is only one digit
        if len(str(i)) == 1:
            results.append(i)
        else:
            strRep = str(i)
            sum = 0

            # For each digit, raise to index power and add to a sum
            for j in range(1, len(strRep)+1):
               sum += pow(int(strRep[j-1]), j)
            if sum == i:
                results.append(i)
    return results

class UnitTests(unittest.TestCase):
    
    def test_kata(self):
        self.assertEqual(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
        self.assertEqual(sum_dig_pow(10, 89),  [89])
        self.assertEqual(sum_dig_pow(10, 100),  [89])
        self.assertEqual(sum_dig_pow(90, 100), [])
        self.assertEqual(sum_dig_pow(89, 135), [89, 135])

if __name__ == '__main__':
    unittest.main()