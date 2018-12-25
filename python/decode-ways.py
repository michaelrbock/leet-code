class Solution1:
  def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """
    # Special case for leading 0's.
    if not s or s[0] == '0':
      return 0

    ways = [1, 1]  # ways[i] = how many ways to decode s[:i].
    for index in range(2, len(s) + 1):
      last_two = int(s[index-2:index])
      print(last_two)
      # Special case for 0's.
      if last_two == 0:
        return 0
      # Take one or take two (with exceptions).
      elif s[index-2] == '0' or last_two == 10 or last_two == 20:
        ways.append(ways[index-1])
      elif 1 <= last_two <= 26:
        ways.append(ways[index-2] + ways[index-1])
      else:
        ways.append(ways[index-1])
    return ways[-1]


class Solution:
  def numDecodings(self, s):
    dp = [0] * (len(s) + 1)
    dp [0] = 1
    dp[1] = 1 if 1 <= int(s[0]) <= 9 else 0

    for i in range(2, len(s) + 1):
      if 1 <= int(s[i-1:i]) <= 9:
        dp[i] += dp[i-1]
      if s[i-2:i][0] != '0' and int(s[i-2:i]) <= 26:
        dp[i] += dp[i-2]
    return dp[-1]


s = Solution()
# assert s.numDecodings('') == 0
# assert s.numDecodings('0') == 0
# assert s.numDecodings('00') == 0
# assert s.numDecodings('01') == 0
# assert s.numDecodings('100') == 0
# assert s.numDecodings('101') == 1
assert s.numDecodings('110') == 1
# assert s.numDecodings('12') == 2
# assert s.numDecodings('226') == 3
# assert s.numDecodings('8512') == 2
# assert s.numDecodings('851212') == 5
# assert s.numDecodings('85121215') == 13
