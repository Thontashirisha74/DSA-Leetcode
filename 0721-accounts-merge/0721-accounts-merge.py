from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:

        graph = defaultdict(list)
        email_to_name = {}

        # Build graph
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                email_to_name[email] = name

                graph[first_email].append(email)
                graph[email].append(first_email)

        visited = set()
        answer = []

        # DFS for every connected component
        for email in email_to_name:

            if email not in visited:

                stack = [email]
                visited.add(email)

                emails = []

                while stack:

                    current = stack.pop()
                    emails.append(current)

                    for neighbor in graph[current]:

                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                emails.sort()

                name = email_to_name[email]

                answer.append([name] + emails)

        return answer