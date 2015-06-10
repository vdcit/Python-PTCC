g = 24.95 #Gia tien moi cuon sach bandau
'''So tien phai tra khi mua 60 quyen sach va duoc giam gia 40% 1 quyen la'''
s = 60*24.95*(60.0/100)
'''Tien van chuyen la 3$ cho quyen dau tien va 0.75$ cho quyen 59 quyen tiep theo'''
t = 3 + 59*0.75
ts = t + s #Tong so tien phai tra

print "Tong so tien phai tra khi mua 60 cuon sach la", ts ,"$"