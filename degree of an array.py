 def findShortestSubArray(self, nums: list[int]) -> int:
        first = {}   
        count = {}   
        degree = 0
        result = 0

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            count[num] = count.get(num, 0) + 1

            length = i - first[num] + 1
            if count[num] > degree:
                degree = count[num]
                result = length
            elif count[num] == degree:
                result = min(result, length)

        return result
