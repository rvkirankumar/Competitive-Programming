class Node:
    def __init__(self, _data, _next=None):
        self.data = _data
        self.next = _next


class LinkedList:
    def __init__(self, _items=[]):
        self.head = None
        self.tail = None
        self.count = 0

        for item in _items:
            self.append(item)

    def append(self, _data):
        new_node = Node(_data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def insert(self, _data, pos):
        new_node = Node(_data)
        if pos <= 0:
            new_node.next = self.head
            self.head = new_node
        elif pos >= self.count:
            self.tail.next = new_node
            self.tail = new_node
        else:
            tmp = self.head
            for _ in range(pos - 1):
                tmp = tmp.next
            new_node.next = tmp.next
            tmp.next = new_node

    def pop(self, pos=None):
        if not pos:
            _ptr = self.head
            for _ in range(self.count - 2):
                _ptr = _ptr.next
            tmp = _ptr.next
            _ptr.next = None
            self.tail = _ptr

        elif 0 < pos < self.count:
            _ptr = self.head
            for _ in range(pos - 1):
                _ptr = _ptr.next
            tmp = _ptr.next
            _ptr.next = None

        _data = tmp.data
        del tmp
        self.count -= 1
        return _data

    def remove(self,  pos):

        if pos <= 0:
            _ptr = self.head
            self.head = _ptr.next
            del _ptr
            self.count -= 1
        else:
            _ptr = self.head
            _tmp = self.head
            for _ in range(pos - 2):
                _ptr = _ptr.next
                _tmp = _tmp.next
            _tmp = _tmp.next
            _ptr.next = _tmp.next
            del _ptr
        return

    def __str__(self):
        _head = self.head
        s = "head -> "

        while _head:
            s += str(_head.data) + " -> "
            _head = _head.next

        s += "None"
        return s

    def __repr__(self):
        _head = self.head
        l = []
        while _head:
            l.append(str(_head.data))
            _head = _head.next

        return f"LinkedList([{', '.join(l)}])"


if __name__ == '__main__':
    ll = LinkedList([5, 6, 2, 4, 8, 1, 9])
    print(ll)
    ll.remove(-1)
    print(ll)
    ll.remove(6)
    print(ll)
    ll.remove(2)
    print(ll)
    ll.remove(3)
    print(ll)
    ll.insert(30,2)
    print(ll)