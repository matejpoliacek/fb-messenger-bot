from pyowm import OWM
import datetime
import os
#from weather import Weather

owm = OWM(os.environ['OWM_API_KEY'])

now = datetime.datetime.now()

def get_weather():
	# collect Forecasters for each location
	owm_obs = [None, None, None]
	owm_obs[0] = owm.three_hours_forecast('Leiden,NL')
	owm_obs[1] = owm.three_hours_forecast('Katwijk Aan Zee,NL')
	owm_obs[2] = owm.three_hours_forecast('Rijnsburg, NL')
	
	# set up desired format
	day = now.strftime("%Y-%m-%d")
	am = day + " 16:00:00+00"
	pm = day +" 17:00:00+00"
	
	# array for extracted Forecast objects
	# fc_arr = [None, None, None]
	
	will_rain = False

	for x in range(0, len(owm_obs)):
		# extract Forecast object
		# fc_arr[x] = owm_obs[x].get_forecast()
		
		if owm_obs[x].will_be_rainy_at(am) or owm_obs[x].will_be_rainy_at(pm):
			will_rain = True

	return will_rain
