from math import*
def snt(n):
    if n<2 : return False
    for i in range(2, int(sqrt(n))+1, 1):
        if n%i==0: return False
    return True

if __name__ == '__main__':
    n=int(input())
    A=[]
    B=[]
    for i in range(1,n+1,1):
        if (n%i==0) and snt(i) : A.append(i)
        elif (n%i!=0) and snt(i): B.append(i)
    print(A,B)    