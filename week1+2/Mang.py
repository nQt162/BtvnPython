a=[0,1,2,3,4,5,6,7,8,9]

#them 3 vào list
a.append(3)
print(a)

#dem co bn phan tu 3 =>2
print(a.count(3))

#copy list b từ list a
b=a.copy()
print(b)

#in ra vị trí của phần tử 9 trong mảng a
print(a.index(9))

#thêm ptu 1.5 vào vị trí thứ 2
a.insert(2,1.5)
print(a)

#xóa phần tử thông qua vị trí 
a.pop(2)
print(a)

#xóa phần tử thông qua giá trị
a.remove(3)
print(a)

#đảo ngược các ptu trong a
a.reverse()
print(a)

#xóa all ptu trong a
a.clear
print(a)