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


d1 = ListNode(10)
d2 = ListNode(7,d1)
d3 = ListNode(1,d2)

t1 = ListNode(9)
t2 = ListNode(6,t1)
t3 = ListNode(4,t2)

m = merge_two_sorted_lists(d3,t3)

while (m.next!=None):
    print(m.data)
    m =  m.next
