from typing import List


class Trie:

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


