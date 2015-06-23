# Bai tap buoi 6
print """An 1 de tao may ao
An 2 de xoa may ao
An 3 de thay doi cau hinh
"""
def xoa_may_ao(d,key):
#''' Function de xoa may ao '''
    del d[key]
    return d
def hienthi(d):
#''' Ham dung de hien thi may ao '''
    for i in d:
        print "May ao ten ",i," co thong so lan luot la: ", d[i]
#def thaythe(key,value_change,dict):  
mayao = {}
nhap = raw_input("Nhap tuy chon: ")
if nhap == '1':
    while True:
        ten = raw_input("Nhap ten may: ")
        if ( ten in mayao ) == False:
            ram = raw_input("Nhap ram: ")
            cpu = raw_input("Nhap CPU: ")
            ocung = raw_input("Nhap thong so o cung: ")
            mayao[ten] = [ram, cpu, ocung]
        else:
            print "Ten may ao da ton tai. nhap lai"
            continue
        dung = raw_input("Nhap q de dung qua trinh nhap \n\
neu tiep tuc nhap enter")
        if dung == 'q':
            break
        
    print "Thong tin cac may tren he thong "
    hienthi(mayao)
nhap = raw_input("Ban co muon xoa may ao khong (yes/no): ")
if nhap == '2' or nhap == 'yes':
    while True:
        may_xoa = raw_input("Nhap ten may ao muon xoa: ")
        if ( may_xoa in mayao ) == True:
            xoa_may_ao( mayao, may_xoa )
        else:
            print "Ban nhap sai may ao. Nhap lai !!!"
            continue
        xong = raw_input("Nhap q de dung qua trinh xoa \n\
neu tiep tuc nhap enter")
        if xong == 'q':
            break
    print "May ao con lai sau khi xoa:"
    hienthi(mayao)
else:
    pass
nhap = raw_input("Ban co muon chinh sua may ao khong (yes/no): ")
if nhap == '3' or nhap == 'yes':
   while True:
        change = raw_input("Nhap ten may muon chinh sua: ")
        if ( change in mayao) == True:
            print ("Nhap lan luot cac thong so chinh sua cua may da chon:\n")
            ram = raw_input("Nhap ram: ")
            cpu = raw_input("Nhap cpu: ")
            ocung = raw_input("Nhap o cung: ")
            mayao[change] = [ram, cpu, ocung]
        xuoi = raw_input("Nhap 'q' de dung qua trinh chinh sua \n\
neu tiep tuc nhap enter")  
        if xuoi == 'q':
            break
   print "Thong tin danh sach may sau khi chinh sua: "
   hienthi(mayao)



    
     