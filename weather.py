from pyowm import OWM
import datetime
from secrets import get_API_KEY
#from weather import Weather

OWM_API_KEY = get_API_KEY()
owm = OWM(OWM_API_KEY)

now = datetime.datetime.now()

def get_weather():
	owm_obs = [None, None, None]
	owm_obs[0] = owm.three_hours_forecast('Leiden,NL')
	owm_obs[1] = owm.three_hours_forecast('Katwijk Aan Zee,NL')
	owm_obs[2] = owm.three_hours_forecast('Rijnsburg, NL')
	
	will_rain = False

	for x in range(0, len(owm_obs)):
		day = now.strftime("%Y-%m-%d")
		am = day + " 07:30:00+00"
		pm = day +" 16:30:00+00"
		if owm_obs[x].will_be_rainy_at(am) or owm_obs[x].will_be_rainy_at(pm):
			will_rain = True

	print str(will_rain)

#def weather_msg():
#	response = get_weather()
#	return response

get_weather()
