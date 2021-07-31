class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        while left != len(nums):
            right = left + 1
            while right != len(nums):
                if nums[left]+nums[right] == target:
                    return ([left, right])
                else:
                    right += 1
            left += 1
            
result = Solution()
print(result)
