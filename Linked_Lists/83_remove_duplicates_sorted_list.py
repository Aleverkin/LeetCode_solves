def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    head_main, dummy = head, head
    while head:
        if head.val > dummy.val:
            dummy.next = head
            dummy = head

        head = head.next

    dummy.next = None

    return head_main