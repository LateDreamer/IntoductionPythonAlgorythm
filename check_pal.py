from linkedlist_FIFO import LinkedListFIFO
from node import Node

def isPal(l1):
    if len(l1) < 2:
        return True
    if l1[0] != l1[-1]:
        return False
    return isPal(l1[1:-1])

def checkPal(ll):
    node = ll.head
    l = []

    while node is not None:
        l.append(node.value)
        node = node.pointer

    return isPal(l)

def tesk_checkllPal():
    ll = LinkedListFIFO()
    l1 = [1,2,3,2,1]
    for i in l1:
        ll.addNode(i)
    assert(checkPal(ll) is True)

    ll.addNode(2)
    ll.addNode(3)
    assert(checkPal(ll) is False)

    print("테스트 통과!")

if __name__ == "__main__":
    tesk_checkllPal()