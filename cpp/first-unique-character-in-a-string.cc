class Solution {
 public:
  int firstUniqChar(string s) {
    unordered_map<char, int> counts;
    for (char c : s) {
      if (counts.find(c) == counts.end()) {
        counts[c] = 1;
      } else {
        counts[c]++;
      }
    }

    for (int i = 0; i < s.length(); ++i) {
      if (counts[s[i]] == 1) {
        return i;
      }
    }
    return -1;
  }
};
