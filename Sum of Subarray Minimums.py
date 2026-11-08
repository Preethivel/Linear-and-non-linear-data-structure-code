class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # left boundaries
        stack = []
        left = [0] * n
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)
        
        # right boundaries
        stack = []
        right = [0] * n
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = len(arr) - i if not stack else stack[-1] - i
            stack.append(i)
        
        # calculate answer
        return sum(arr[i] * left[i] * right[i] for i in range(n)) % MOD
