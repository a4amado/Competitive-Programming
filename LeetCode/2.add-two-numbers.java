/*
 * @lc app=leetcode id=2 lang=java
 *
 * [2] Add Two Numbers
 */

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int rmaining = 0;
        ListNode Curr_1 = l1;
        ListNode Curr_2 = l2;
        ListNode head = new ListNode();

        ListNode Dhead = head;

        while (Curr_1 != null || Curr_2 != null || rmaining != 0) {
            int sum = (Curr_1 == null? 0 : Curr_1.val) + (Curr_2 == null? 0 : Curr_2.val) + rmaining;
            rmaining = sum / 10;
            int v = sum % 10;

            Dhead.next = new ListNode(v);
            Dhead = Dhead.next;

            Curr_1 = (Curr_1 != null? Curr_1.next : null) ;
            Curr_2 = (Curr_2 != null? Curr_2.next : null) ;
              

        }
        head = head.next;
        return head;
    }
}

// @lc code=end
