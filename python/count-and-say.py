class Solution:
  def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    result = '1'
    for i in range(n-1):
      index = 0
      new_result = []
      while index < len(result):
        count = 0
        num = result[index]
        while index < len(result) and result[index] == num:
          count += 1
          index += 1
        new_result.append(str(count) + str(num))
      result = ''.join(new_result)
    return result


s = Solution()
assert s.countAndSay(1) == '1'
assert s.countAndSay(4) == '1211'
assert s.countAndSay(5) == '111221'
