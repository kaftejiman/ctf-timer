#!/usr/bin/python3

import sys
import time
from datetime import datetime, timedelta
import calendar
from os.path import expanduser

PATH = expanduser("~")

def createFile(hoursRemaining):
	with open("{}/.ctftimer".format(PATH),"w") as f:
		f.write("{}".format(hoursRemaining))
	with open("{}/.ctftimer-temp".format(PATH),"w") as temp:
		future = datetime.utcnow() + timedelta(hours=int(hoursRemaining,10))
		temp.write("{}".format(calendar.timegm(future.timetuple())))

def decTimer():
	with open('{}/.ctftimer'.format(PATH),'r') as f:
		with open('{}/.ctftimer-temp'.format(PATH),'r') as temp:
			ts = int(temp.read(),10)
			now = time.time()
		if (now < ts):
			with open('{}/.ctftimer'.format(PATH),'w') as out:
				remain = datetime.fromtimestamp(ts) - datetime.now()
				out.write("{:.0f}".format(remain.total_seconds()/3600))
		elif now>ts:
			with open('{}/.ctftimer'.format(PATH),'w') as out:
				out.write("0")
if __name__ == "__main__":
	# if given parameter instantiate .ctftimer file with parameter as value
	if (len(sys.argv) >= 2):
		hours = sys.argv[1]
		createFile(hours)
	# otherwise decrement timer
	else:
		decTimer()
	
