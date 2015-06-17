while True:
    print '-------MENU-------'
    print '1 Create Instances'
    print '2 Delete Instances'
    print '3 Change Instances'
    print 'q Quit            '
    print '------------------'
    s = raw_input('nhap so can chon: ')
    if s == '1':
        print 'Tao may ao ---------------------------------'
        print '--------------------------------------------'
    elif s == '2':
        print 'Xoa may ao ---------------------------------'
        print '--------------------------------------------'
    elif s == '3':
        print 'Sua may ao ---------------------------------'
        print '--------------------------------------------'
    elif s == 'q':
        break
    else:
        print '######## Khong hop le ##########'