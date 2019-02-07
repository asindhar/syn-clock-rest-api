from flask import Flask
from flask_restful import Resource, Api
import datetime

app = Flask(__name__)
api = Api(app)

class serverTime(Resource):
	"""docstring for class"""
	def get(self):
		#get server time
		dt = datetime.datetime.now()
		#format the date object to a string - month:day:hour:min:year.sec 
		#ex 0206180219.59
		dt_str = dt.strftime('%m%d%H%M%y.%S')
		return {'dt': dt_str}, 200
		
api.add_resource(serverTime, '/')

if __name__ == '__main__':
	##### To deploy on localhost #####
	#app.run()

	###### To deploy on your machine ip address ####
	#app.run('YOUR_IP_ADDRESS')
	app.run()