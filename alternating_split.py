class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError()
    first = head
    second = head.next
    activefirst = first
    activesecond = second
    while activefirst and activesecond:
        activefirst.next = activesecond.next
        if activefirst.next:
            activefirst = activefirst.next
        else:
            break

        activesecond.next = activefirst.next
        if activesecond.next:
            activesecond = activesecond.next
        else:
            break

    return Context(first, second)
