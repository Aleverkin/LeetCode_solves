# [][]
# [1 1 1 2][1]

list_merged_main, list_merged = None, None

if list1 and list2:
    if list1.val <= list2.val:
        list_merged_main = list_merged = list1
        list1 = list1.next
    else:
        list_merged_main = list_merged = list2
        list2 = list2.next

    # next steps
    while list1 or list2:
        val_1 = list1.val if list1 else 500
        val_2 = list2.val if list2 else 500

        if val_1 <= val_2 and list1:
            list_merged.next = list1
            list_merged, list1 = list_merged.next, list1.next
        else:
            list_merged.next = list2
            list_merged, list2 = list_merged.next, list2.next

elif list1:
    list_merged_main = list1
elif list2:
    list_merged_main = list2

return list_merged_main


# without dummy
if not list1 and not list2:
	return list1
if not list1 or not list2:
	return list1 if not list2 else list1

seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
head_main = seek

while seek and target:
	while seek.next and seek.next.val < target.val:
		seek = seek.next

	seek.next, target = target, seek.next
	seek = seek.next

return head_main

# Через dummy:

cur = dummy = ListNode()

while list1 and list2:
	if list1.val < list2.val:
		cur.next = list1
		cur, list1 = cur.next, list1.next
	else:
		cur.next = list2
		cur, list2 = cur.next, list2.next

if list1 or list2:
	cur.next = list1 if list1 else list2

return dummy.next













