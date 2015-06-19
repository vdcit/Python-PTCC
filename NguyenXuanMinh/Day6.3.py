may_ao = {}
def tao_may_ao():
    ''' Day la ham tao may ao '''
    ten_may_ao = raw_input('nhap ten may ao:')
    ram = raw_input('RAM: ')
    cpu = raw_input('CPU: ')
    lst = [ten_may_ao, ram, cpu]
    may_ao[ten_may_ao] = lst
def show_may_ao():
    ''' Day la ham hien thi may ao '''
    print 'Danh sach may ao -------'
    for key in may_ao:
        print '------------------------'
        print 'Ten may ao:   ', may_ao[key][0]
        print 'RAM       :   ', may_ao[key][1]
        print 'CPU       :   ', may_ao[key][2]
        print '------------------------'
def xoa_may_ao():
    ''' Day la ham xoa may ao '''
    print 'Xoa may ao -------'
    name = raw_input('Nhap ten may ao muon xoa: ')
    if (name in may_ao) is True:
        print 'Ban co chac muon xoa may ao: ', may_ao[name][0]
        y = raw_input('Neu dong y xoa thi nhan phim y, khong thi nhan phim bat ky: ')
        if y == 'y':
            may_ao.pop(name)
            print 'Da xoa thanh cong'
        else:
            print 'thoat'
    else:
        print 'Ban da nhap sai ten'
while True:
    print '-------MENU-------'
    print '1 Create Instances'
    print '2 Show Instances  '
    print '3 Delete Instances'
    print 'q Quit            '
    print '------------------'
    s = raw_input('nhap so can chon: ')
    if s == '1':
        tao_may_ao()
    elif s == '2':
        show_may_ao()
    elif s == '3':
        xoa_may_ao()
    elif s == 'q':
        break
    else:
        print '######## Khong hop le ##########'