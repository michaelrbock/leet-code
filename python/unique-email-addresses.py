def normalize(email):
  name, domain = email.split('@')
  normalized = []
  for char in name:
    if char == '+':
      break
    elif char != '.':
      normalized.append(char)
  normalized += '@' + domain
  return ''.join(normalized)


class Solution:
  def numUniqueEmails(self, emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    unique_emails = set()
    for email in emails:
      unique_emails.add(normalize(email))
    return len(unique_emails)
