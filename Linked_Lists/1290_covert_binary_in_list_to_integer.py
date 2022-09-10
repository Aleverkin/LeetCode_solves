# 1
# 101
# 0

val_list = []
while head:
    val_list.append(head.val)
    head = head.next

res = 0
poww = len(val_list) - 1
for x in val_list:
    res += (2 ** poww) * x
    poww -= 1

return res