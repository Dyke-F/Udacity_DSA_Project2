class CacheNode(object):
    """ Node object, PARAMETERS:
        ========================
        [value = data to be held in the Node (here a number),
        (next, previous) = connections in a priority queue,
        key = hash value to store node object inside a lookup dict]
        
        """
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        self.key = None


class LRU_Cache(object):
    """ Least Recently Used Memory Cache with limited size.
        Uses a mapping (dict) for fast (O(1)) lookups by storing objects of type -> CacheNode
        and a queue to sort priority of objects. Least recently used data (not previously set or looked-up)
        will be removed to free space for new items.
        PARAMETERS:
        ==========
        self.capacity = size limit (int)
        self.cache = mapping for instant .get() method
        self.start / self.end = beginning and ending of least recently used items in a queue
        [Node items will be appended to self.end, while beeing removed from self.start]
        """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.start = None; self.end = None
    
    def get(self, key):
        """ Returns the value of a node mapped to key. If key does not exist, returns -1.
            Also resorting queue items, so that most recently looked up node is set to the end of the queue.
            """
        
        if key in self.cache:
            curr_node = self.cache[key]
            if curr_node == self.start:
                self.start = self.start.next
            curr_node_prev = curr_node.previous
            curr_node_next = curr_node.next
            if curr_node_prev is not None:
                curr_node_prev.next = curr_node_next
            if curr_node_next is not None:
                curr_node_next.previous = curr_node_prev
            curr_node.next = None
            curr_node.previous = None
            self.end.next = curr_node
            self.end.next.previous = self.end
            self.end = self.end.next
            return self.cache[key].value
    
    else:
        return -1

    def set(self, key, value):
        """ Inserts data (value) in a CacheNode object to the mapping and to the end of the queue.
            If mapping size limit is reached, removes the object at the start of the queue
            (least recently used) from both the queue and the mapping (dict).
            """
        
        if len(self.cache) >= self.capacity:
            del_node = self.start
            self.start = self.start.next
            del self.cache[del_node.key]
        new_node = CacheNode(value)
        new_node.key = key
        if self.start is None:
            self.start = new_node
            self.end = self.start
        else:
            self.end.next = new_node
            self.end.next.previous = self.end
            self.end = self.end.next
        self.cache[key] = new_node



### Official test cases


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1), "---> should return 1")       # returns 1
print(our_cache.get(2), "---> should return 2")       # returns 2
print(our_cache.get(9), "---> should return -1")      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3), "---> should return -1")      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("=========================")

### Own test cases ###

mycache = LRU_Cache(3)
print(mycache.get(1), "---> should return -1")
# -1

mycache.set(1,1)
mycache.set(1,3)
mycache.set(2,4)
print(mycache.get(1), "---> should return 3")
# 3

mycache = LRU_Cache(3)
mycache.set(1,1)
print(mycache.get(1), "---> should return 1")
# 1
# cache should be empty now:
node = mycache.start
print(node, "---> should return None")
# None
