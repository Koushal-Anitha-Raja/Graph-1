class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        q = deque() 
        # in degree array is initialized with zeros to the length
        indegree = [0]*numCourses
        #initialize course studies to zero
        courseStudied = 0
        
        #creating defaultdict as value pair is list
        adj = defaultdict(list) 
        
        #loop through the prerequisties array
        for course,prereq in prerequisites:
            # appending course to adjacency matrix
            adj[prereq].append(course) 
             # incrementing at each state
            indegree[course]+=1
        
        #loop through the indegree array
        for i in range(len(indegree)):
            # if indegree is zzero then the course can be added
            if indegree[i] == 0: 
                q.append(i)
        #if cannot return false        
        if not q:
            return False
        #until the queue is empty
        while q:
             # pop from queue and store it in curr
            curr = q.popleft()
            courseStudied+=1 
            #iterate through the adj list
            for dependent in adj[curr]:
                #decrement at each state
                indegree[dependent] -= 1 
                # if dependent is equal to 0
                if indegree[dependent] == 0: 
                    q.append(dependent) 
         # if course studied is equal to numcourses
        if courseStudied == numCourses:
            return True
        #else return false
        return False
        