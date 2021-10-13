import random
import math
import multiprocessing as mp
import functools
import time


def hyper_volume(nd):

    g=math.gamma(nd*0.5+1)
    v=(math.pi**(nd*0.5))/g
    return v

def hyper_volume_approx(n,nd):
    nc=0.0

    l=[[random.uniform(-1,1) for i in range(nd)] for i in range(n) ]

    for i in range(n):
        if functools.reduce(lambda x,y: x+y,map(lambda x: x*x, l[i]))<=1:
            nc+=1
    v_approx=2**nd*nc/n
    return v_approx


n=100000
nd=10

import timeit

start = time.time()

print('Approx v: ', hyper_volume_approx(n,nd))
print('Real v: ',hyper_volume(nd))
print('time std version: ',time.time()-start)
print('\n')



np=32
if np>mp.cpu_count():
    sys.exit('Cores not available')
n=100000


proc=[]
pn=[n//np for i in range(np)]
pn[-1]+=n%np

map_args=[(x,nd) for x in pn]

start = time.time()
with mp.Pool(processes=np) as pool:
    v_sum = pool.starmap(hyper_volume_approx,map_args)
    v=sum(v_sum)*(1.0/np)
print('time parallel version: ',time.time()-start)

print('approx v: ', v)
print('real v: ', hyper_volume(nd))
#hello