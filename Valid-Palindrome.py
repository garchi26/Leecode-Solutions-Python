'''
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s1=re.sub("[^A-Za-z0-9]","",s).lower()
        if (s1[::] == s1[::-1]):
            return True
        else:
            return False
