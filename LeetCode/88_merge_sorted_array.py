class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if nums1 is None or m == 0:
            nums2[:n]
        
        elif nums2 is None or n == 0:
            nums1[:m]
        
        nums1 = nums1[:m]
        nums2 = nums2[:n]
        i, j = 0, 0
            
        while i < len(nums1) and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1    
                
            i += 1
            
        if j < len(nums2):
            nums1.extend(nums2[j:])
            
if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
    
    nums1 = [1]
    nums2 = []
    m = 1
    n = 0
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
    
    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1)