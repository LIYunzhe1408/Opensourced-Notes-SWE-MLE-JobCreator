#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;

        while (j >= 0) {
            // nums1 might be null
            if (i >= 0 && nums1[i] > nums2[j])
                nums1[k--] = nums1[i--];
            else
                nums1[k--] = nums2[j--];
        }
    }
};


// STL Method: Time Complexity will be O((m+n)log(m+n))
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for (int i = m, j = 0; j < n; i++, j++) {
            nums1[i] = nums2[j];
        }
        sort(nums1.begin(), nums1.end());
    }
};