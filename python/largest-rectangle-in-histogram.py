class Solution:
  def largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    stack = []
    max_area = 0
    index = 0
    while index < len(heights):
      if not stack or heights[index] >= heights[stack[-1]]:
        stack.append(index)
        index += 1
      else:
        top = stack.pop()
        print(heights[top], index, stack[-1] if stack else index)
        area = heights[top] * (index - stack[-1] - 1 if stack else index)
        max_area = max(max_area, area)

    while stack:
      top = stack.pop()
      area = heights[top] * (index - stack[-1] - 1 if stack else index)
      max_area = max(max_area, area)

    return max_area
