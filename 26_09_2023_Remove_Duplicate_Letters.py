"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        make_count = {}
        in_set = set()

        for char in s :
            make_count[char] = make_count.get(char, 0) + 1
        for char in s :
            make_count[char] -= 1
            if char in in_set :
                continue
            while res and char < res[-1] and make_count[res[-1]] > 0:
                in_set.remove(res.pop())
            res.append(char)
            in_set.add(char)
        return ''.join(res)
