class Solution {
public:
    bool isPalindrome(string s) {
    vector<char> v;
    int cnt = 0;
    for(int i = 0; i < s.size(); i++){
        if(s [i] != ' ' && s[i] != '?' && s[i] != '.' && s[i] != ',' && s[i] != '!' && s[i] != '\'' && s[i] != ':'){
            v.push_back(tolower(s[i]));
            cnt++;
        }
    }
    /*
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    } 
    */  
    int n = v.size();
    int i = 0;
    int j = n - 1;
    while(i < j){
        if(v[i] == v[j]){
            cnt--;
            i++;
            j--;
        } else {
            return false;
        }
    }
    return true;
 
    }
};
