class Solution(object):
  def findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    # Make graph in form { course : set(prereqs) }
    graph = {}
    for course in range(numCourses):
      graph[course] = set()
    for course, prereq in prerequisites:
      graph[course].add(prereq)

    # Create schedule.
    result = []
    while graph:
      prev_len = len(result)
      # Get next free course.
      for course, prereqs in graph.items():
        if not prereqs:
          result.append(course)
          for other_course in graph:
            if course in graph[other_course]:
              graph[other_course].remove(course)
          del graph[course]
      if len(result) == prev_len:
        return []

    return result
