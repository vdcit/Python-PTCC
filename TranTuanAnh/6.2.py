def print_str():
    print "\n~----------------~"
    print "|      Menu      |"
    print "~----------------~"
    print "| 1. Tao may ao  |"
    print "~----------------~"
    print "| 2. Xoa may ao  |"
    print "~----------------~"
    print "| 3. Show may ao |"
    print "~----------------~"
    print "| Nhan q de thoat|"
    print "~----------------~\n"
    print "="*18
instaces_lst = []

def check_ins(name):
    '''
    Return True if instace is exist
    '''
    for i in instaces_lst:
        if i['Ten'] == name:
            return True
    return False
    
def add_ins(name, ram, cpu):
    '''
    Add a instance
    '''
    if check_ins(name) is True:
        print '\nMay ao da ton tai'
    else:
        instaces_lst.append({'Ten': name, 'RAM': ram, 'CPU': cpu})
        print "\nTao may ao thanh cong!\n"

def del_ins(name):
    '''
    Delete a instance
    '''
    if check_ins(name) is True:
        for i in instaces_lst:
            if i['Ten'] == name:
                instaces_lst.remove(i)
                print '\nXoa may ao thanh cong'
    else:
        print '\nMay ao khong ton tai'

def show_instance():
    '''
    List all instance
    '''
    for i in range(len(instaces_lst)):
        print '\nMay ao', i+1
        print 'Ten:', instaces_lst[i]['Ten']
        print 'RAM:', instaces_lst[i]['RAM']
        print 'CPU:', instaces_lst[i]['CPU']

def manage():
    '''
    Manage instaces
    '''
    while True:
        print_str()
        n = raw_input('\nTuy chon chuc nang (1 ,2 ,3): ')
        if n == '':
            print "\nHay nhap vao 1, 2, 3, hoac 'q'!\n"
        elif n == 'q':
            import sys
            sys.exit()
        elif n == '1':
            print '\nNhap thong tin may ao: \n'
            name = raw_input('Ten: ')
            ram = raw_input('RAM: ')
            cpu = raw_input('CPU: ')
            add_ins(name, ram, cpu)
        elif n == '2':
            name = raw_input("Ten may ao muon xoa: ")
            del_ins(name)
        elif n == '3':
            if len(instaces_lst) != 0:
                print '\nThong tin cac may ao trong he thong:\n'
                show_instance()
            else:
                print '\nHe thong chua co may ao'
        else:
            print '\nBan da nhap sai. Hay nhap lai!\n'
    
manage()

