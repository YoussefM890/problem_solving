from typing import Optional

from leetcode.data_structures import ListNode


class Remove_Nth_Node_From_End_of_List:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow,fast = head,head
        for i in range(n):
            fast = fast.next
        if fast :
            while fast.next != None :
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
        else :
            head = head.next
        return head