class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        num_digits = len(str(nums[0]))
        total = 0

        for p in range(num_digits):
            freq = {}
            for num in nums:
                digit = (num // 10**p) % 10
                freq[digit] = freq.get(digit, 0) + 1

            pairs = 0
            for digit in freq:
                pairs += freq[digit] * (n - freq[digit])
            total += pairs // 2

        return total
