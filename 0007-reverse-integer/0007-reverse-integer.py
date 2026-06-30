class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = str(x)
        if x>0:
            rev = n[::-1]
            y = int(rev)
            if -(2**31) <= y <= (2**31 - 1):
                return y
            return 0
        elif x<0:
            ab = abs(x)
            n = str(ab)
            rev = n[::-1]
            y = -int(rev)
            if -(2**31) <= y <= (2**31 - 1):
                return y
            return 0
        else:
            return x
             
