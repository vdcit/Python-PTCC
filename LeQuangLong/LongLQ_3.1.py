import math

data = raw_input('Nhap ban kinh:> ')
while True:
    try:
        number = float(data)
    except ValueError:
        data = raw_input('Nhap so:> ')
    else:
    	print "The tich hinh cau ban kinh %2.2f la: %2.3f" %(number, math.pi * number ** 3 * 4.0/3.0)
    	break