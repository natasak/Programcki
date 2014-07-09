import time
from datetime import date, datetime, time

def age_score(age):
	if age < 20:
		return 1
	elif age < 30:
		return 2
	else:
		return 3

def nova_funk(age):
	return age_score(age)

def friendsFB(friends):
	if friends < 100:
		return 1
	elif friends < 200:
		return 2
	elif friends < 300:
		return 3
	else:
		return 4

def calculate_complexity(p1, p2):
	return age_score(p1) + friendsFB(p2)


curr_time = date.today() # datum danasnji
trenutno = datetime.now() # danasnji datum in ura
#job = ["loving it", "hating it", "dont know"]

temperature = 26.3
internet = 4

complexity = 0


age = int(input("Koliko si stara?"))
#print age_score(age)
#print nova_funk(age)
#complexity = complexity + age_score(age)
#print complexity
friends = int(input("Koliko imas FB prijateljev?"))
#print friendsFB(friends)

print "Moj rezultat kompliciranosti zivljenja je: %d" % calculate_complexity(age, friends)

#if age < 30:
#	complexity = complexity + 20
#	print "Stara rosnih %d let. Tvoj complexity score je: %d." % age %complexity
#else:
#	complexity = complexity

#print "Stara sem %d let." % age

#deadlines = raw_input("Imas rok, ki se hitro bliza?")
#if deadlines == "ja":
#	deadlines = True
#else:
#	deadlines = False
#print deadlines

#num_missed = int(input("Koliko busev si zamudila?"))
#print "Zamudila sem %d busev." % num_missed

#print "Danes smo naslednjega datuma:"
#print curr_time
#print "Ura pa je:"
#print trenutno

#money = float(input("Koliko imas evrov?"))
#print "Imam %f evrov." % money

#job = []
#print "Napisi tri moznosti o priljubljenosti sluzbe: "
#for i in range(3):
#	a = raw_input(">  ")
#	job.append(a)

#print job


#family = int(input("Koliko sorodnikov imas?"))
#print "Imam %d sorodnikov." % family


#print job
#print job[0]
#print temperature
#print deadlines
#print not deadlines
#print curr_time