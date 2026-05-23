class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
    int n = s.size();   
    if(n % 2 != 0){
        return false;
    } else {
        for(int i = 0; i < n; i++){
            if(s[i] == '('){
                st.push(')');
            } else if(s[i] == '{'){
                st.push('}');
            } else if(s[i] == '['){
                st.push(']');
            } else if (s[i] == ')' || s[i] == ']' || s[i] == '}'){
                if(st.empty()){
                    return false;
                } else {
                    char top = st.top();
                    if(top == s[i]){
                        st.pop();
                    } else {
                        return false;
                    }
                }
            }
        }
    }

    if(st.empty()){
        return true;
    } else {
        return false;
    }
    }
};
