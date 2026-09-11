class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        output = []
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                prod *= num
        for num in nums:
            if zeroes > 0:
                if zeroes == 1 and num == 0:
                    output.append(prod)
                else:
                    output.append(0)
            else:
                output.append(prod // num)
        return output
        