

/*
 * @lc app=leetcode id=19 lang=java
 *
 * [19] Remove Nth Node From End of List
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        int length = 0;
        // get the length of the linked list
        ListNode curr = head;
        while (curr != null) {
            length++;
            curr = curr.next;
        }
        
        if (n == length) {
            head = head.next;
            return head;
        }

        int i_from_the_beggining = length  - n;

        int i = 0;
        curr = head;
        while (i <= i_from_the_beggining) {
            if (i == i_from_the_beggining -1) {
                // replace and break
                curr.next = curr.next.next;
                break;
            }
            curr = curr.next;
            i++;
        }
        return head;
    }
}
// @lc code=end
