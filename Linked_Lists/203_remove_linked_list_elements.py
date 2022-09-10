def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    while head and (head.val == val):
        head = head.next

    if not head:
        return None

    head_main, dummy = head, head
    head = head.next

    while head:
        if head.val != val:
            dummy.next = head
            dummy = head

        head = head.next

    dummy.next = None

    return head_main