from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_len = len(digits)
        digits.reverse()
        for idx, val in enumerate(digits):
            n = val + 1
            if n > 9:
                digits[idx] = 0
                if idx+1 == digits_len:
                    digits.append(0)
            else:
                digits[idx] = n
                digits.reverse()
                if digits[0] == 0:
                    digits.remove(0)
                return digits

        digits.reverse()
        if digits[0] == 0:
            digits.remove(0)
        return digits


result = Solution().plusOne([9,9,9])
print(result)
