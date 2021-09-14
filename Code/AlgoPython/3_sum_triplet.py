
def threeSum(nums):
    nums.sort()
    ans = []
    i = 0
    while i < len(nums) - 2:
        j = i + 1
        k = len(nums) - 1
        while j < k:
            target = nums[i] + nums[j] + nums[k]
            if target == 0:
                ans.append([i, j, k])
                temp_k = k
                temp_j = j
                while nums[temp_k] == nums[temp_k - 1] and j < temp_k - 1:
                    ans.append([i, j, temp_k - 1])
                    temp_k -= 1
                while nums[temp_j] == nums[temp_j + 1] and temp_j + 1 < k:
                    ans.append([i, temp_j + 1, k])
                    temp_j += 1
                while nums[j] == nums[j + 1] and nums[k] == nums[k - 1] and j + 1 < k - 1:
                    ans.append([i, j + 1, k - 1])
                    j += 1
                    k -= 1
                j += 1
                k -= 1
            elif target > 0:
                k -= 1
            else:
                j += 1
        i += 1
            
    return ans


test_case = [[-5, 2, 2, 3, 3], [-4, 2, 2, 2, 2]]

for nums in test_case:
    print("test case: " + str(nums))
    ans = threeSum(nums)
    print(" ans: " + str(ans))
    


                
            
        
        
        
