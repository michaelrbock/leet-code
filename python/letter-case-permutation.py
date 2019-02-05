class Solution:
  def letterCasePermutation(self, S):
    """
    :type S: str
    :rtype: List[str]
    """
    results = []

    def recurse(i, so_far):
      if i == len(S):
        results.append(so_far)
        return
      if S[i].isalpha():
        recurse(i + 1, so_far + S[i].lower())
        recurse(i + 1, so_far + S[i].upper())
      else:
        recurse(i + 1, so_far + S[i])

    recurse(0, '')
    return results
