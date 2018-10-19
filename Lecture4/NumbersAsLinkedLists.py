class LinkedListNode:
    def __init__(self, item, next_node = None):
        self.item = item
        self.next_node = next_node


def print_number(node):
    res = []
    curr_node = node
    while curr_node is not None:
        res.append(curr_node.item)
        curr_node = curr_node.next_node

    print("".join(reversed([str(x) for x in res])))


def sum_linked_lists(l1, l2):
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    result_node = current_node = LinkedListNode((l1.item + l2.item) % 10, None)
    overflow = (l1.item + l2.item) // 10
    l1 = l1.next_node
    l2 = l2.next_node

    while l1 is not None and l2 is not None:
        curr_item = (l1.item + l2.item + overflow) % 10
        current_node.next_node = LinkedListNode(curr_item, None)
        current_node = current_node.next_node
        overflow = (l1.item + l2.item + overflow) // 10

        l1 = l1.next_node
        l2 = l2.next_node

    if l1 is None:
        l1 = l2

    while l1 is not None:
        curr_item = (l1.item + overflow) % 10
        current_node.next_node = LinkedListNode(curr_item, None)
        current_node = current_node.next_node
        overflow = (l1.item + overflow) // 10

        l1 = l1.next_node

    if overflow != 0:
        current_node.next_node = LinkedListNode(overflow, None)

    return result_node

# 4682
n1 = LinkedListNode(9, LinkedListNode(9, LinkedListNode(9, LinkedListNode(9, None))))
# 145
n2 = LinkedListNode(9, LinkedListNode(9, LinkedListNode(9, None)))

print_number(sum_linked_lists(n1, n2))
