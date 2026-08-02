class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in range(9, -1, -1):
            triple = str(digit) * 3
            if triple in num:
                return triple
        return " "


s = Solution()
print(s.largestGoodInteger("6777133339"))
