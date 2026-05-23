class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left, right, mid;
        right = nums.size();
        left = 0;
        mid = right / 2;
        while(left <= right){
            if(nums[mid] == target){
                return mid;
            } else {
                if(nums[mid] < target){
                    left = mid + 1;
                    mid = (left + right) / 2;
                } else if (nums[mid] > target){
                    right = mid - 1;
                    mid = (left + right) / 2;
                }
            }
        }
        return -1;
    }
};
