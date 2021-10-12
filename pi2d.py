import random
import math
import matplotlib.pyplot as plt

def isInside(px,py):
    return px*px+py*py<1


n=1000000

l1=[0]*n
l2=[0]*n
for i in range(n):
    l1[i]=random.uniform(-1,1)
    l2[i]=random.uniform(-1,1)


nc=0.0
lc1=[]
lc2=[]
lo1=[]
lo2=[]
for i in range(n):
    if isInside(l1[i],l2[i]):
                nc+=1
                lc1.append(l1[i])
                lc2.append(l2[i])
    else: 
      lo2.append(l2[i])
      lo1.append(l1[i])

  
plt.plot(lc1,lc2,'o')       
plt.plot(lo1,lo2,'o')   
plt.show


pi_approx=4*nc/n
print(pi_approx)
print(math.pi)
