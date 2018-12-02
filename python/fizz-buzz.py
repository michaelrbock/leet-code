class Solution:
  def fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = []
    for num in range(1, n + 1):
      if num % 3 == 0 and num % 5 == 0:
        result.append('FizzBuzz')
      elif num % 5 == 0:
        result.append('Buzz')
      elif num % 3 == 0:
        result.append('Fizz')
      else:
        result.append(str(num))
    return result