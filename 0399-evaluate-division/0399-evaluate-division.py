class Solution:
    def calcEquation(self, equations, values, queries):

        graph = {}

        # Build graph
        for (a, b), value in zip(equations, values):

            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(start, end, visited):

            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, value in graph[start]:

                if neighbor not in visited:

                    result = dfs(neighbor, end, visited)

                    if result != -1.0:
                        return value * result

            return -1.0

        answer = []

        for start, end in queries:

            # Variable doesn't exist
            if start not in graph or end not in graph:
                answer.append(-1.0)

            else:
                answer.append(dfs(start, end, set()))

        return answer