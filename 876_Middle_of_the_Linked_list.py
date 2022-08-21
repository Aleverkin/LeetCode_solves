head = linked_list
length = 0

head1 = head
while head1 != None:
    length += 1
    head1 = head1.next

m = int(length / 2)

for _ in range(m - 1):
    head = head.next

print(head.val)
