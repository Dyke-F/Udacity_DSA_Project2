import sys

class HuffmanNode(object):
    
    """ Node object
        PARAMETERS:
        ==========
            identity = unique letter of input string to HuffmanHeap
            frequency = count of each unique letter in input string
            code = int(0,1); == 0 if after building the tree the Node 
                             becomes a left child, else == 1 if right child
            left / right = when comparing two nodes, 
                         the smaller node becomes left else right
    """
    
    def __init__(self, identity, 
                 frequency, 
                 left = None,
                 right = None, code = None):
        
        self.identity = identity     
        self.frequency = frequency
        self.code = code
        self.left = left
        self.right = right


class HuffmanHeap(object):
    """ Encoding an input string of characters into a unique 0-1 bit sequence.
        HuffmanHeap is a MinHeap starting out with unique nodes as inputs to each index,
        that are later resorted to a full tree.
        PARAMETERS:
        ==========
            self.tree = initial Array / Dynamic Python List, holding unique
                        HuffmanNodes for each unique character.
            self.next_idx = parameter for insertion
            self.count_dict = initialize the HuffmanNode objects with their
                              respective frequency
    """
    
    def __init__(self, init_size = 100):
        self.tree = [None for _ in range(init_size)]
        self.next_idx = 0
        self.count_dict = {}
    
    def count_freq(self, data):
        """ Count frequency of each unique character in the given data """
        for char in data:
            self.count_dict[char] = self.count_dict.get(char, 0) + 1
        
    def init_insert(self):
        """ Initialize the heap tree """
        
        for identity, frequency in self.count_dict.items():
            self.tree[self.next_idx] = HuffmanNode(identity, frequency, code=0)
            self._upstream_heapify()   # sort as a MinHeap
            self.next_idx += 1
            # if initial array size too small, increase dimensions
            if self.next_idx >= len(self.tree):
                temp = self.tree
                self.tree = [None for _ in range(len(temp)*2)]
                for idx, item in enumerate(temp):
                    self.tree[idx] = item
                    
    def insert(self, node):
        """ When creating the tree, reinsert the current 
        new node with its appended left / right children 
        back to the heap and heapsort again"""
        self.tree[self.next_idx] = node
        self._upstream_heapify()
        self.next_idx += 1
                    
    def _upstream_heapify(self):
        """ Adopted from Udacitys Data Structures and Algorithms Course """
        child_index = self.next_idx
        while child_index >= 1:
            parent_index = (child_index -1) // 2
            parent_element = self.tree[parent_index]
            child_element = self.tree[child_index]
            if child_element.frequency < parent_element.frequency:
                self.tree[parent_index] = child_element
                self.tree[child_index] = parent_element
                child_index = parent_index
            else:
                break
                
    def heap_sort(self):
        """ After initialising a unique node for each unique character and
            pushing them into self.tree, start sorting:
                Algorithm: 1. Obtain the lowest frequency node.
                           2. Resort the tree and repeat step 1 and 2.
                           3. Create a new node, fusing the 2 nodes obtained above.
                           4. Reinsert the new node into the heap.
                           5. Repeat 1.-4. until all nodes are connected in a MinHeap Tree.
        """
        

        
        def get_lowest():
            lowest_freq = self.tree[0]
            self.next_idx -= 1
            last_item = self.tree[self.next_idx]
            self.tree[0] = last_item
            self.tree[self.next_idx] = None
            self._downstream_heapify()
            return lowest_freq
        
        while self.next_idx >= 2:
            # if self.next_idx is at least two, we guarantee when 
            # calling get_lowest we obtain last_item: idx=1 for the 
            # first call and idx = 0 for the last item in the second call below
            one = get_lowest()
            one.code = 0

            two = get_lowest()
            two.code = 1

            params = None, one.frequency+two.frequency, one, two
            new_node = HuffmanNode(*params)
            self.insert(new_node)
            
            
    def left_child(self, idx):
        """ Helper function for down-heapifying, returns left childs index and node
            if the left child exists 
        """
        child_idx = 2 * idx + 1
        if child_idx < self.next_idx:
            return (child_idx, self.tree[child_idx])
        else:
            return (child_idx, None)
    
    def right_child(self, idx):
        """ Helper function for down-heapifying, returns right childs index and node
            if the right child exists 
        """
        child_idx = 2 * idx + 2
        if child_idx < self.next_idx:
            return (child_idx, self.tree[child_idx])
        else:
            return (child_idx, None)
        
            
    def switch(self, idx1, idx2):
        """ Change nodes in the heap-tree with respect to indices """
        self.tree[idx1], self.tree[idx2] = self.tree[idx2], self.tree[idx1]
             
                
    def _downstream_heapify(self, parent_idx = 0):
        """ Pass a node from root down to its matching index """
        node = self.tree[parent_idx] # root
        if parent_idx < self.next_idx: # assert node index is not out of range
            left_idx, left = self.left_child(parent_idx) # get left child
            right_idx, right = self.right_child(parent_idx) # get right child
            min_element = node.frequency
            if left != None: # compare parent to left child if left child exists
                min_element = min(min_element, left.frequency)
            if right != None: # compare parent to right child if left right exists
                min_element = min(min_element, right.frequency)
            if min_element == node.frequency:
                return # don't change anything if parent is the min-node
            elif min_element == left.frequency:
                self.switch(parent_idx, left_idx)   # change parent and left node
                self._downstream_heapify(left_idx)  # recursively call down-heap on left node
            elif min_element == right.frequency:   
                self.switch(parent_idx, right_idx)  # change parent and right node
                self._downstream_heapify(right_idx) # recursively call down-heap on right node
    
def huffman_encoding(data):
    """ Encode a text message into binary 0-1 bit integer sequences. """
    assert data != "", "Please provide a non-empty string"
    tree = HuffmanHeap()    # initialize the HuffmanHeap
    tree.count_freq(data)   # count frequency and create nodes

    tree.init_insert()      # initialise a sorted heap with nodes
    tree.heap_sort()        # build the real tree
    
    # get binary code
    root = tree.tree[0]     # start at the root
    encoding_dict = {}      # dict object holding code for unique chars
    temp = ""
    
    def traverse_rec(node, temp):
        """ Traverse the tree in DFS (depth first search)"""

        if node:
            if node.code is not None:     # root node will not hold code
                temp += str(node.code)
            if node.identity is not None: # fusion nodes are not unique chars
                encoding_dict[node.identity] = temp # map char -> 0/1 code
            traverse_rec(node.left, temp)  # go all left children
            traverse_rec(node.right, temp) # go all rright children
        return encoding_dict
    
    encoding_dict = traverse_rec(root, temp)
        
    # encode the data
    encoded_data = ""
    for char in data:
        if char in encoding_dict.keys():
            encoded_data += encoding_dict[char]
    
    return encoded_data, tree, encoding_dict



def huffman_decoding(data, tree, encoding_dict):
    """ Decode a given 0/1 binary bit string to its origin """
    
    # One way of doing this would be by traversing the tree,
    # however for each substring (the length of which is initially unknown
    # until we hit a leaf node) we restart from the root.
    
    # Here, we use a decoding_dict and check wheter a substring is in its keys,
    # else we increase the substring by the next character
    
    decoded = ""
    decoding_dict = {vals: keys for keys, vals in encoding_dict.items()}
    
    iterator = (value for value in data)
    idx = 0
    while idx < len(data):

        subcode = ""     # binary strings for chars are in varying length,
                         # so increase subcode length until we find it in 
                         # the decoding_dict.keys(), then return its character
                
        while subcode not in decoding_dict and idx < len(data):
            subcode += next(iterator)
            idx += 1
        decoded += decoding_dict[subcode]
        
    return decoded



### Own tests ###

print("Test case 1 ----------")
sentence = "Udacity is great for python learning"
print("Standard size:", sys.getsizeof(sentence))
encoded, tree, _ = huffman_encoding(sentence)
print("Encoded size:", sys.getsizeof(int(encoded, base=2))) # use base=2 because its binary only
print("Bit sequence", encoded)
decoded = huffman_decoding(encoded, tree, _)
print("Decoded:", decoded)
print("----------------------")

#Test case 1 ----------
#Standard size: 85
#Encoded size: 44
#Bit sequence 011001001011111001111011110001010111010101110101000001000111111101010111000110001010111100101110010100011110010101101100011110001100110111000100
#Decoded: Udacity is great for python learning
#----------------------


print("Test case 2 ----------")
sentence = "Sebastian Thrun likes self-driving cars"
print("Standard size:", sys.getsizeof(sentence))
encoded, tree, _ = huffman_encoding(sentence)
print("Encoded size:", sys.getsizeof(int(encoded, base=2))) # use base=2 because its binary only
print("Bit sequence", encoded)
decoded = huffman_decoding(encoded, tree, _)
print("Decoded:", decoded)
print("----------------------")

#Test case 2 ----------
#Standard size: 88
#Encoded size: 48
#Bit sequence 0011011001111111010000110110010101010110110010010001111011011110110111111001011010110000001100011001111000101100101001111100101000001010111111100110011110101110000
#Decoded: Sebastian Thrun likes self-driving cars
#----------------------


# Edge cases

# In this tree, only one node will be inserted holding the value a. The length of the string doesnt matter (see below).
# In this special case, by default the nodes code is set to 0 to provide minimu memory usage, although the node is per definition 
# not the left child of a parent ...

print("Test case 3 ----------")
sentence = "aa"
print("Standard size:", sys.getsizeof(sentence))
encoded, tree, _ = huffman_encoding(sentence)
print("Encoded size:", sys.getsizeof(int(encoded, base=2))) # use base=2 because its binary only
print("Bit sequence", encoded)
decoded = huffman_decoding(encoded, tree, _)
print("Decoded:", decoded)
print("----------------------")

#Test case 3 ----------
#Standard size: 51
#Encoded size: 24
#Bit sequence 00
#Decoded: aa
#----------------------


print("Test case 4 ----------")
sentence = "aaaaaaaaaaaaaaaaaaaaaaaaaaa"
print("Standard size:", sys.getsizeof(sentence))
encoded, tree, _ = huffman_encoding(sentence)
print("Encoded size:", sys.getsizeof(int(encoded, base=2))) # use base=2 because its binary only
print("Bit sequence", encoded)
decoded = huffman_decoding(encoded, tree, _)
print("Decoded:", decoded)
print("----------------------")

#Test case 4 ----------
#Standard size: 76
#Encoded size: 24
#Bit sequence 000000000000000000000000000
#Decoded: aaaaaaaaaaaaaaaaaaaaaaaaaaa


# Returns assertion error, as string is empty
print("Test case 5 ----------")
sentence = ""
print("Standard size:", sys.getsizeof(sentence))
encoded, tree, _ = huffman_encoding(sentence)
print("Encoded size:", sys.getsizeof(int(encoded, base=2))) # use base=2 because its binary only
print("Bit sequence", encoded)
print("----------------------")

#Test case 5 ----------
#Standard size: 49
#---------------------------------------------------------------------------
#AssertionError                            Traceback (most recent call last)
#<ipython-input-77-ab1a5ecc6de6> in <module>
#    305 sentence = ""
#    306 print("Standard size:", sys.getsizeof(sentence))
#--> 307 encoded, tree, _ = huffman_encoding(sentence)
#    308 print("Encoded size:", sys.getsizeof(int(encoded, base=2))) # use base=2 because its binary only
#    309 print("Bit sequence", encoded)
#
#<ipython-input-77-ab1a5ecc6de6> in huffman_encoding(data)
#    171 def huffman_encoding(data):
#    172     """ Encode a text message into binary 0-1 bit integer sequences. """
#--> 173     assert data != "", "Please provide a non-empty string"
#    174     tree = HuffmanHeap()    # initialize the HuffmanHeap
#    175     tree.count_freq(data)   # count frequency and create nodes
#
#AssertionError: Please provide a non-empty string
