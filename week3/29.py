def cnt(kytu,chuoi):
    return chuoi.count(kytu)

if __name__ == "__main__":
    s=str(input())
    a= str(input())
    b=cnt(a,s)
    print(f"So lan xuat hien cua {a}: {b}")