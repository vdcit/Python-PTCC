# Bai tap buoi 6 su dung dict de khai bao thong tin may ao
# Khai bao mot dict de luu cac thong tin ve may ao
dict = {}


def input_instance():
    ''' Function input instance '''
    name_instance = raw_input("Nhap may ten may ao: ")
    if name_instance not in dict:
        ram = raw_input("Thong so RAM: ")
        cpu = raw_input("Thong so CPU: ")
        dict[name_instance] = [ram, cpu]
    else:
        print "Ten may ao da ton tai !!!"
    
 
 
def delete_instance():
    ''' Function for delete instance '''
    name_instance = raw_input("Nhap ten may ao muon xoa: ")
    if name_instance in dict:
        dict.pop(name_instance)
        print "Hoan thanh viec xoa may ao"
    else:
        print "Ban nhap sai ten may ao"

        
def show_instance():
    ''' Function for show instance '''
    print " He thong dang co %d may ao" % len(dict)
    print "Thong tin cac may ao lan luot la: \n"
    for key in dict:
        print "======="
        print "Ten may: ",key
        print "Thong so Ram: ",dict[key][0]
        print "Thong so CPU: ",dict[key][1]

        
def change_instance():
    ''' Function for change information instance '''
    name_instance = raw_input("Nhap ten may ao muon xoa: ")
    if name_instance in dict:
        change_ram = raw_input("Nhap lai Ram: ")
        change_cpu = raw_input("Nhap lai CPU: ")
        dict[name_instance] = [change_ram, change_instance]
    else:
        print "Ten may ao khong co trong he thong !!!"


# Khai bao ham da xong !!! Bat dau thuc hien cac chuc nang

while True:
    print "\n~----------------~"
    print "|   Tuy chon     |"
    print "~----------------~"
    print "| 1. Tao may ao  |"
    print "~----------------~"
    print "| 2. Xoa may ao  |"
    print "~----------------~"
    print "| 3. Thay doi    |"
    print "~---------------~|"
    print "| 4. Hien thi    |"
    print "~----------------~"
    print "| Nhan q de thoat|"
    print "~----------------~\n"  
    print "*"*10
    input = raw_input("Nhap tuy chon: ")
    if input == '1':
        input_instance()
    elif input == '2':
        delete_instance()
    elif input == '4':
        show_instance()
        print "*"*10
    elif input == '3':
        change_instance()
    elif input == 'q':
        break
    else:
        print "Nhap sai tuy chon !!!"
    
        
            