class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        values = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    values = [i, j]
                    return values
        
        return values
        
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(nums=[2,7,11,15], target=9))
    print(solution.twoSum(nums=[3,2,4], target=6))
    print(solution.twoSum(nums=[3,3], target=6))