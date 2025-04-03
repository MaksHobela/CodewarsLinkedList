class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s.lower() in ["null", "nil", "nullptr", "null()"]:
        return None

    values = s.split(" -> ")

    if values[-1].lower() in ["null", "nil", "nullptr", "null()"]:
        values = values[:-1]

    head = None
    active = None

    for value in values:
        try:
            int_value = int(value)
        except ValueError:
            continue

        new_node = Node(int_value)

        if head is None:
            head = new_node
            active = head
        else:
            active.next = new_node
            active = active.next

    return head