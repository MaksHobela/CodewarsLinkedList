def stringify(node):
    if not node:
        return 'None'
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    return " -> ".join(result) + " -> None"