import math
def CS(r):
    return 2*r*math.pi, math.pi* r**2

if __name__ == "__main__":
    r=int(input())
    C,S=CS(r)
    print(f"Chu vi: {C}, Diện tích: {S}")