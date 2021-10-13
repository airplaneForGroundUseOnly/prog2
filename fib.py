import time 


def fib_py(n) :
    if n<=1:
        return n
    else:
        return(fib_py(n-1))+fib_py(n-2)
    
    
n=20
start=time.time()
f=Integer(f) 
f.fib(n)
print('C++ time: ', time.time-start)


start=time.time()
fib_py(n)
print(time.time()-start)


    
    
