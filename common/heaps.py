from math import log2,ceil

class Heap():
    """
    Heap
        Heaps can be understood as binary trees with certain properties.
            Property 1: The key at any node must be lesser than or equal to the keys of its children nodes.

        - This implementation gives us access to the min value in O(1) since the root node always has the min key.
        - The insert and delete operations can be implemented by "bubbling-up" or "bubbling-down" which can be done in O(log n) 
          time. Since there will be log n layers in the tree.
        - Even though they are understood as graphs they can be implemented using arrays.
            if we consider index x, then the children of x can be found ad 2x,2x+1.
                                         the parent of x can be found at x/2[even], ceil(x/2)[odd]

    """

    def __init__(self):        
        self.heap = []

    def bubble_down(self, index):
        
        # initially set it to dummy value
        smaller_child_index = -1

        # while there is a child node in the heap
        while smaller_child_index < self.len:
            
            # calculate the index of the childrent of current node
            child_2_index = 2*(index+1)
            child_1_index = child_2_index-1

            # swap the 
            if child_2_index < self.len:
                if self.heap[child_1_index] < self.heap[child_2_index]:
                    smaller_child_index = child_1_index
                else:
                    smaller_child_index = child_2_index

            elif child_1_index < self.len:
                smaller_child_index = child_1_index           
            
            else:
                break
            
            self.heap[index],self.heap[smaller_child_index] = self.heap[smaller_child_index], self.heap[index]
            index = smaller_child_index
        return True

    def insert(self, item):
        # Insert the item in the heap and ensure the heap property is intact/restored using bubbling up
        index = len(self.heap)
        self.heap.append(item)

        # check for heap property
        if index != 0:
            
            # bubble-up
            parent_index = None
            while parent_index != 0:
                parent_index = (index-1)//2
                if self.heap[parent_index] > self.heap[index]:
                    self.heap[parent_index],self.heap[index] = self.heap[index],self.heap[parent_index]
                    index = parent_index
                else:
                    break

        return True

    def delete(self, index):
        val = self.heap[index]

        # move the last value to the root node
        self.heap[index]= self.heap.pop()

        # bubble-down such that the heap property is restored
        self.bubble_down(index = index)
        return val

    def display(self):

        levels = ceil(log2(len(self.heap)+1))

        total_distance = pow(3,levels)
        for level in range(levels):
            ind = pow(2,level)-1
            no_of_items = pow(2,level)

            distance = total_distance//no_of_items
            for i in self.heap[ind:ind+no_of_items]:
                print(str(i).rjust(distance//9, ' ').ljust(distance//4, ' '),end="")
            print(" ",end="\n\n")

    def assert_heap_property(self):
        levels = ceil(log2(len(self.heap)+1))

        for level in range(levels):
            parent_index = pow(2,level)-1
            child_2_index = 2*(parent_index+1)
            child_1_index = child_2_index-1

            if child_2_index < len(self.heap):
                if self.heap[child_2_index] < self.heap[parent_index]:
                    raise AssertionError("The heap property is violated.")
            if child_1_index < len(self.heap):
                if self.heap[child_1_index] < self.heap[parent_index]:
                    raise AssertionError("The heap property is violated.")
        print("Maintains heap property")

    def extract_min(self):
        
        # note the minimum value
        min_val = self.heap[0]

        # move the last value to the root node
        self.heap[0]= self.heap.pop()
        self.len = len(self.heap)

        # bubble-down such that the heap property is restored
        self.bubble_down(index = 0)
        
        return min_val

    def __str__(self):
        self.display()
        return str(self.heap)
    
    def __repr__(self):
        return str(self.heap)
