""" Chen Wang cwang0688@gmail.com
""" 

def binarySearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        # Prevent arithmetic overflow
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1

def main():
    nums = [1,2,3,5]
    target = 4
    print(binarySearch(nums, 4))

main()
    