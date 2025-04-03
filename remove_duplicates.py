class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    active = head
    while active and active.next:
        if active.data == active.next.data:
            active.next = active.next.next
        else:
            active = active.next
    return head