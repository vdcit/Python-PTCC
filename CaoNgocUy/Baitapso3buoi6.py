print "Cac ban dang xem bai tap so 2 cua UyCN"
print "Viet chuong trinh dem so lan suat hien cua cac tu trong 10 lan nhap"
nhap = []
for i in range(0, 10):
    ten = raw_input("Nhap tu: ")
    nhap.append(ten)   
print "Cac tu ban da nhap la: "
print nhap
d = {}
for tu in nhap:
    if tu in d:
        d[tu] = d[tu] + 1
    else:
        d[tu] = 1
print "So luong cac tu ban da nhap nhu sau: ", d       