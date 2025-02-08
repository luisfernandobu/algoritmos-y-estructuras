from Node import Node

""" 
    Singly linked lists operations 
"""
""" Traversal """
# Traverse the linked list from head to end
def traverse_list(head):
    while head is not None:
        if head.next:
            print(head.data, end=" -> ")
        else:
            print(head.data)
        head = head.next
    print()

""" Insertion """
# Insert at the front of the linked list
def insert_at_front(head, new_data):
    new_node = Node(new_data)
    new_node.next = head

    return new_node

# Insert at the end of the linked list
def insert_at_end(head, new_data):
    new_node = Node(new_data)
    
    # Special case for empty list
    if head is None:
        return new_node
    
    current = head
    while current.next:        
        current = current.next
    
    current.next = new_node
    
    return head

# Insert after a given node
def insert_after(head, key_node, new_data):
    new_node = Node(new_data)
    current = head
    
    while current:  
        if current.data == key_node.data:
            new_node.next = current.next
            current.next = new_node
            break
        
        current = current.next
        
    return head

# Insert before a given node
def insert_before(head, key_node, new_data):
    new_node = Node(new_data)
    current = head
    prev = None
    
    while current:  
        if current.data == key_node.data:
            new_node.next = current
            
            # Case if the given node is head
            if prev is None:
                return new_node
            
            prev.next = new_node
            break
        
        prev = current
        current = current.next
        
    return head

# Insert at specific position  
def insert_at_position(head, position, new_data):
    new_node = Node(new_data)
    current = head
    counter = 1
    
    # Case for position = 1 (insert at the beginning)
    if position == 1:
        new_node.next = current
        return new_node
    
    while current and counter <= position:        
        if counter == position - 1:
            new_node.next = current.next
            current.next = new_node
            break
        
        current = current.next
        counter += 1
        
    return head

""" Deletion """
# Delete head node (first node)
def delete_head(head):
    if head:
        head = head.next
    
    return head

# Delete the last node
def delete_at_end(head):
    last = head
    prev = None
    
    while last.next:
        prev = last
        last = last.next

    prev.next = None
    
    return head

# Delete node at specific position
def delete_node(head, position):
    curr = head
    prev = None
    counter = 1
    
    # Case for position = 1 (delete head)
    if position == 1:
        return curr.next
    
    while curr and counter <= position:        
        if counter == position:
            prev.next = curr.next
            break
        
        prev = curr
        curr = curr.next
        counter += 1
        
    return head
    
""" Search """
# Search a specific value in the linked list, return True if found or False if not found
def search_key(head, key):
    curr = head
    
    while curr:
        if curr.data == key:
            return True
        curr = curr.next
    
    return False

""" Get length """
# Get the length of the linked list
def get_length(head):
    curr = head
    counter = 0
    
    while curr:
        counter += 1
        curr = curr.next
        
    return counter

""" Tests """
def main():
    # Initialize nodes and assign data
    node_a = Node(2)
    node_b = Node(3)
    node_c = Node(4)

    # Connect nodes
    node_a.next = node_b
    node_b.next = node_c

    # Save address of first node in head
    head = node_a
    
    # Traverse
    print("Linked list:")
    traverse_list(head) # 2 -> 3 -> 4
    
    # Insert at front
    print("Insert at front:")
    head = insert_at_front(head, 0)
    traverse_list(head) # 0 -> 2 -> 3 -> 4
    
    # Insert at the end
    print("Insert at the end:")
    head = insert_at_end(head, 6)
    traverse_list(head) # 0 -> 2 -> 3 -> 4 -> 6
    
    # Insert after a given node
    print("Insert after a given node:")
    head = insert_after(head, node_c, 5)
    traverse_list(head) # 0 -> 2 -> 3 -> 4 -> 5 -> 6
    
    # Insert before a given node
    print("Insert before a given node:")
    head = insert_before(head, node_a, 1)
    traverse_list(head) # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
    
    # Insert at specific position
    print("Insert at specific position:")
    head = insert_at_position(head, 4, 10)
    traverse_list(head) # 0 -> 1 -> 2 -> 10 -> 3 -> 4 -> 5 -> 6
    
    # Delete head
    print("Delete head:")
    head = delete_head(head)
    traverse_list(head) # 1 -> 2 -> 10 -> 3 -> 4 -> 5 -> 6
    
    # Delete at the end
    print("Delete at the end:")
    head = delete_at_end(head)
    traverse_list(head) # 1 -> 2 -> 10 -> 3 -> 4 -> 5
    
    # Delete node at specific position
    print("Delete node at specific position:")
    head = delete_node(head, 3)
    traverse_list(head) # 1 -> 2 -> 3 -> 4 -> 5
    
    # Search a specific value in list
    print("Search value in list:")
    print(search_key(head, 10))
    print()
    
    # Get Linkedlist length
    print("Get length:")
    print(get_length(head))
    
if __name__ == "__main__":
    main()
    