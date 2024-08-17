class Node:
    def __init__(self):
        self.links = [None for _ in range(26)]
        self.termination = False    

class Trie:
    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        def insert_ix(node, word, ix):
            cix = ord(word[ix]) - ord("a")
            if not node.links[cix]:
                node.links[cix] = Node()
            if ix < len(word) - 1:
                insert_ix(node.links[cix], word, ix+1)
            else:
                node.links[cix].termination = True
                return

        insert_ix(self.node, word, 0)

    def search(self, word: str) -> bool:
        # search_str(node, word, ix)
        if self.node:
            cur = self.node
            for i,c in enumerate(word):
                cix = ord(c) - ord("a")
                if not cur.links[cix]:
                    return False
                else:
                    cur = cur.links[cix]
            if cur.termination:
                return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        if self.node:
            cur = self.node
            for i,c in enumerate(prefix):
                cix = ord(c) - ord("a")
                if not cur.links[cix]:
                    return False
                else:
                    cur = cur.links[cix]
            return True
        else:
            return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)