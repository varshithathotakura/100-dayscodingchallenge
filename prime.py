##def isPrime(n):
##    if n <= 1:
##    	return False
##    for i in range(2,int(n**0.5) + 1):
##    	if n % i == 0:
##    		return False
##    return True
##N = int(input())
##def specialPrime(N):
##    n = N
##    var=[]
##    if isPrime(n) == False:
##        return(False,[])
##    while n > 1:
##        n  -= 2
##        if isPrime(n):
##            var.append(n)
##        if len(var) == 2 :
##            if var[0] + var[1] +1 == N:
##                return True,var
##            else :
##                var = var[1:]
##    return False,[]
##ans,value = specialPrime(N)
##if ans:
##        print("Yes. It is a  special prime .\n%d + %d + 1 = %d"%(value[0],value[1],N))     
##else:
##        print("No. It's not a special prime.") 

def isPrime(n):
    if n <= 1:
    	return False
    for i in range(2,int(n**0.5) + 1):
    	if n % i == 0:
    		return False
    return True
N = int(input())
def specialPrime(N):
    n = N
    x,y = 0,0
    if isPrime(n) == False:
        return(False,[])
    while n > 1:
        n  -= 2
        if isPrime(n):
            if x:
                y = n
            else:
                x = n
        if y:
            if x+y +1 == N:
                return True,(x,y)
            else :
                x,y = y,0
    return False,[]
ans,value = specialPrime(N)
if ans:
        print("Yes. It is a  special prime .\n%d + %d + 1 = %d"%(value[0],value[1],N))     
else:
        print("No. It's not a special prime.")
        
