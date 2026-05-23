class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        /*
        Complex = O(nlogn) Space = O(1)
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == nums[i+1]){
                return true;
            }
        }
        return false;
        */
        //Hashset 
        //Complex O(n) Space: O(n)
        unordered_set<int> hashSet;
        for(int i = 0; i < nums.size(); i++){
            if(hashSet.find(nums[i]) != hashSet.end()){
                return true;
            }  
            hashSet.insert(nums[i]);
        }
        return false;

        
    }
};
