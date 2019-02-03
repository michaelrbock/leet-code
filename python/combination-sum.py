class Solution:
  def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    results = []

    def combination_sum_rec(target, start, so_far):
      if target == 0:
        results.append(so_far[:])
        return
      for i in range(start, len(candidates)):
        if target - candidates[i] >= 0:
          so_far.append(candidates[i])
          combination_sum_rec(target - candidates[i], i, so_far)
          del so_far[-1]

    combination_sum_rec(target, 0, [])
    return results
