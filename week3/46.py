import math
def check(n):
    sum = 1
    for i in range (2,int(n**0.5+1)):
        if n%i==0: 
            sum+=i
            if i!=1 and i!=n//i: sum += n//i
    return sum

def test(n):
    if n==check(n): print("TRUE")
    else : print("FALSE")


if __name__ == "__main__":
    n=int(input())
    test(n)