class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
         vector<int> r;
   unordered_map<int, int> m;
    for(int i = 0; i < nums.size(); i++){
         int complement = target - nums[i];
         if(m.find(complement) != m.end()){
              r.push_back(m[complement]);
              r.push_back(i);
              return r;
         }
         m[nums[i]] = i;
    }

    }
};
