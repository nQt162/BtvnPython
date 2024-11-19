def reverse():
    chuoi_dao= ""
    chuoi=str(input())
    for i in chuoi:
        chuoi_dao=i+chuoi_dao
    print(chuoi_dao)
    check(chuoi,chuoi_dao)

def check(chuoi,chuoi_dao):
    if(chuoi==chuoi_dao): print("TRUE")
    else : print("FALSE")

if __name__ == "__main__":
   reverse()
   