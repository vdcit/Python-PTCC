def ve_hinh():
    print "+ - - -- - -  + - - - - - -+ - - - - - - - + - - - - - - - +"
    print "|     1       |      2     |       3       |       q       |"
    print "+ - - -- - -  + - - - - - -+ - - - - - - - + - - - - - - - +"
    print "|  Tao may ao | Xoa may ao | Doi cau hinh  |     Thoat     |"
    print "+ - - -- - -  + - - - - - -+ - - - - - - - + - - - - - - - +"
    

def action(input):
 #   result = ''
    while input != 'q':
        if input == '1':
            result = "Tao may ao thanh cong"
            break
        elif input == '2':
            result = "Xoa may ao thanh cong"
            break
        elif input == '3':
            result = "Doi cau hinh thanh cong"
            break
        else:
            input = raw_input('Yeu cau nhap lai > ')
    else:
        exit()
    return result

ve_hinh()

input = raw_input('Nhap tuy chon > ')
print action(input)

