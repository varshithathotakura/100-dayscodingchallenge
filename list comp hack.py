if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())#n is an integer that the cordianes sum <n i.e,(i+j+k)<n.
    arr = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
print(arr)
