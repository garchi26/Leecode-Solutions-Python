'''
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = ''.join(sorted(s))
        t1= ''.join(sorted(t))
        if(s1 == t1):
            return True
        else:
            return False
