def fibg():
    c,p=0,1
    while (True):
        q=c+p
        yield q
        p=c
        c=q
        
fib_gen=fibg()        
 
for i in range(1, 10):
    print(i,next(fib_gen))