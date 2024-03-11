import java.util.*;

/*
 * @lc app=leetcode id=15 lang=java
 *
 * [15] 3Sum
 */


// @lc code=start
class Solution {
 
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> l = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) return l;

            if (i > 0) {
                if (nums[i] == nums[i - 1]) {
                    continue;
                }
            }
            for (List<Integer> ll : this.get_all_pairs(nums, i, nums[i])) {
                l.add(ll);
            }

        }
        return l;
    }

    ArrayList<ArrayList<Integer>> get_all_pairs(int[] list, Integer start, Integer curr) {

        int[] new_range = Arrays.copyOfRange(list, start + 1, list.length);
       
        int r = new_range.length - 1;
        int l = 0;
        ArrayList<ArrayList<Integer>> ll = new ArrayList<>();

        while (r > l) {
            if (l > 0) {
                if (new_range[l] == new_range[l-1]) {
                    l++;
                    continue;
                }
            }
            if (r < new_range.length - 1) {
                if (new_range[r] == new_range[r+1]) {
                    r--;
                    continue;
                }
            }
            Integer curr_sum = new_range[r] + new_range[l] + curr;

            if (curr_sum > 0) {
                r--;
            } else if (curr_sum < 0) {
                l++;
            } else {
                ArrayList<Integer> lll = new ArrayList<>();
                lll.add(curr);
                lll.add(new_range[l]);
                lll.add(new_range[r]);
                ll.add(lll);
                r--;
                l++;

            }

        }
        return ll;
    };

}
// @lc code=end
