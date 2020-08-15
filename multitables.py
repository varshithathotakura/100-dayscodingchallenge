##n=int(input("enter a num"))
##r1=int(input("enter a start range"))
##r2=int(input("enter a end range"))
##if(r1>r2):
##    m=1
##else:
##    m=-1
##for i in range (r1,r2+1,m):
##   print(n,"*",i,"=",n*i)
##
n=int(input("Enter a number: "))
r1=int(input("Enter the starting range: "))
r2=int(input("Enter the  ending range: "))
if(r1>r2):
	for i in range(r1,r2-1,-1):
		print(n,'*',i,'=',n*i)
else:
	for i in range(r1,r2+1):
		print(n,'*',i,'=',n*i)


