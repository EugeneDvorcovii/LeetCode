class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        for ii in range(len(x_str) // 2):
            if x_str[ii] != x_str[-ii - 1]:
                return False
        return True