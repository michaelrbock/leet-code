class Solution:
  def isAlienSorted(self, words: 'List[str]', order: 'str') -> 'bool':
    # Create dict from order.
    dictionary = {}
    for i, char in enumerate(order):
      dictionary[char] = i

    def compare(word1, word2):
      """Returns True if word1 <= word2."""
      i = 0
      while i < len(word1) and i < len(word2):
        if dictionary[word1[i]] < dictionary[word2[i]]:
          return True
        elif dictionary[word1[i]] > dictionary[word2[i]]:
          return False
        # they're equal
        i += 1
      # Check if one string is longer than the other
      if i < len(word2):  # Still letters left in word2
        return True
      else:  # Still letters left in word1
        return False

    for i in range(len(words) - 1):
      if not compare(words[i], words[i+1]):
        return False

    return True
