r=raw_input()
n=len(r)
count=0
for i in range(0,n):
     for j in range(i+1,n):
            if(r[i]==r[j]:
                 count=count+1
if(count==0):
   print "yes"
else:
   print "no"
