// Sort List

public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    ListNode sortList(ListNode head) {
        ListNode tracker = head;
        if(head == null) {
            return head;
        }
        while(tracker.next != null) {
            ListNode curr = head;
            while(curr.next != null) {
                if(curr.val > curr.next.val) {
                    swapValue(curr, curr.next);
                }
                curr = curr.next;
            }
            tracker = tracker.next;
        }
        return head;
    }
    
    void swapValue(ListNode n1, ListNode n2) {
        int temp = n1.val;
        n1.val = n2.val;
        n2.val = temp;
    }
}