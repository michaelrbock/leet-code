class Solution:
  def defangIPaddr(self, address: str) -> str:
    new_ip = []
    for char in address:
      if char == '.':
        new_ip.extend(['[', '.', ']'])
      else:
        new_ip.append(char)
    return ''.join(new_ip)
