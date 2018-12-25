class Solution {
 public:
  int climbStairs(int n) {
    // Strategy: fibonacci numbers.
    int prev = 0;
    int curr = 1;
    for (int i = 0; i < n; ++i) {
      int temp = curr;
      curr = curr + prev;
      prev = temp;
    }
    return curr;
  }
};
