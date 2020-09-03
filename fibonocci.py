def fib(n):
        a=0
        b=1
        print(a,b,end=" ")
        i=2
        while i<n:
                c=a+b
                print(c,end=" ")
                a=b
                b=c
                i+=1
        print(b)
                
fib(8)             


##def fibSum(n):
##	ans = ((1+5**0.5)/2)**n -((1-5**0.5)/2)**n
##	ans = int(ans/(5**0.5))
##	return ans
##print(fibSum(int(input())+1))      

##def fib(n):#6,5
##        if n==1:
##                return 0
##        elif n==2:
##                return 1
##        else:
##                return(fib(n-1)+fib(n-2))
##print(fib(6))


##def fact(n):#5,4,3,2,1
##        if n==0 or n==1:
##                return 1
##        else:
##                return(n*fact(n-1))#5*4*3*2*1
##
##print(fact(5))

