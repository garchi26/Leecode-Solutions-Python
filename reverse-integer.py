'''
Input: x = 123
Output: 321

Input: x = -123
Output: -321

'''

class Solution:
    def reverse(self, a: int) -> int:
        count=0
        b=0
        if (a < 0):
            a= -a
            count =1
        while(a != 0 ):
            n= a % 10;
            b= (b*10)+n;
            a= int((a-n)/10);
        if (count == 1):
            b= -b
        powr= pow(2,31) 
        if ((b >= -powr) and (b <= powr)):
            return b
        else:
            return 0
