def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    currA, currB = headA, headB
    lenA = lenB = 0

    while currA or currB:
        if currA:
            lenA += 1
            currA = currA.next

        if currB:
            lenB += 1
            currB = currB.next

    if lenA >= lenB:
        long = headA
        short = headB
    else:
        long = headB
        short = headA

    for i in range(abs(lenA - lenB)):
        long = long.next

    while long:
        if long == short:
            return long
        long = long.next
        short = short.next

    return None