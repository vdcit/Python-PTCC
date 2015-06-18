# Bai tap ve nha buoi 5 
# Author: Nguyen Hoai Name
print """An 1 de tao may ao
An 2 de xoa may ao
An 3 de thay doi cau hinh
An 'q' de thoat chuong trinh
An 'p' de hien thong tin may ao"""
a = []
tt = []
while True:
    dau_vao = raw_input("Nhap so: ")
    if dau_vao == '1':
        ten = raw_input("Nhap ten may: ")
        ram = raw_input("Nhap ram: ")
        tt = [ten,ram]
        a.append(tt)
    elif dau_vao == '2':
        print "Qua trinh xoa may"
        xoa = int(raw_input("Nhap chi so may ao: "))
        a.pop(xoa)
        print "May ao con lai:"
        a
    elif dau_vao == '3':
        print "Qua trinh thay doi cau hinh"
    elif dau_vao == 'p':
        print a
    elif dau_vao == 'q':
        exit()
    else:
        print "Ban da nhap sai, hay nhap dung theo yeu cau cua dau bai"

        
        
        