from collections import Counter

def _valid_word(word, chars):
  char_counts = Counter(chars)
  for char in word:
    if char not in char_counts or char_counts[char] <= 0:
      return False
    char_counts[char] -= 1
  return True

class Solution:
  def countCharacters(self, words: List[str], chars: str) -> int:
    count = 0
    
    for word in words:
      if _valid_word(word, chars):
        count += len(word)
        
    return count
