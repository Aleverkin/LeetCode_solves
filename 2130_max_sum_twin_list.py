def pairSum(self, head: Optional[ListNode]) -> int:
    def reverse_list(head):
        dummy = None

        while head:
            temp = head.next
            head.next = dummy
            dummy = head
            head = temp

        return dummy


    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    slow = slow.next
    slow = reverse_list(slow)

    max_twin_sum = 0

    while slow:
        val = slow.val + head.val
        if val > max_twin_sum:
            max_twin_sum = val

        slow = slow.next
        head = head.next

    return max_twin_sum