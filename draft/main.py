class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

    # def __repr__(self):
    #     rep = f"The value: <{self.value}>"
    #     return rep


class SLL(object):
    def __init__(self):
        self.head = Node

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def list_print(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.value)
            print_val = print_val.next


li = SLL()
li.push(1)
li.push(2)
li.push(3)
li.list_print()
