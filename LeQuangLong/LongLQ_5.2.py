def in_ngay_thang(input):
	while input != 'q':
		thang = int(input)
		if thang == 1 or thang == 3 or thang == 5:
			ngay = 31
		elif thang == 2:
			ngay = 28
		else:
			ngay = 30
		return ngay
	else:
		exit()

	

input = raw_input('nhap thang >')
ngay = in_ngay_thang(input)
print "So ngay trong thang la: %d"%(ngay)
	