# Solved

# By 13.06.2024:
# Runtime = 44 ms (beats 25.35% of users)
# Memory = 16.59 MB (beats 64.11% of users)
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Check if 1st list is empty or "m" value equals to 0
        if nums1 is None or m == 0:
            # Clear the 1st list
            nums1.clear()
            # Insert "n" values from the 2nd list to the 1st one
            nums1.extend(nums2[:n])
        
        # Check if 2nd list is empty or "n" value equals to 0
        elif nums2 is None or n == 0:
            # While the length of the 1st list is greater than "m"
            while len(nums1) > m:
                # Delete last values from the 1st list
                nums1.pop()
                
        else:
            # While the length of the 1st list is greater than "m"
            while len(nums1) > m:
                # Delete last values from the 1st list
                nums1.pop()
            
            # While the length of the 2nd list is greater than "n"    
            while len(nums2) > n:
                # Delete last values from the 2nd list
                nums2.pop()
            
            # Variables to point to the indexes of 2 lists for 
            # comparison    
            i, j = 0, 0
            
            # While the 1st pointer doesn't go out of the 1st 
            # list length and the 2nd pointer is less than "n"    
            while i < len(nums1) and j < n:
                # Comparison between certain values of 2 lists. 
                # Checking if a certain value from the 1st list 
                # is greater than from the 2nd one
                if nums1[i] > nums2[j]:
                    # Insert "j" value of the 2nd list into the 
                    # "i" position of the 1st list
                    nums1.insert(i, nums2[j])
                    # Move the 2nd pointer next
                    j += 1    
                
                # Move the 1st pointer next    
                i += 1
            
            # Check if there's still left not inserted values 
            # from the 2nd list    
            if j < len(nums2):
                # Insert left values to the end of the 1st list
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