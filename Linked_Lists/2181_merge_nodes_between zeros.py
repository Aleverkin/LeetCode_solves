# l = [2, 10 ^ ^ 5)
#
# no
# two
# cons
# with 0
#     begin and end
#     start
#     with 0
#
# 0
# 1
# 0

node_accum = head.next
head = head.next
head_main = node_accum

val = 0
while head:
    if head.val != 0:
        val += head.val
    else:
        node_accum.val = val
        node_accum.next = head.next
        node_accum = head.next
        val = 0

    head = head.next

return head_main
