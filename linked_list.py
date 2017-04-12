class Node:
    def __init__(self, value, previous_node, next_node):
        self.value = value
        self.preious_node = previous_node
        self.next_node = next_node

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def queue(new_node):
        #add to the tail end of the linked list

        if self.head_node == None and self.tail_node == None:
            self.head_node = new_node;
            self.tail_node = new_node;
        else:
            old_tail = self.tail_node
            self.tail_node = new_node
            new_node.previous_node = old_tail
            old_tail.next_node = new_node
    def dequeue():
        #remove from the head end of the linked list
        temp = self.head
        self.head = temp.next_node
        # new head is  tem node. store value of current node
        return temp.value


ll = QueueLinkedList()
