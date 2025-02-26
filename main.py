class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Add a Node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to head to make it circular
        else:
            last_node = self.head
            while last_node.next != self.head:  # Traverse till we reach the node pointing to the head
                last_node = last_node.next
            last_node.next = new_node
            new_node.next = self.head  # Point new node to head to maintain the circular property

    # Add a Node at the beginning of the list
    def preappend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to head to make it circular
        else:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            new_node.next = self.head
            last_node.next = new_node
            self.head = new_node  # Update head to new node

    # Traversal with step-by-step display
    def traverse_and_display(self):
        if not self.head:
            print("The list is empty.")
            return

        current_node = self.head
        position = 1
        print("Traversing the circular linked list:")
        while True:
            print(f"Step {position}: Current Node = {current_node.data}")
            current_node = current_node.next
            position += 1
            if current_node == self.head:  # Stop when we reach the head again
                break
        print("Traversal complete.")

    # Display the Circular Linked List (wrap around to head)
    def show(self):
        if not self.head:
            print("The list is empty.")
            return

        current_node = self.head
        print("Circular Linked List:")
        while True:
            print(current_node.data, end=" -> " if current_node.next != self.head else " -> Head")
            current_node = current_node.next
            if current_node == self.head:  # Stop when we reach the head again
                break
        print()

# Create a circular linked list and perform operations
circular_list = CircularLinkedList()

# Add nodes at the end
circular_list.append("A")
circular_list.append("B")
circular_list.append("C")
circular_list.append("D")

# Add node at the beginning
circular_list.preappend("Z")

# Display the list
circular_list.show()

# Traverse with step-by-step display
circular_list.traverse_and_display()
