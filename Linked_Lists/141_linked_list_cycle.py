def hasCycle(self, head: Optional[ListNode]) -> bool:
    if not head:
        return False

    head.val = None
    head = head.next

    while head:
        if head.val == None:
            return True

        head.val = None
        head = head.next

    return False