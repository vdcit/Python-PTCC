print "Ban dang xem bai tap buoi 5 cua UyCN"
print "Menu quan li may ao:"
nhap = True
while nhap:
    print ("""
    - Nhan 1 de chon tao may ao.
    - Nhan 2 de chon xoa may ao.
    - Nhan 3 de chon thay doi may ao.
    - Nhan q de chon thoat.
    """)
    an = raw_input("Ban chon de thao tac voi may ao: ") 
    if an == "1": 
        print("""\n Thanks :) Ban da chon tao may ao. 
                    Executing ... Done!!!
                    Quay lai menu. Loading ...""") 
    elif an == "2":
        print("""\n Thanks :) Ban da chon xoa may ao. 
                    Executing ... Done!!!
                    Quay lai menu. Loading ...""") 
    elif an == "3":
        print("""\n Thanks :) Ban da chon thay doi may ao. 
                    Executing ... Done!!!
                    Quay lai menu. Loading ...""") 
    elif an == "q":
        print("""\n OMG - Ban da chon thoat. 
                    Tam biet!""")
        break
    else:
        print("""\n WARNING: Ban chon khong hop le, quay lai menu de chon.
                    Loading...""")
    
