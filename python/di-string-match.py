class Solution:
  def diStringMatch(self, S: 'str') -> 'List[int]':
    result = []
    increase = 0
    decrease = len(S)
    for char in S:
      if char == 'I':
        result.append(increase)
        increase += 1
      else:  # char == 'D'
        result.append(decrease)
        decrease -= 1
    if S[-1] == 'I':
      result.append(increase)
    else:  # S[-1] == 'D'
      result.append(decrease)
    return result
