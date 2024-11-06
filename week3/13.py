from math import*
def prime(n):
    if n<2: return 0
    for i in range (2, int(n ** 0.5) + 1,1):
        if(n%i==0): return 0
    return 1
if __name__ == '__main__':
    n=int(input())
    N=[]
    a=0
    for i in range (2,n+1,1):
        if prime(i): 
         print("Số nguyên tố:",i )
    