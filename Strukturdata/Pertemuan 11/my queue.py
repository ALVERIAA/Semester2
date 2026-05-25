#membuat queue dengan linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#membuat class queue dengan linked list
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
#membuat method enqueue untuk menambahkan data ke dalam queue
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
#membuat method dequeue untuk menghapus data dari dalam queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return data
#membuat method peek untuk melihat data terdepan dalam queue
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.front.data
#membuat method is_empty untuk mengecek apakah queue kosong atau tidak
    def is_empty(self):
        return self.size == 0
#membuat method display untuk menampilkan isi queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()


antrian = Queue()
antrian.enqueue("joni")
antrian.enqueue("budi")
antrian.enqueue("siti")
antrian.display()
antrian.peek()
antrian.dequeue()