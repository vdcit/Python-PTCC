# Bai tap ve nha buoi 5 
# Author: Nguyen Hoai Name
print "An 1 de tao may ao\n\
An 2 de xoa may ao\n\
An 3 de thay doi cau hinh\n\
An 'q' de thoat chuong trinh"
while True:
    dau_vao = raw_input("Nhap so: ")
    if dau_vao == '1':
        print "Qua trinh tao may ao dang duoc thuc hien"
    elif dau_vao == '2':
        print "Qua trinh xoa may ao dang duoc thuc hien"
    elif dau_vao == '3':
        print "Qua trinh thay doi cau hinh"
    elif dau_vao == 'q':
        exit()
    else:
        print "Ban da nhap sai, hay nhap dung theo yeu cau cua dau bai"
