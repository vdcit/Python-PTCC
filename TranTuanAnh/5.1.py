def print_str():
    print "~----------------~"
    print "|      Menu      |"
    print "~----------------~"
    print "| 1. Tao may ao  |"
    print "~----------------~"
    print "| 2. Xoa may ao  |"
    print "~----------------~"
    print "| 3. Sua cau hinh|"
    print "~----------------~"
    print "| Nhan q de thoat|"
    print "~----------------~\n"

def control():
    while True:
        print_str()
        n = raw_input('Tuy chon chuc nang (1 ,2 ,3): ')
        if n == '':
            print "Hay nhap vao 1, 2, 3, hoac 'q'!\n"
            continue
        elif n == 'q':
            import sys
            sys.exit()
        elif n == '1':
            print "Tao may ao thanh cong!\n"
        elif n == '2':
            print "Xoa may ao thanh cong!\n"
        elif n == '3':
            print "Hoan tat sua cau hinh!\n"
        else:
            print 'Ban da nhap sai. Hay nhap lai!\n'
            continue
    
control()

