import heapq  # used to build the priority queue (min-heap)
from collections import defaultdict, Counter

# Node class for the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char            # character (None for internal nodes)
        self.freq = freq            # frequency of the character
        self.left = None            # left child
        self.right = None           # right child

    # Define comparator for heapq (it needs to compare Nodes)
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(text):
    # Count frequency of each character using Counter
    frequency = Counter(text)

    # Create a priority queue (min-heap) of nodes
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Combine nodes until one tree remains
    while len(heap) > 1:
        node1 = heapq.heappop(heap)  # smallest freq
        node2 = heapq.heappop(heap)  # second smallest freq

        # Create new parent node with combined freq
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        # Add merged node back to heap
        heapq.heappush(heap, merged)

    # Root of the final tree
    return heap[0]

# Function to build the code table from the tree
def build_codes(node, prefix="", code_table=None):
    if code_table is None:
        code_table = dict()

    if node:
        # If it's a leaf node, assign the code
        if node.char is not None:
            code_table[node.char] = prefix
        # Recursively build codes for left and right children
        build_codes(node.left, prefix + "0", code_table)
        build_codes(node.right, prefix + "1", code_table)

    return code_table

# Encode the text using the code table
def encode(text, code_table):
    return ''.join(code_table[char] for char in text)

# Decode binary string back to text using the tree
def decode(encoded_text, root):
    decoded = ""
    current = root

    for bit in encoded_text:
        # Go left on '0', right on '1'
        current = current.left if bit == '0' else current.right

        # If we hit a leaf node, record the character
        if current.char is not None:
            decoded += current.char
            current = root  # reset to root for next char

    return decoded

# --- MAIN DRIVER EXAMPLE ---
if __name__ == "__main__":
    text = "abbcccddddeeeee"
    root = build_huffman_tree(text)
    code_table = build_codes(root)

    print("Character codes:")
    for char, code in code_table.items():
        print(f"{repr(char)}: {code}")

    encoded = encode(text, code_table)
    print("\nEncoded:", encoded)

    decoded = decode(encoded, root)
    print("Decoded:", decoded)
