a=[5,4,3,2,1]
n=len(a)
r=0
for i in range(0,n):
     for j in range(i+1,n):
         if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in range(0,n):
     r=r+1
if(r>=1):
     print a
