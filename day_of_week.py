def day_of_week(yyyy,mm,dd):
	weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
	month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
	c = (yyyy - yyyy % 100) / 100
	y = yyyy % 100
	m = (mm + 9) % 12 + 1
	if m == 11 or m == 12:
		y -= 1
	return weekday[int((dd + int(2.6*m-0.2)-2*c+y+int(y/4)+int(c/4)) % 7)] + ", " + month[mm-1] + " " + str(dd).zfill(2) + ", " + str(yyyy)

print(day_of_week(2022,2,7))