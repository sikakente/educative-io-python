class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populate_suffix_trie_from(string)

    def populate_suffix_trie_from(self, string):
        start = 0
        end = len(string)
        for i in range(start, end):
            suffix = string[i:end]
            self._insert_suffix(suffix, start, len(suffix), self.root)

    def contains(self, string):
        current = self.root
        for char in string:
            if char not in current:
                return False
            current = current[char]
        return True if self.endSymbol in current else False

    def _insert_suffix(self, suffix, idx, end, current_node):
        if idx == end:
            current_node[self.endSymbol] = True
            return
        current_char = suffix[idx]
        if current_char in current_node:
            current_node = current_node[current_char]
            self._insert_suffix(suffix, idx + 1, end, current_node)
        else:
            current_node[current_char] = {}
            self._insert_suffix(suffix, idx + 1, end, current_node[current_char])
