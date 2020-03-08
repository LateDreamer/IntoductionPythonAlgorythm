from stack import Stack

class SetOfStacks(Stack):
    def __init__(self, capacity=4):
        self.setofstacks = []
        self.items = []
        self.capacity = capacity

    def push(self, value):
        if self.size() >= self.capacity:
            self.setofstacks.append(self.items)
            self.items = []
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if self.isEmpty() and self.setofstacks:
            self.items = self.setofstacks.pop()
        return value

    def sizeStack(self):
        return len(self.setofstacks) * self.capacity + self.size()

    def __repr__(self):
        aux = []
        for s in self.setofstacks:
            aux.extend(s)
        aux.extend(self.items)
        return repr(aux)

if __name__ == "__main__":
    capacity = 5
    stack = SetOfStacks(capacity)
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print("스택에 숫자 0~9를 추가합니다.")
    for i in range(10):
        stack.push(i)
    print(stack)
    print("스택 크기: {0}".format(stack.sizeStack()))
    print("peek: {0}".format(stack.peek()))
    print("pop: {0}".format(stack.pop()))
    print("peek: {0}".format(stack.peek()))
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print(stack)