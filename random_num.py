import random
import time
from ubidots import ApiClient

api = ApiClient(token='BBFF-JpZNxID9deZz3frfDC3hL83oH88YD5')
variable = api.get_variable('5d7a60b01d847267550608df')
while(1):
	x=random.randint(1,100)
	response = variable.save_value({"value":x})
	print "\nThe random number sent to IoT dashboard is "+str(x)
	time.sleep(0.1)