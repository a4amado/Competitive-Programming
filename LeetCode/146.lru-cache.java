/*
 * @lc app=leetcode id=146 lang=java
 *
 * [146] LRU Cache
 */
import java.util.ArrayList;
import java.util.HashMap;
// HashMap

// array

// @lc code=start
class LRUCache {
    HashMap<Integer, Integer> map;
    ArrayList<HashMap<Integer, Integer>> arr_of_contect;
    int cap = 0 ;
    public LRUCache(int capacity) {
        this.cap = capacity;
        this.arr_of_contect = new ArrayList<HashMap<Integer, Integer>>(capacity);
    }
    
    public int get(int key) {
        
    }
    
    public void put(int key, int value) {
        // if this does not exist
        // 1. put it in arr in the pos 0
        // 2. put it in the map as follows  <key, position in the array>
        if (!this.does_exist(key)) {
            
        }
        
    }

    private boolean does_exist(int key) {
        return map.get(key) != null;
    }

    private void update_pos(int key) {

    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
// @lc code=end

