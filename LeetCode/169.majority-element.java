/*
 * @lc app=leetcode id=169 lang=java
 *
 * [169] Majority Element
 */
import java.util.ArrayList;
import java.util.HashMap;
// @lc code=start
class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> l = new HashMap<>();
        int max_ = nums[0];
        int times = 0;
        for (int i : nums) {
            if (l.get(i) == null) {
                l.put(i, 1);
                continue;
            };
            l.replace(i, l.get(i) + 1);
            if (l.get(i) > times)  {
                max_ = i;
                times = l.get(i);
            }
        }

        return max_;

        
    }
}
// @lc code=end

