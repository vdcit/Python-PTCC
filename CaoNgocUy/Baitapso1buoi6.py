print "Ban dang xem bai tap buoi 5 cua UyCN"
print "Menu quan li may ao:"
nhap = True
all = []
import time

def list():
    for i in range(len(all)):
        print "****************"
        print "May ao", i + 0
        print "^^^^^^^^^"
        print "ten:", all[i][0]
        print "-----------"
        print "ram:", all[i][1]
        print "-------"
        print "cpu:", all[i][2]

def menu():
    print ("""
    _________ MENU _________
    - Nhan 1 de chon tao may ao.
    ----------------------------
    - Nhan 2 de chon xoa may ao.
    ----------------------------
    - Nhan 3 de chon thay doi may ao.
    ---------------------------------
    - Nhan 4 de hien thi danh sach may ao.
    --------------------------------------
    - Nhan q de chon thoat.
    -----------------------
    """)
    
def checkins(ten):
    for i in all:
        if i[0] == ten:
            return True
    return False

while nhap:
    print ("""
    _________ MENU _________
    - Nhan 1 de chon tao may ao.
    ----------------------------
    - Nhan 2 de chon xoa may ao.
    ----------------------------
    - Nhan 3 de chon thay doi may ao.
    ---------------------------------
    - Nhan 4 de hien thi danh sach may ao.
    --------------------------------------
    - Nhan q de chon thoat.
    -----------------------
    """)
    an = raw_input("Ban chon de thao tac voi may ao: ")
    
    if an == "1": 
        print("""\n Thanks :) Ban da chon tao may ao.""")
        print("""------------------------------------""")
        vm = []
        ten = raw_input("Nhap ten may ao: ")
        ram = raw_input("Nhap so Ram cho may ao: ")
        cpu = raw_input("Nhap so cpu cho may ao: ")
        if checkins(ten) is True:
            print """==== WARNING: May ao da ton tai ===="""
        else:
            vm.append(ten)
            vm.append(ram)
            vm.append(cpu)
            print ("""Executing ...""") 
            time.sleep(1)
            print ("""Done!!!""")
            all.append(vm)
            print ("""Quay lai menu. Loading ...""")
            time.sleep(1)
        
    elif an == "2":
        print("""Thanks :) Ban da chon xoa may ao. 
                 Danh sach may ao da tao. Loading ...""")
        time.sleep(2)
        if len(all) == 0:
            print """___Khong co may ao de xoa___"""
            print """----------------------------"""
            print """Quay lai menu chinh. Loading ..."""
            time.sleep(1)            
        else:
            print """Danh sach cac may ao da tao. Loading ..."""
            print """------------------------------------"""
            time.sleep(1)
            list()
            a = raw_input("Nhap ten may ao ban muon xoa: ")
            if checkins(ten) is True:
                for i in all:
                    if i[0] == a:
                        all.remove(i)
                        time.sleep(1)
                        print "Xoa may ao thanh cong"
                    else:
                        print "May ao khong ton tai"
                        list()
            
    elif an == "3":
        print("""Thanks :) Ban da chon thay doi may ao.""")
        print("""--------------------------------------""")
        if len(all) == 0:
            print ("""Khong tim thay may ao nao trong danh sach de thuc hien thay doi""")
            print ("""---------------------------------------------------------------""")
            print """Quay lai menu chinh. Loading..."""
            time.sleep(1)
        else:
            print """Danh sach cac may ao da tao. Loading ..."""
            print ("""---------------------------------------""")
            time.sleep(1)
            list()
            b = int(raw_input("Nhap so thu tu may ao ban muon thay doi: "))
            print """Thong so may ao muon thay doi"""
            print "************************"
            print "ten:", all[b][0]
            print "-----------"
            print "ram:", all[b][1]
            print "-------"
            print "cpu:", all[b][2]
            print "-------"
            cten = raw_input("Ten moi cua may ao: ")
            cram = raw_input("So ram moi cua may ao: ")
            ccpu = raw_input("So cpu moi cua may ao: ")
            all[b][0] = cten
            all[b][1] = cram
            all[b][2] = ccpu
            print "Sau khi thay doi thong so thi: "
            list()
            time.sleep(1)
            
    elif an == "4":
        print("""Danh sach may ao da tao""")
        print("""-----------------------""")
        if len(all) == 0:
            print """Khong co may ao nao"""
            print """-------------------"""
            print """Quay lai menu chinh. Loading..."""
            time.sleep(1)
        else:
            print """Danh sach cac may ao da tao. Loading ..."""
            print """----------------------------------------"""
            time.sleep(1)
            list()
            
    elif an == "q":
        print("""\n OMG - Ban da chon thoat. 
                    Tam biet!""")
        break
    else:
        print("""\n WARNING: Ban chon khong hop le, quay lai menu de chon.
                    Loading...""")
    
