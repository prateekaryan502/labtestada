a=[[0,0,1,0,1,0],[0,0,0,0,0,1],[1,0,0,0,1,0],[0,0,0,0,0,0],[1,0,1,0,0,0],[0,1,0,0,0,0]]
visited=[False for i in range(len(a))]
count=0
def DFS(i,visited):
    if visited[i]==False:
        visited[i]=True
        print(i,end=" ")
    for j in range(len(a)):
        if a[i][j]==1 and visited[j]==False:
            DFS(j,visited)
for i in range(len(a)):
    if visited[i]==False:
        count+=1
        DFS(i,visited)
        print("")
print("Number of connected components are :",count)