# Time Complexity was O(N), Space complexity was O(N)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::map<int, int> m;

        for (auto it : nums){
            if (! m.contains(it)){
                m[it] = 1;
            } else {
                m[it] += 1;
            }
        }

        for (const auto& pair:m) {
            if (pair.second > nums.size() / 2)
                return pair.first;
        }
        return 0;
    }
};

# Moore Voting Algorithm
# As long as you have a majority(i.e. appear time > n / 2), the majority number must be at the very end of the loop.
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0;
        int count = 0;

        for (auto it : nums) {
            if (count == 0) {
                candidate = it;
            }

            if (it == candidate)
                count ++;
            else
                count --;
        }
        return candidate;
    }
};


# Easy solution
# The majority must be in the middle position if sorted.
# But the time complexity was O(Nlog(N)) because of the sorting
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        return nums[n/2];
    }
};