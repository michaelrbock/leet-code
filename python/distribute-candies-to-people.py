class Solution:
  def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    people = [0] * num_people

    i = 0
    candy = 1
    while candies > 0:
      if candy > candies:
        candy = candies
      people[i] += candy
      candies -= candy
      i += 1; candy += 1
      if i >= num_people:
        i %= num_people

    return people
