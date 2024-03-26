#!/usr/bin/env python
# coding: utf-8

# In[1]:


##search insert position
def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

# Test cases
nums1 = [1, 3, 5, 6]
target1 = 5
print(search_insert_position(nums1, target1))  # Output: 2

nums2 = [1, 3, 5, 6]
target2 = 2
print(search_insert_position(nums2, target2))  # Output: 1

nums3 = [1, 3, 5, 6]
target3 = 7
print(search_insert_position(nums3, target3))  # Output: 4


# In[2]:


##search a 2D matrix
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        mid_element = matrix[mid // n][mid % n]
        
        if mid_element == target:
            return True
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Test cases
matrix1 = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target1 = 3
print(searchMatrix(matrix1, target1))  # Output: true

matrix2 = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target2 = 13
print(searchMatrix(matrix2, target2))  # Output: false


# In[3]:


##search in rotated sorted array
def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            # If target is within the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, the right half is sorted
        else:
            # If target is within the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Example usage:
nums1 = [4,5,6,7,0,1,2]
target1 = 0
print(search(nums1, target1))  # Output: 4

nums2 = [4,5,6,7,0,1,2]
target2 = 3
print(search(nums2, target2))  # Output: -1

nums3 = [1]
target3 = 0
print(search(nums3, target3))  # Output: -1


# In[4]:


## Find First and last position of element in sorted array(34)
def searchRange(nums, target):
    def find_start(nums, target):
        start = -1
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    start = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return start
    
    def find_end(nums, target):
        end = -1
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    end = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return end
    
    start = find_start(nums, target)
    end = find_end(nums, target)
    
    return [start, end]

# Example usage:
nums1 = [5,7,7,8,8,10]
target1 = 8
print(searchRange(nums1, target1))  # Output: [3, 4]

nums2 = [5,7,7,8,8,10]
target2 = 6
print(searchRange(nums2, target2))  # Output: [-1, -1]

nums3 = []
target3 = 0
print(searchRange(nums3, target3))  # Output: [-1, -1]


# In[5]:


##missing number(268)
def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example usage:
nums1 = [3,0,1]
print(missingNumber(nums1))  # Output: 2

nums2 = [0,1]
print(missingNumber(nums2))  # Output: 2

nums3 = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums3))  # Output: 8


# In[ ]:




