def in_ngay_thang(input):
	thang = int(input)
	if thang == 1:
		ngay = 31
	if thang == 2:
		ngay = 28
	if thang == 3:
		ngay = 31
	if thang == 4:
		ngay = 30
	if thang == 5:
		ngay = 31 
	if thang == 6:
		ngay = 30 
	if thang == 7:
		ngay = 31 
	if thang == 8:
		ngay = 31 
	if thang == 9:
		ngay = 30 
	if thang == 10:
		ngay = 31
	if thang == 11:
		ngay = 30 
	if thang == 12:
		ngay = 31

	return ngay

input = raw_input('nhap thang >')
ngay = in_ngay_thang(input)
print "So ngay trong thang la: %d"%(ngay)
	