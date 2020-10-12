class ListNode:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next


def merge_two_sorted_lists(L1: ListNode, L2: ListNode) -> ListNode:
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <L2.data:
            tail.next, L1 = L1, L1.next
        else :
            tail.next, L2 = L2, L2.next

        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next


d8 = ListNode(8)
d7 = ListNode(7,d8)
d6 = ListNode(6,d7)
d5 = ListNode(5,d6)
d4 = ListNode(4,d5)
d3 = ListNode(3,d4)
d2 = ListNode(2,d3)
d1 = ListNode(1,d2)



t1 = ListNode(14)
t2 = ListNode(15,t1)
t3 = ListNode(16,t2)

m = merge_two_sorted_lists(d3,t3)

while (m.next!=None):
    print(m.data)
    m =  m.next

# reverse linked list of specific region

def reverse_sublist(L:ListNode, start:int, finish: int) -> ListNode:
    dummy_head = sublist_head = ListNode(0,L)
    for _ in range(1,start):
        sublist_head = sublist_head.next

    # Reverse sublist

    sublist_iter = sublist_head.next
    for _ in range(finish-start):
        temp = sublist_iter.next
        sublist_iter.next,temp.next,sublist_head.next = (temp.next,sublist_iter,sublist_iter.next)

    return dummy_head.next


m = reverse_sublist(d1,3,6)
while (m.next!=None):
    print(m.data)
    m =  m.next