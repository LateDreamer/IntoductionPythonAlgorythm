from linkedlist_FIFO import LinkedListFIFO
from node import Node

def partList(ll, n):
    more = LinkedListFIFO()
    less = LinkedListFIFO()

    node = ll.head

    while node:
        item = node.value

        if item < n:
            less.addNode(item)

        elif item > n:
            more.addNode(item)

        node = node.pointer

    less.addNode(n)
    nodemore = more.head

    while nodemore:
        less.addNode(nodemore.value)
        nodemore = nodemore.pointer

    return less

if __name__ == "__main__":
    ll = LinkedListFIFO()
    l = [6,7,3,4,9,5,1,2,8]
    for i in l:
        ll.addNode(i)

    print("분할 전: ")
    ll._printList()

    print("분할 후: ")
    newll = partList(ll, 6)
    newll._printList()