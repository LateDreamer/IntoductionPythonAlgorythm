from linkedlist_FIFO import LinkedListFIFO
from node import Node

class CircularLinkedListFIFO(LinkedListFIFO):
    def _add(self, value):
        self.length += 1
        node = Node(value, self.head)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

def isCircularll(ll):
    p1 = ll.head
    p2 = ll.head

    while p2:
        try:
            p1 = p1.pointer
            p2 = p2.pointer.pointer
        except:
            break

        if p1 == p2:
            return True
    return False

def test_isCircularll():
    ll = LinkedListFIFO()
    for i in range(10):
        ll.addNode(i)
    assert(isCircularll(ll) is False)

    lcirc = CircularLinkedListFIFO()
    for i in range(10):
        lcirc.addNode(i)
    assert(isCircularll(lcirc) is True)

    print("테스트 통과!")

if __name__ == "__main__":
    test_isCircularll()
