may_ao = []
def tao_may_ao():
    ''' Day la ham tao may ao '''
    ten_may_ao = raw_input('nhap ten may ao:')
    ram = raw_input('RAM: ')
    cpu = raw_input('CPU: ')
    lst = [ten_may_ao, ram, cpu]
    may_ao.append(lst)
def show_may_ao():
    ''' Day la ham hien thi may ao '''
    print 'Danh sach may ao -------'
    for i in range(1, len(may_ao)+1):
        print '------------------------'
        print 'STT       :   ', i
        print 'Ten may ao:   ', may_ao[i-1][0]
        print 'RAM       :   ', may_ao[i-1][1]
        print 'CPU       :   ', may_ao[i-1][2]
        print '------------------------'
def xoa_may_ao():
    ''' Day la ham xoa may ao '''
    print 'Xoa may ao -------'
    try:
        stt = input('Nhap stt may ao muon xoa: ')
    except Exception as e:
        print 'Ban phai nhap vao la STT'
    if (stt in range(1, len(may_ao)+1)) is True:
        print 'Ban co chac muon xoa may ao: ', may_ao[stt-1][0]
        y = raw_input('Neu dong y xoa thi nhan phim y, khong thi nhan phim bat ky: ')
        if y == 'y':
            may_ao.pop(stt-1)
            print 'Da xoa thanh cong'
        else:
            print 'Ban da thoat'
    else:
        print 'Ban da nhap sai'
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