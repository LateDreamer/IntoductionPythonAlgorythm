from stack import Stack

class NodeWithMin(object):
    def __init__(self, value=None, minimum=None):
        self.value = value
        self.minimum = minimum

class StackMin(Stack):
    def __init__(self):
        self.items = []
        self.minimum = None

    def push(self, value):
        if self.isEmpty() or self.minimum > value:
            self.minimum = value
        self.items.append(NodeWithMin(value, self.minimum))

    def peek(self):
        return self.items[-1].value

    def peekMinimum(self):
        return self.items[-1].minimum

    def pop(self):
        item = self.items.pop()
        if item:
            if item.value == self.minimum:
                self.minimum = self.peekMinimum()
            return item.value
        else:
            print('Stack is empty.')

    def __repr__(self):
        aux = []
        for i in self.items:
            aux.append(i.value)
        return repr(aux)

if __name__ == "__main__":
    stack = StackMin()
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print("스택에 숫자 10~1과 1~4를 추가합니다.")
    for i in range(10,0,-1):
        stack.push(i)
    for i in range(1,5):
        stack.push(i)
    print(stack)

    print("스택 크기: {0}".format(stack.size()))
    print("peek: {0}".format(stack.peek()))
    print("peekMinimum: {0}".format(stack.peekMinimum()))
    print("pop: {0}".format(stack.pop()))
    print("peek: {0}".format(stack.peek()))
    print("peekMinimum: {0}".format(stack.peekMinimum()))
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print(stack)