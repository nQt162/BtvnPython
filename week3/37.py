def check(n):
    if n<2: return 0
    for i in range(2,int(n**0.5)+1,1):
            if n%i==0: return 0
    return 1

def inkq(a):
    b=[]
    for i in a:
        if check(i)==1: 
           b.append(i)
    print(f"{b}")
if __name__ == "__main__":
    n=int(input())
    a=[]
    for i in range(n):
        x=int(input())
        a.append(x)
    inkq(a)