
from typing import List
class ExempleTrie:
    def __init__(self):
        self.root = dict()
    def insert(self, word: str) -> None:
        cur = self.root
        for i in word :
            if i not in cur :
                cur[i] = dict()
            cur = cur[i]
        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word :
            if i not in cur : return False
            cur = cur[i]
        return '*' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix :
            if i not in cur : return False
            cur = cur[i]
        return True

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        # Implement logic for inserting a word into the Trie

    def search(self, word):
        node = self.root
        # Implement logic for searching a word in the Trie

    def startsWith(self, prefix):
        node = self.root



inputs = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
words = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
output = []
for i, command in enumerate(inputs):
    if command == "Trie":
        trie = Trie()
        output.append(None)
    elif command == "insert":
        trie.insert(words[i][0])
        output.append(None)
    elif command == "search":
        output.append(trie.search(words[i][0]))
    elif command == "startsWith":
        output.append(trie.startsWith(words[i][0]))
print("Output:", output)



class Longest_Common_Prefix(Trie) :
    def insert(self,word):
        cur = self.root
        for index,i in enumerate(word) :
            if len(cur.children) == 0 :
                cur[i] = TrieNode()
            if i not in cur.children :
                cur.is_end_of_word = True
                return
        cur.is_end_of_word = True
    def longestCommonPrefix(self, l: List[str]) -> str:
        cur = self.root
        prefix = ''
        while cur.is_end_of_word == False :
            cur.childre = cur.pop()
            prefix += cur



















