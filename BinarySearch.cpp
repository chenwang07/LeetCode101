#include <vector>
using namespace std;

vector<int> nums = { 1,2,3,4,5,6,7,8,9 };


bool binarySearch(vector<int>& nums, int target) {
    int left = 0, right = nums.size();
    // 写法有几种，固定这种比较好
    // https://www.cnblogs.com/grandyang/p/6854825.html
    // 因为是小于right，所以nums[right]是查不到的，所以right一开始初始化就
    // 必须是nums.size()而不是nums.size() - 1，如果是-1的话，最后一个元素是查不到的
    // 同理，更新right的时候必须是right = mid，如果是mid - 1, 那么mid - 1就查不到
    // 而right = mid，就没关系，因为mid在之前的if中已经查过不是了（不然就已经返回了）
    while (left < right) {
        // prevent overflow of large number 
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) 
            return true;
        else if (nums[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid;
        }
    }
    return false;
}