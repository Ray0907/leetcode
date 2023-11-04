from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        in_degree = [0] * numCourses
        for course ,x in prerequisites:
            in_degree[course] +=1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        while queue:
            course = queue.popleft()
            for next_course in graph[course]:
                in_degree[next_course] -=1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return all(in_degree[i] == 0 for i in range(numCourses))
