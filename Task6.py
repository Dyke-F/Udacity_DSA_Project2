class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string
    
    
    def append(self, value):
        
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
    
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        
        return size

def union(llist_1, llist_2):
    """ Returns union of nodes of llist1 and llist2.
        Initialize an empty set of nodes. Traverse both lists and add the nodes value
        attribute to the set. Finally instantiate a new linkedlist and append new nodes
        with the union_values values.
        """
    
    union_values = set()
    
    curr_node1 = llist_1.head
    while curr_node1:
        union_values.add(curr_node1.value)
        curr_node1 = curr_node1.next
    
    curr_node2 = llist_2.head
    while curr_node2:
        union_values.add(curr_node2.value)
        curr_node2 = curr_node2.next
    
    union_llist = LinkedList()
    for val in union_values:
        union_llist.append(val)
    return union_llist


def intersection(llist_1, llist_2):
    """ Returns interserction of nodes of llist1 and llist2.
        Initialize an empty set of nodes for each llist seperately.
        Traverse both lists and add the nodes value to their respective set.
        Iterate over one of the sets and if the value is in the second set
        as well, add this value to the intersection_set. Finally instantiate
        a new linkedlist and append new nodes with the union_values values.
        """
    
    llist1_set = set()
    llist2_set = set()
    
    curr_node1 = llist_1.head
    while curr_node1:
        llist1_set.add(curr_node1.value)
        curr_node1 = curr_node1.next
    
    curr_node2 = llist_2.head
    while curr_node2:
        llist2_set.add(curr_node2.value)
        curr_node2 = curr_node2.next
    
    intersection_set = set()
    for value in llist1_set:
        if value in llist2_set:
            intersection_set.add(value)
    return intersection_set



# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

print("============================")


### Own test cases
# 1
ll1 = LinkedList()
ll2 = LinkedList()

elem1 = []
elem2 = [1,2,3,4,5]
for _ in elem1:
    ll1.append(_)
for _ in elem2:
    ll2.append(_)

print(union(ll1, ll2), "should be: 1 -> 2 -> 3 -> 4 -> 5 ->")
print(intersection(ll1, ll2), "should be no overlap")
print("============================")

# 2
ll1 = LinkedList()
ll2 = LinkedList()

elem1 = []
elem2 = []
for _ in elem1:
    ll1.append(_)
for _ in elem2:
    ll2.append(_)

print(union(ll1, ll2), "should be empty")
print(intersection(ll1, ll2), "should be empty")
print("============================")

# 3
ll1 = LinkedList()
ll2 = LinkedList()

elem1 = [1,2,3]
elem2 = [4,5,6,2,2]
for _ in elem1:
    ll1.append(_)
for _ in elem2:
    ll2.append(_)

print(union(ll1, ll2), "should be: 1 -> 2 -> 3 -> 4 -> 5 -> 6 ->")
#1 -> 2 -> 3 -> 4 -> 5 -> 6 ->
print(intersection(ll1, ll2), "should be 2")
#2
