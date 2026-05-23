class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for a, b in prerequisites:
            indegrees[a] += 1
            graph[b].append(a)
        
        res = []
        queue = deque()

        for course, degree in enumerate(indegrees):
            if degree == 0:
                queue.append(course)
        
        while queue:
            node = queue.popleft()
            res.append(node)
            for nh in graph[node]:
                indegrees[nh] -= 1
                if indegrees[nh] == 0:
                    queue.append(nh)
        
        if len(res) == numCourses:
            return res
        else:
            return []