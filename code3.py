n= int(input("Enter any Number: "))
count = 0
i = 2
while(i <=n//2):
    if(n% i == 0):
        count = count + 1
        break
    i = i + 1
if (count == 0 and n!= 1):
    print(n,"is a Prime Number")
else:
    print(n,"is not a Prime Number")
