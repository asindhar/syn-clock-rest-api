import requests, subprocess

def syncTime():
	#Api url to fetch date string from server
	api_url = 'http://localhost:5000/'

	#accepted format of date is month:day:hour:min:year.sec
	res = requests.get(api_url).json()
	return res['dt']


if __name__ == '__main__':
	#Get time from server
	res = syncTime()
	#Run sudo command date for changing client time
	subprocess.run(["sudo","date", res])
