class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        temp = self.trie
        for letter in word:
            if letter not in temp:
                temp[letter] = {}
            temp = temp[letter]
        temp[-1] = -1

    def search(self, word: str) -> bool:
        def recursive(curr, wrd):
            if type(curr) is dict:
                for i, letter in enumerate(wrd):
                    if letter == '.':
                        found = False
                        for j in curr:
                            found = found or recursive(curr[j], wrd[i+1:])
                        return found

                    if letter in curr:
                        curr = curr[letter]
                    else:
                        return False

                return -1 in curr
            else:
                return False
        return recursive(self.trie, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
