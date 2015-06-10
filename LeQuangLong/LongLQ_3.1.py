import math

data = raw_input('Nhap ban kinh:> ')
while True:
    try:
        number = float(data)
    except ValueError:
        data = raw_input('Nhap so:> ')
    else:
    	print "The tich hinh cau ban kinh %2.2f la: %2.3f" %(number, 4/3 * math.pi * number ** 3)
    	break