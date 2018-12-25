from collections import defaultdict

class Solution:
  def fourSumCount(self, A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    # Idea: combine sums for A+B, C+D then do dict trick.
    a_b = []
    for i in range(len(A)):
      for j in range(len(B)):
        a_b.append(A[i] + B[j])
    c_d = defaultdict(int)
    for i in range(len(C)):
      for j in range(len(D)):
        partial_sum = C[i] + D[j]
        c_d[partial_sum] += 1
    result = 0
    for num in a_b:
      diff = 0 - num
      if diff in c_d:
        result += c_d[diff]
    return result


s = Solution()
assert s.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]) == 2
assert s.fourSumCount([-1,-1], [-1,1], [-1,1], [1,-1]) == 6
