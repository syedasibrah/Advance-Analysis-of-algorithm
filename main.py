
from collections import Counter


class Node:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    freqs = Counter(text)
    nodes = [Node(freq, char) for char, freq in freqs.items()]
    while len(nodes) > 1:
        node1, node2 = sorted(nodes)[:2]
        parent = Node(node1.freq + node2.freq)
        parent.left, parent.right = node1, node2
        nodes = [node for node in nodes if node not in (node1, node2)]
        nodes.append(parent)
    return nodes[0]


def traverse_tree(node, code='', codes={}):
    if node.char:
        codes[node.char] = code
    else:
        traverse_tree(node.left, code + '0', codes)
        traverse_tree(node.right, code + '1', codes)
    return codes


def huffman_compress(text):
    root = build_huffman_tree(text)
    codes = traverse_tree(root)
    compressed = ''.join(codes[char] for char in text)
    return compressed, codes


def huffman_decompress(compressed, codes):
    reversed_codes = {code: char for char, code in codes.items()}
    decompressed = ''
    code = ''
    for bit in compressed:
        code += bit
        if code in reversed_codes:
            decompressed += reversed_codes[code]
            code = ''
    return decompressed


text = input("Enter Text you want to encode: ")
compressed, codes = huffman_compress(text)
print(compressed)

decision = input("Do you want to decode the above string ? YES or NO ?")

if decision == "YES":
    decompressed = huffman_decompress(compressed, codes)
    print(decompressed)
else:
    pass

