from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    active = node
    actindex = 0
    
    while active:
        if actindex == index:
            return active
        active = active.next
        actindex += 1
    raise Exception