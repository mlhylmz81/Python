import unittest
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node
    def uygulaSonraki(self, next_node = None):
        self.next = next_node
def IsItLoop(head):
    if head == None:
        return False
    x = y = head
    while(x or y or y.next):
        if y.next == None:
            return False
        if x == y.next or x == y.next.next:
            return True
        x = x.next
        y = y.next.next
    return False
class TestMethods(unittest.TestCase):
    def test_loop_empty(self):
        self.assertEqual(IsItLoop(None), False)

    def test_loop(self):
        self.assertEqual(IsItLoop(n5), True)

    def test_no_loop(self):
        self.assertEqual(IsItLoop(m5), False)

n1 = Node(1, None)
n2 = Node(2, n1)
n3 = Node(3, n2)
n4 = Node(4, n3)
n5 = Node(5, n4)
n6 = Node(6, n5)
n7 = Node(7, n6)
n8 = Node(8, n7)
n9 = Node(9, n8)
n10 = Node(10, n9)
n11 = Node(11, n10)
n12 = Node(12, n11)
n2.uygulaSonraki(n11) # dongu
m1 = Node(1, None)
m2 = Node(2, m1)
m3 = Node(3, m2)
m4 = Node(4, m3)
m5 = Node(5, m4)
unittest.main()
