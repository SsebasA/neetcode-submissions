class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
           vector<int> r;
    int n = numbers.size();
    int i = 0;
    int j = n -1 ;
    while(i <= j){
        if(numbers[i] + numbers[j] == target){
            r.push_back(i+1);
            r.push_back(j+1);
            return r;
        } else if(numbers[i] + numbers[j] < target){
            i++;
        } else {
            j--;
        }
    }
    }
};
