class Solution(object):
  def permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = set()

    def permute_rec(so_far, to_go):
      if not to_go:
        results.add(tuple(so_far))

      for i in range(len(to_go)):
        permute_rec(so_far + [to_go[i]], to_go[:i] + to_go[i+1:])

    permute_rec([], nums)
    return list(results)
