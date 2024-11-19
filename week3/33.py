def max(a):
    max=-1e-1
    for i in a:
        if max < i: max = i
    return max    

if __name__ == "__main__":
    n=int(input())
    a=[]
    for i in range(n):
        x=int(input())
        a.append(x)
    max = max(a)
    print(max)    
