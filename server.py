from flask import Flask
from flask_restful import Resource, Api
import datetime

app = Flask(__name__)
api = Api(app)

class serverTime(Resource):
	def get(self):
		#get server time
		dt = datetime.datetime.now()
		
		return {'dt': str(dt)}, 200
		
api.add_resource(serverTime, '/')

if __name__ == '__main__':
	##### To deploy on localhost #####
	#app.run()

	###### To deploy on your machine ip address ####
	#app.run('YOUR_IP_ADDRESS')
	app.run()