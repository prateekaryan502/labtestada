a=[1,12,15,26,38]
b=[2,13,17,30,45]
def median(a):
    if len(a)%2==0:
        return (a[len(a)//2-1]+a[len(a)//2])/2
    else :
        return (a[len(a)//2])
def findmedian(a,b):
    if len(a)==2:
        m=(max(a[0],b[0])+min(a[1],b[1]))/2
        return m
    m1 = median(a)
    m2 = median(b)
    if m1==m2:
        return m1
    if m1>m2:
        return findmedian(a[:len(a)//2+1],b[len(b)//2:])
    if m1<m2:
        return findmedian(a[len(a)//2:],b[:len(b)//2+1])
print(findmedian(a,b))
