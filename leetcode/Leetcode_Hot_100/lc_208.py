class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word not in self.dic.keys():
            self.dic[word] = [word]
            for i in range(len(word)):
                self.dic[word].append(word[:-i - 1])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.dic.keys():
            return True
        else:return False
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for i in self.dic.keys():
            if prefix in self.dic[i]:
                return True
        return False
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
t = Trie()
t.insert('app')
print(t.startsWith('app'))