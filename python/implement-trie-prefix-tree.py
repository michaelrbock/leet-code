class Node(object):
  def __init__(self):
    self.word = False
    self.children = {} # { char : Node }


class Trie(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = Node()

  def insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: None
    """
    curr = self.root

    end_index = None
    for i, char in enumerate(word):
      if char in curr.children:
        curr = curr.children[char]
      else:
        end_index = i
        break

    if end_index is not None:
      for i in range(end_index, len(word)):
        curr.children[word[i]] = Node()
        curr = curr.children[word[i]]

    curr.word = True

  def search(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    curr = self.root

    for char in word:
      if char in curr.children:
        curr = curr.children[char]
      else:
        return False

    return curr.word

  def startsWith(self, prefix):
    """
    Returns if there is any word in the trie that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    curr = self.root

    for char in prefix:
      if char in curr.children:
        curr = curr.children[char]
      else:
        return False

    return curr.word or len(curr.children) > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
