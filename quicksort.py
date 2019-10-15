def quicksort(a,l,h):
    if(l<h):
        j=partition(a,l,h)
        quicksort(a,l,j)
        quicksort(a,j+1,h)

def partition(a,l,h):
    pivot=a[l]
    i,j=l,h
    while(i<j):
        while(a[i]<=pivot):
            i+=1
            if i==h+1:
                break

        while(a[j]>pivot):
            j-=1
            if j==l-1:
                break
        if(i<j):
            a[i],a[j]=a[j],a[i]
    if j!= l-1:
        a[l],a[j]=a[j],a[l]
    return j
a=[3,2,5,1,8,9]
start1,end1=2,5
start2,end2=1,6
k1,k2=2,4
a1=a[start1-1:end1]
a2=a[start2-1:end2]
print(a1,a2)
quicksort(a1,0,len(a1)-1)
quicksort(a2,0,len(a2)-1)
print(a1[k1-1])
print(a2[k2-1])

