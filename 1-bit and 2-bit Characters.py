'''We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

'''


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        flag = False
        while i < n:
            if bits[i] == 0:
                i += 1
                flag = True
            else:
                i += 2
                flag = False
        return flag
