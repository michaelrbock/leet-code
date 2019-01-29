from collections import defaultdict, deque


def ok_prereqs(graph, course, visited):
  if course not in graph:
    return True
  if course in visited:
    return False
  visited.add(course)
  for prereq in graph[course]:
    if not ok_prereqs(graph, prereq, visited):
      return False
  visited.remove(course)
  return True


class Solution:
  def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    # 1. build graph
    graph = defaultdict(set)
    for prereq_list in prerequisites:
      course = prereq_list[0]
      for prereq in prereq_list[1:]:
        graph[course].add(prereq)

    # 2. traverse for each course
    for course in range(numCourses):
      if course not in graph:
        continue  # No prereqs.
      if not ok_prereqs(graph, course, set()):
        return False

    return True


s = Solution()
assert s.canFinish(2, [[1,0]])
assert not s.canFinish(2, [[1,0],[0,1]])
assert s.canFinish(3, [[0,1],[0,2],[1,2]])
