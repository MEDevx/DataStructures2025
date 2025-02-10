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

  def search(self, key):
    current = self.head
    index = 0
    while current:
      if current.data == key:
        return index
      current = current.next
      index += 1
    return -1

  def update(self, old_value, new_value):
    current = self.head
    while current:
      if current.data == old_value:
        current.data = new_value
        return
      current = current.next

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

colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
for color in colors:
    llist.insert(color)
print("\nLinked List after inserting colors:")
llist.traverse()

llist.delete("Green")  # Removing one element
print("Linked List after deleting 'Green':")
llist.traverse()

index = llist.search("Yellow")
print(f"Index of 'Yellow': {index}")

llist.update("Purple", "Orange")
print("Linked List after updating 'Purple' to 'Orange':")
llist.traverse()

print(f"Number of elements in the linked list: {llist.count()}\n" )
