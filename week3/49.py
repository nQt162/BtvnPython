
def test(n):
    num_str = str(n)
    b = len(num_str)
    a = sum(int(digit)**b for digit in num_str)
    return a
def check(n):
    if n==test(n): print("True")
    else: print("False")
        
if __name__ == "__main__":
    n = int(input())
    check(n)
    