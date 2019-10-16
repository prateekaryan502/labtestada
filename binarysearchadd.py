import sys
def upperbound(arr,key):
    s=0
    e=len(arr)-1
    while(s<=e):
        m=(s+e)//2
        if key>=a[m]:
            s=m+1
        else :
            e=m-1
    return  s-1
def lowerbound(arr,key):
    e=len(arr)-1
    s=0
    while(s<=e):
        m=(s+e)//2
        if key<=a[m]:
            e=m-1
        else :
            s=m+1
    return  e+1
if __name__=="__main__" :
   sys.stdin = open('input.txt', 'r')
   n=int(input())
   a=[int(i) for i in input().split()]
   key=int(input())
   s=0
   e=len(a)-1
   l=lowerbound(a,key)
   u=upperbound(a,key)
   c=u-l+1
   if l>u :
       print(-1,-1,0)
   else :
       print(l,u,c)
