if __name__ == '__main__':
    n = int(input("Nhập số lượng sinh viên cần thống kê: "))  # Nhập số lượng sinh viên
    danhsach = {}  # Khởi tạo từ điển rỗng để lưu tên và điểm của sinh viên

    # Nhập thông tin sinh viên
    for i in range(n):
        ten = input("Nhập tên sinh viên: ")
        diem = int(input("Nhập điểm của sinh viên: "))
        danhsach[ten] = diem

    # Khởi tạo từ điển sodiem để đếm số lượng sinh viên đạt từng mức điểm
    sodiem = {i: 0 for i in range(11)}

    # Thống kê số lượng sinh viên đạt từng mức điểm
    for diem in danhsach.values():
        sodiem[diem] += 1

    # In kết quả thống kê
    for diem in range(10, -1, -1):
        print(f"Điểm {diem}: {sodiem[diem]} học sinh")
