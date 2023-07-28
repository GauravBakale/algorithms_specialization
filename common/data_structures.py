class Queue():

    """
        Queue
    """

    def __init__(self,type='FIFO'):
        self.type=type
        self.queue = []
        self.len = len(self.queue)

    def push(self,item):
        self.queue.append(item)
        self.len = len(self.queue)

    def pop(self):
        if self.type == 'FIFO':
            if len(self.queue):
                item = self.queue.pop(0)
                self.len = len(self.queue)
        if self.type == 'LIFO':
            if len(self.queue):
                item = self.queue.pop()
                self.len = len(self.queue)
        return item

    def get(self):
        return self.queue[:]
    
    def __len__(self) -> int:
        return len(self.queue)

    def __iter__(self):
        return iter(self.queue)
    
    def __repr__(self):
        return str(self.queue)

    def __str__(self):
        return str(self.queue)
    
