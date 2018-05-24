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
	#am = day + " 15:00:00+00"
	#pm = day +" 23:00:00+00"
	hours = range(7,21) # check hours from 7 am to 8pm incl.
	
	# array for extracted Forecast objects
	# fc_arr = [None, None, None]
	
	response = ""
	response_end = " at these hours: "
	will_rain = False
	will_rain_commute_am = False
	will_rain_commute_pm = False
	
	for x in range(0, len(owm_obs)):
		# extract Forecast object
		# fc_arr[x] = owm_obs[x].get_forecast()
		
		for hour in hours:
			time = day + " " + hour + ":00:00+00"	
			if owm_obs[x].will_be_rainy_at(time):
				response_end = response_end + hour +":00 " 
				will_rain = True
				if hour < 9:
					will_rain_commute_am = True
				if hour > 16:
					will_rain_commute_pm = True
	
	if will_rain and (not will_rain_commute_am or not will_rain_commute_pm):
		response = ":| Be careful, rain forecast outside commute " + response_end
	elif will_rain and (will_rain_commute_am or will_rain_commute_pm):
		response = ":( Rain forecast during"
		if will_rain_commute_am and will_rain_commute_pm:
			response = response " morning and afternoon"
		elif will_rain_commute_am:
			response = response + " morning"
		elif will_rain_commute_pm:
			response = response + " afternoon"
		response = response + " commute, specifically " + response_end
	else:
		response = ":) No rain forecast for today"
	

	return response
