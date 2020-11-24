# Project 2 - Explanations

**Task 1**
___
The LRU_Cache is implemented in a way that is using base python only without the help of any library (like ordereddict from collections and so on). LRU_Cache comprises nodes assembled in a linked list. Building the linked list is fast, as we keep track of the tail and inserting a new node is directly done at the end (Time complexity O(1)). However in only a linked list a lookup would be worst case O(n). Therefore every node with its matching key as a hash i inserted in a dictionary: Lookup operations therefore occur also in O(1) time. 
Rearranging the elements when our cache limit is reached is also fast, as we always remove the tail node (O(1)). Sorting the linked list (aka swapping two nodes) also occurs in O(1) time.
The space complexity is dependant only on the input, in the worst case this is the maximum capacity (O(n)).

**Task 2**
___
In this task, we recursively check folders for certain files. A folder can have n subfolders (depth), and every (sub)folder can have x folders (width). The overall time complexity is therefore depending on the number of recursions we have to make (O(n * x)).
Space complexity is relying on the number of files a that we finally store in our output, there space complexity is linear (O(a)).

**Task 3**
___
The main time consuming operation in this task is to build the huffman tree based on a heap data structure. Inserting new nodes is dependant on the length of the input word (n). Sorting the huffman tree (heapsort) takes O(n * log(n)) time. After removing one element, we need to heapsort downstream (also O(n * log(n))). For the final encoding step, we need to traverse the tree for each letter (n), which is faster than the current total O(n * log(n)) which is to be considered as the total time complexity.
Space complexity: O(x), where x is the number of characters used.

**Task 4**
___
Similar to task 2, we have to recurse through a depth of n groups, containing x users. Therefore our potential time complexity might be O(n * x). As we only return True or False depending wheter a user is in a group, the space complexity is O(1).

**Task 5**
___
The BlockChain is basically an advanced linked list. Instead of .next attributes however its organized in reverse, containing previous hashes to the block before. Searching the first block in a blockchain of 100 blocks, is directly linear to the number of blocks (100). Therefore the time complexity for the search operation = O(n). Inserting a new single block is fast as we keep track of the tail (O(1)). The to_list method iterates through all blocks, therefore like the search function requires O(n) time. The chain_size attribute is O(1) as while inserting new blocks we add up the num_blocks attribute, therefore its always up to date.
Space complexity: Depends on the number of blocks n -> (O(n)).

**Task 6**
___
Union:
We here iterate through two linked lists O(2 * n), simplified to O(n), then iterate another time through our set. In the best case the values in both linked lists were equal so 2n would be half the size as before (n). Worst case they are different and our set has twice the size. However, this is linear so we do not consider this. Next we iterate all values back to a new linked list (O(n)). Globally time complexity is O(n). Space complexity: O(n). 

Intersection:
Here we build two different sets first to get unique values from each linked list, then find values that are in both of them. Time complexity overall again is O(n) as in the worst case we need to iterate through each value. Space complexity (simplified) is also O(n).


```python

```
