class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for a, b in prerequisites:
            indegrees[a] += 1
            graph[b].append(a)
        
        completed = 0
        queue = deque()

        for course, degree in enumerate(indegrees):
            if degree == 0:
                queue.append(course)
        
        while queue:
            node = queue.popleft()
            completed += 1
            for nh in graph[node]:
                indegrees[nh] -= 1
                if indegrees[nh] == 0:
                    queue.append(nh)
        
        return completed == numCourses
            
        