def test(n):
    sum=0
    for i in range(3,n+1,3):
        sum+=i
    print("Tổng các số chia hết cho 3: ",sum)

if __name__ == "__main__":
    n=int(input())
    test(n)