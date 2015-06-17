while True:	
	print "Menu"
	print "Chon 1 de tao may ao"
	print "Chon 2 de xoa may ao"
	print "Chon 3 de thay doi cau hinh"
	print "Chon q de thoat"
	
	a= raw_input("Nhap tuy chon: ")
	if a=='q':
		exit()
	elif a == '1':
		print "BAN DA CHON MENU TAO MAY AO"
	elif a == '2':
		print "BAN DA CHON MENU XOA MAY AO"
	elif a == '3':
		print "BAN DA CHON THAY DOI CAU HINH MAY AO"
	else:
		print "BAN NHAP SAI, HAY NHAP LAI"