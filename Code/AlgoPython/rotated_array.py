class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        
        # 等号要有，如果是一个元素的话，没有等号就直接跳过返回-1，如果这单个元素刚好是target 那-1就是错的
        while (left <= right):
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # 没有重复元素，所以这里可以去掉等号
            if nums[mid] < nums[right]:
                # and后面的判断不能省，因为有rotation存在，如果仅仅是比mid大的话就去搜索右边，可能会错过真正的解
                # 假设 [3,5,6,7,0,1,2], target = 3，在第一轮中
                # target不仅比nums[mid]大，还比nums[right]大，这种情况我们搜右边会搜索不到，但其实答案是存在的
                # 只不过被rotate到左边去了，这种情况下，我们实际应该去左边搜索
                if target > nums[mid] and target <= nums[right]: # target <= 也是必须，不然如果target=nums[right]，我们会走左边，那就漏解了
                    left = mid + 1
                else:
                    # right也必须要减一，因为有可能会mid=right=left，不减的话死循环
                    # 因为已经判断过nums[mid]不是解，所以不会漏
                    right = mid -1
            else:
                # 同理 这里target <=nums[mid]的等号无意义，nums[mid]==target的话就已经返回了
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid +1
        return -1