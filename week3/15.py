N=int(input())
if(N%2==0):print("Tổng các số chẵn:",int(N*(N/2+1)/2))
else :
    a=(N-1)/2 
    print("Tổng các số chẵn:",int(a*(a+1)))