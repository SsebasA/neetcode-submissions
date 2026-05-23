class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
       int n = nums.size();
    
    if (n < 3) {
        return {};
    }
    
    // Ordenamos el vector para facilitar la búsqueda de tripletas
    sort(nums.begin(), nums.end());
    
    vector<vector<int>> r; // Vector para almacenar los resultados
    
    for (int i = 0; i < n - 2; i++) {
        // Evitamos duplicados para el primer número
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        
        int j = i + 1; // Segundo puntero
        int k = n - 1; // Tercer puntero
        int target = 0 - nums[i];
        
        while (j < k) {
            int sum = nums[j] + nums[k];
            
            if (sum == target) {
                r.push_back({nums[i], nums[j], nums[k]});
                
                // Evitamos duplicados para el segundo número
                while (j < k && nums[j] == nums[j + 1]) {
                    j++;
                }
                
                // Evitamos duplicados para el tercer número
                while (j < k && nums[k] == nums[k - 1]) {
                    k--;
                }
                
                j++;
                k--;
            } else if (sum > target) {
                k--;
            } else {
                j++;
            }
        }
    }
    
    return r;
        
    }
};
