class TrieNode:
    def __init__(self, char=None, is_terminal=False):
        self.char = char
        self.children = {}
        self.is_terminal = is_terminal

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            current = current.children.setdefault(char, TrieNode(char))
        current.is_terminal = True

    def __contains__(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_terminal

    def get_prefixes(self, word):
        prefix, prefixes, current = '', [], self.root
        for char in word:
            if char not in current.children:
                return prefixes
            current = current.children[char]
            prefix += char
            if current.is_terminal:
                prefixes.append(prefix)
        return prefixes
