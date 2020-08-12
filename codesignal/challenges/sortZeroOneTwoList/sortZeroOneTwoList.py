
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def sortZeroOneTwoList(l):
    count = [0, 0 , 0]
    while l != None:
        if l.value == 0:
            count[0] += 1

        if l.value == 1:
            count[1] += 1

        if l.value == 2:
            count[2] += 1

        l = l.next;

    head = None
    for i in range(2, -1, -1):
        for j in range(0, count[i]):
            temp = ListNode(i)
            temp.next = head
            head = temp
    return head


