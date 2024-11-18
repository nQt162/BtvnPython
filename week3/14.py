A=[]

def fibo(n):
        if n==1 : return 1
        elif n==0 : return 0
        else : return fibo(n-1) + fibo(n-2)

def test():
      for i in range(len(A)):
            print(A[i],end=" ")

if __name__ == "__main__":
    n=int(input())
    for i in range (n+1): A.append(fibo(i))
    test()