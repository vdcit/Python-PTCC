lst_name = []
for i in range(0, 10):
    name = raw_input('nhap ten: ')
    lst_name.append(name)
#print lst_name
dic = {}
for name in lst_name:
    if name in dic:
        dic[name] +=1
    else:
        dic[name] = 1
#    print dic
for name in dic:
    print 'ten ', name, 'xuat hien ', dic[name], 'lan'
        
    
