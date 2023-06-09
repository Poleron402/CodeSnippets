#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        wd = str(x)
        if int(wd) <0:
            wd = wd[1:]
            wdrev = '-'+wd[::-1]
        else:
            wdrev = wd[::-1]
        wdrev = int(wdrev)
        if wdrev >= (-2**(31)) and wdrev <= (2**(31)-1):
            return wdrev
        else:
            return 0
