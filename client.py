import requests, subprocess
from datetime import datetime

def syncTime():
	#Api url to fetch date string from server
	api_url = 'http://localhost:5000/'

	#Start timer for RTT
	t1 = datetime.now()

	#Get data from api endpoint
	#accepted format of date is month:day:hour:min:year.sec
	res = requests.get(api_url).json()
	
	#Stop timer for RTT
	t2 = datetime.now()
	RTT = (t2 - t1) / 2
	
	print("Date-Time received from server: ", res['dt'])
	print("RTT: ", RTT)

	#Add RTT to server time
	dt = datetime.strptime(res['dt'], '%Y-%m-%d %H:%M:%S.%f') + RTT
	print("Date-Time with RTT: ", dt)

	#format the date object to a string - month:day:hour:min:year.sec 
	#ex 0206180219.59
	# Unix date command only change time upto seconds level
	dt_str = dt.strftime('%m%d%H%M%y.%S')
	
	return dt_str


if __name__ == '__main__':
	#Get time from server
	res = syncTime()
	#Run sudo command date for changing client time
	subprocess.run(["sudo","date", res])
