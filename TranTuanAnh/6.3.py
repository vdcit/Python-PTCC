# dem so lan xuat hien cua cac tu trong 10 lan nhap:
result = []
temp = []
for i in range(10):
    result.append(raw_input('Nhap ten: '))
    if result[i] not in temp:
        temp.append(result[i])

for i in temp:
    print i, ':', result.count(i)