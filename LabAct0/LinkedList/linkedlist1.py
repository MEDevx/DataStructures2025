class Node:
  def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node

  def delete(self, key):
    temp = self.head
    if temp and temp.data == key:
      self.head = temp.next
      temp = None
      return
    prev = None
    while temp and temp.data != key:
      prev = temp
      temp = temp.next
    if temp is None:
      return
    prev.next = temp.next
    temp = None

  def count(self):
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count

  def traverse(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

llist = LinkedList()

for i in range(1, 6):
    llist.insert(i * 3)
print("\nLinked List after inserting first 5 multiples of 3:")
llist.traverse()

llist.delete(9)
print("Linked List after deleting 9:")
llist.traverse()

print(f"Number of elements in the linked list: {llist.count()}\n")
