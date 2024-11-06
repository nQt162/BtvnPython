

if __name__ == '__main__':
    n=int(input())
    A=[]
    B=[]
    for i in range (0, n, 1):
        x=int(input())
        A.append(x)
    for i in range(0, n, 1):
        x=int(input())
        B.append(x)
    mydict={A[i]:B[i] for i in range(0, n, 1)}
    print(mydict)