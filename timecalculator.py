def add_time(ftime,stime,oday=False):

	wd =  [
        'monday', 'tuesday',
        'wednesday', 'thursday',
        'friday', 'saturday',
        'sunday'
      ]

	#Limpiar tiempo

	h,m = ftime.split(":")
	m,p = m.split(" ")
	hs,ms = stime.split(":")

	h = int(h)
	m = int(m)
	hs = int(hs)
	ms = int(ms)

	#Calculo de tiempo bueno

	dh = h + hs
	dm = m + ms
	dd = 0

	#Calculo de mas horas por minutos

	if dm > 59:
		#print("------+60------")
		dh += round(dm / 60)
		dm -= (round(dm / 60) * 60)

	#Calculo de mas dias por horas
	if dh > 23:
		#print("------+24------")
		dd += round(dh / 24)
		dh -= (int(dh / 24) * 24)
	elif dh>11 and p == "PM":
		dd = 1
		dh -= (int(dh / 24) * 24)
		#print("nex")
	
	#Calculo del periodo
	if dh > 12:
		if p == "PM":
			dh -= 12
			p = "AM"
		else:
			dh -= 12
			p = "PM"

	elif dh == 12:
		if p == "PM":
			p = "AM"
		else:
			p = "PM"

	if dm < 10:
		dm = "0"+str(dm)
	else:
		dm = str(dm)

	dh = str(dh)
	p = str(p)

	sv = ""

	if oday != False:
		#print("---------WD--------")

		dw = wd.index(oday.lower())
		
		
		if (dw+dd)>(len(wd)-1):

			x = int(dd/7)
			z = dd-(x*7)
			y = (z+dw)

			if y>6:
				y-=7

			sv = (wd[y])
		
		else:
			sv = ( wd [(dw+dd)] )

		sv = str(sv)
		sv = sv.title()

		sv = ", " + sv #+ " "

	if dd == 0:
		r = dh+":"+dm+" "+p+sv
	elif dd == 1:
		r = dh+":"+dm+" "+p+sv+" (next day)"
	else:
		r = dh+":"+dm+" "+p+sv+" ("+str(dd)+" days later)"
	return (str(r))
