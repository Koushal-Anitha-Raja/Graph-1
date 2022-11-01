class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
         # the indegree array is multiplied n
        indegree = [0]*n
        
        #iterate through the person trust 
        for person,trusted_person in trust:
            # decrementing indegree person by 1 to find the judge
            indegree[person-1]-=1 
            # increment the trusted person by one at each state
            indegree[trusted_person-1]+=1 
            #iterate through the loop in indegree
        for i in range(len(indegree)):
            
             # if indegree is equal to last value
            if indegree[i] == n-1:
                #then add plus one return as index
                return i+1
        return -1
        