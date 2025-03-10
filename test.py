'''
Test of reverse method for LL.
'''


from linked_list import Node, LinkedList


node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')

ll = LinkedList()
print(ll)

# Add nodes to LL
ll.insert_at_end(node_a)
ll.insert_at_end(node_b)
ll.insert_at_end(node_c)
ll.insert_at_end(node_d)
print(ll)

# Test reverse() method
ll.reverse()
print(ll)
