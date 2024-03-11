
/*
 * @lc app=leetcode id=268 lang=java
 *
 * [268] Missing Number
 */
import java.lang.reflect.Array;
import java.util.*;

// @lc code=start

class Solution {
    public int missingNumber(int[] nums) {

        // Sorting the array
        Arrays.sort(nums);

        int missing = 0;

        for (int i = 0; i <= nums.length; i++) {
            // Check if the current number is equal to the index
            if (i >= nums.length || nums[i] != i) {
                missing = i;
                break;
            }
        }

        return missing;
    }
}
// @lc code=end
