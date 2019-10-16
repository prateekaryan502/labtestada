a=[[1,0,1,0,1],[1,1,0,0,0],[0,1,0,1,1]]
count=0
visited=[[False for i in range(len(a[0]))] for j in range(len(a))]

def DFS(i,j,visited,a):
    visited[i][j]=True
    print([i,j],end=" ")
    for m in range(i-1,i+2):
        for n in range(j-1,j+2):
            if m>=0 and n>=0 and n<=len(a[0])-1 and m<=len(a)-1:
                if a[m][n]==1  and visited[m][n]==False:
                    DFS(m,n,visited,a)

for i in range(len(a)):
    for j in range(len(a[0])):
        if visited[i][j]==False and a[i][j]==True:
            DFS(i,j,visited,a)
            count+=1
            print("")
print(count)