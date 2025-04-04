def loop_size(node):
    fast = node
    slow = fast
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return 0
    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next
    count = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        count += 1
    return count
