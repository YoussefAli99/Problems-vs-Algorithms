class TrieNode:
    def __init__(self, value=False):
        ## Initialize this node in the Trie
        self.value = value
        self.char_dict = dict()

    def insert(self, char):
        c_node = TrieNode()
        self.char_dict[char] = c_node
        return c_node

    def suffixes(self, suffix=''):
        output = list()

        def find_suffix(node, output_):
            if node.value:
                output.append(output_)
            for char in node.char_dict:
                temp = output_ + char
                find_suffix(node.char_dict[char], temp)
        find_suffix(self, '')
        return output


class Trie:
    def __init__(self):
        root_node = TrieNode()
        self.root = root_node

    def insert(self, word):
        cur = self.root
        for char in word:
            if char in cur.char_dict:
                cur = cur.char_dict[char]
            else:
                new_child_node = cur.insert(char)
                cur = new_child_node
        cur.value = True

    def find(self, prefix):
        cur = self.root
        for char in prefix:
            if char in cur.char_dict:
                cur = cur.char_dict[char]
            else:
                return None

        return cur

    def __str__(self):
        output_ = ['']
        def print_n(node, output_):
            output_[0] += f"End of word: {node.value}\n"
            for char in node.char_dict:
                output_[0] += f"char: {char}"
                print_n(node.char_dict[char], output_)
        print_n(self.root, output_)
        return output_[0]


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"]
for word in wordList:
    MyTrie.insert(word)

node = MyTrie.find('f')
print(node.suffixes())