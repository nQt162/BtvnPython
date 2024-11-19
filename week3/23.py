a=[]
def aver(a,n):
    sum=0   
    for i in a:
        sum+=i
    print("Trung binh cong:",f"{sum/n:.1f}")

if __name__ == "__main__":
    n=int(input())
    for i in range(n): 
        x=int(input())
        a.append(x)
    aver(a,n)