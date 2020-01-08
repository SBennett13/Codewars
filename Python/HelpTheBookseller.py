#!/usr/bin/env python3
"""
Scott Bennett, scottbennett027@gmail.com

Problem:
A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more capitals letters. The 1st letter of a code is the capital letter of the book category. In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

For example an extract of one of the stocklists could be:

L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
or

L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :

  M = {"A", "B", "C", "W"} 
or

  M = ["A", "B", "C", "W"] or ...
and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.

For the lists L and M of example you have to return the string (in Haskell/Clojure/Racket a list of pairs):

  (A : 20) - (B : 114) - (C : 50) - (W : 0)
where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.

If L or M are empty return string is "" (Clojure and Racket should return an empty array/list instead).

Note:
In the result codes and their values are in the same order as in M.

Link: https://www.codewars.com/kata/54dc6f5a224c26032800005c
"""
import math, unittest

def stock_list(b,c):
    # If c is empty, return nothing
    if not c:
        return ''

    # Make a dictionary to aggregate the books and their counts
    # Grouped by first letter 
    bookDict = {}
    for item in b:

        # Split on the space, if the dict already has this entry, add to it
        # If it is a new entry, enter it into the dict
        sep = item.split()
        if sep[0][0] not in bookDict:
            bookDict[sep[0][0]] = int(sep[1])
        else:
            bookDict[sep[0][0]] += int(sep[1])
    resultStr = []

    # Edge case checker
    numZ = 0

    # For each entry in the query list
    # if it is in the bookDict, then append it to the result str
    # else append it as a zero entry
    for a in c:
        if a in bookDict:
            resultStr.append("(" + a + " : " + str(bookDict[a]) + ")")
        else:
            resultStr.append("(" + a + " : 0)")
            numZ += 1
    
    # Edge Case, if all queries are 0, return empty
    if numZ == len(c):
        return ''
    return(" - ".join(resultStr))

class UnitTests(unittest.TestCase):
    def test_kata(self):
        b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B"]
        self.assertEqual(stock_list(b, c), "(A : 200) - (B : 1140)")

if __name__ == '__main__':
    unittest.main()