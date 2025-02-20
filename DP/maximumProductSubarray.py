class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        maxProd = [0] * n
        minProd = [0] * n
        maxProd[0] = nums[0]
        minProd[0] = nums[0]
        res = nums[0]

        for i in range(1,n):
            maxProd[i] = max(nums[i], nums[i] * maxProd[i-1], nums[i] * minProd[i-1])
            minProd[i] = min(nums[i], nums[i] * maxProd[i-1], nums[i] * minProd[i-1])
            res = max(res, maxProd[i])

        return res

# Question: https://leetcode.com/problems/maximum-product-subarray/

