class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        res = defaultdict(str)

        for email in emails:
            curr_email = set()

            for i in range(len(email)):
                if email[i] == '.' and '@' not in curr_email:
                    continue

                if email[i] == '+':
                    res[email] += email[email.index("@"):]
                    break
                else:
                    res[email] += email[i]
                    curr_email.add(email[i])

        uniqueEmails = set()

        for email, val in res.items():
            uniqueEmails.add(val)

        return len(uniqueEmails)