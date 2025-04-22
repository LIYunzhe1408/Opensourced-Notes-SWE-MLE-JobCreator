class Solution {
public:
    bool isAnagram(string s, string t) {
        // For different length.
        int s_length = s.size(), t_length = t.size();
        if (s_length != t_length)
            return false;

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        // Replace the following by: return s == t;
        for (int i = 0; i < s_length; i++) {
            if (s[i] != t[i])
                return false;
        }
        return true;
    }
};