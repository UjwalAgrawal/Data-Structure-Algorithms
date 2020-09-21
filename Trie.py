# Trie implementation in python
# Special thanks to https://stackoverflow.com/users/577088/senderle for his answer

class Trie:
    def __init__(self):
        self.tree = {}
    
    def addPattern(self, words):
        _end = '_end_'
        for pattern in words:
            current_dict = self.tree
            for i in pattern:
                current_dict = current_dict.setdefault(i,{})
            current_dict[_end] = _end

    
    def searchPattern(self, pattern):
        current_dict = self.tree
        for i in pattern:
            if i not in current_dict:
                return(False)
            else:
                current_dict = current_dict[i]
        return(True)


if __name__ == "__main__":
    T = Trie()
    n = int(input("Numer of words: "))
    words = []
    for _ in range(n):
        words.append(input())
    #seach pattern
    T.addPattern(words)
    pattern = input("Enter the pattern to search for: ")
    print(T.searchPattern(pattern))


