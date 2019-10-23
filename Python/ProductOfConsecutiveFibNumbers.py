#!/usr/bin/env python3
"""
Scott Bennett, scottbennett027@gmail.com

Problem:
The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return

[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(m) being the smallest one such as F(m) * F(m+1) > prod.

Examples
productFib(714) # should return [21, 34, true], 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false], 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55


Link: https://www.codewars.com/kata/product-of-consecutive-fib-numbers
"""

import math, unittest

def productFib(prod):
    
    # First two values of the sequence
    fib = [0, 1]
    
    # while the product of the last two is less than
    # the desired product, append the next value
    while fib[len(fib)-1] * fib[len(fib)-2] < prod:
        fib.append(fib[len(fib)-1]+fib[len(fib)-2])
    
    # If the product of the last two is equal, return the
    # values and true
    if fib[len(fib)-1]*fib[len(fib)-2] == prod:
        return [fib[len(fib)-2],fib[len(fib)-1], True]
    # Otherwise, return the last values and false
    else:
        return [fib[len(fib)-2],fib[len(fib)-1], False]

class UnitTests(unittest.TestCase):

    def test_kata(self):
        self.assertEqual(productFib(4895), [55, 89, True])
        self.assertEqual(productFib(5895), [89, 144, False])

if __name__ == '__main__':
    unittest.main()