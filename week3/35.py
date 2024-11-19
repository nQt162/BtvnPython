def cnt(a,x):
    cnt = 0
    for i in a: 
        if i==x : 
             cnt+=1
    return cnt         
 

if __name__ == "__main__":
    n=int(input())
    a=[]
    for i in range(n): 
        x=int(input())
        a.append(x)
    b=int(input("Phan tu dem: "))
    cnt = cnt(a,b)
    print(cnt)