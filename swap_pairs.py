from preloaded import Node

def swap_pairs(head):
    start = Node(0)
    start.next = head
    prev = start
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
    
    return start.next