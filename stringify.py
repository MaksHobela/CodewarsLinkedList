class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
    if not node:
        return 'None'
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    return " -> ".join(result) + " -> None"
