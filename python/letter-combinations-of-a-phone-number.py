LETTERS = {
  '2': ['a', 'b', 'c'],
  '3': ['d', 'e', 'f'],
  '4': ['g', 'h', 'i'],
  '5': ['j', 'k', 'l'],
  '6': ['m', 'n', 'o'],
  '7': ['p', 'q', 'r', 's'],
  '8': ['t', 'u', 'v'],
  '9': ['w', 'x', 'y', 'z'],
}

class Solution:
  def _letter_combinations_rec(self, digits, so_far):
    if not digits:
      self.results.append(so_far)
      return
    for letter in LETTERS[digits[0]]:
      self._letter_combinations_rec(digits[1:], so_far + letter)

  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    self.results = []
    if digits:
      self._letter_combinations_rec(digits, '')
    return self.results
