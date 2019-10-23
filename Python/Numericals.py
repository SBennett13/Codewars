#!/usr/bin/env python3
"""
Scott Bennett, scottbennett027@gmail.com

Problem:
You are given an input string.

For each symbol in the string if it's the first character occurence, replace it with a '1', else replace it with the amount of times you've already seen it...

But will your code be performant enough?

Examples:
input   =  "Hello, World!"
result  =  "1112111121311"

input   =  "aaaaaaaaaaaa"
result  =  "123456789101112"

Link: www.codewars.com/kata/numericals-of-a-string
"""
import unittest

def numericals(s):
    result,d = "", dict()

    # If you haven't seen the char before, it isn't in the dict,
    # so set its val to one, if you have, increment its val
    # then append to the result string
    for i in s:
        if d.get(i) == None:
            d[i] = 1
        else:
            d[i] = d[i]+1
        result += str(d[i])
    return result

class UnitTests(unittest.TestCase):

    def test_kata(self):
        self.assertEqual(numericals("Hello, World!"), "1112111121311")
        self.assertEqual(numericals("Hello, World! It's me, JomoPipi!"), "11121111213112111131224132411122")
        self.assertEqual(numericals("hello hello"), "11121122342")
        self.assertEqual(numericals("Hello"), "11121")
        self.assertEqual(numericals("aaaaaaaaaaaa"),"123456789101112")

if __name__ == '__main__':
    unittest.main()