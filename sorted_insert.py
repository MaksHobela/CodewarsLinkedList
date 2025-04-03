class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    newnode = Node(data)
    if head is None or head.data >= data:
        newnode.next = head
        return newnode
    active = head
    while active.next is not None and active.next.data < data:
        active = active.next
    newnode.next = active.next
    active.next = newnode
    return head