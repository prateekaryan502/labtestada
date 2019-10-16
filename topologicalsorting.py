def topologicalorder(n,a):
    indegree = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            indegree[i]=indegree[i]+a[j][i]
    for j in range(n):
        for i in range(n):
            if indegree[i]==0:
                print(i)
                indegree[i]=-1
                for j in range(n):
                    if a[j][i]==1:
                        indegree[j]=indegree[j]-1
n=4 #number of jobs
dependencies=[[1,0],[2,0],[3,1],[3,2]]
a=[[0 for i in range(n)]for j in range(n)]
for i in dependencies:
    a[i[0]][i[1]]=1
print(a)
topologicalorder(n,a)