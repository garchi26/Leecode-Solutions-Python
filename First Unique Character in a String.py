'''
Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1
'''
# import collections module to get the count of each and every word in dic
# if count is equal to 1 then it will print that value index number in return else at exit, it will print -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections 
        count = collections.Counter(s);        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return(-1)
