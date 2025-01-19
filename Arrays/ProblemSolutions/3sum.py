class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            # Skip duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1

            while left < right:
                # If Sum Found
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Move pointers and remove duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                # If Not, Move Pointers
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -=1

        return result

# Question: https://leetcode.com/problems/3sum/            