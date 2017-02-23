import pyowm

def weather_info(country) :

        owm = pyowm.OWM('d932beecc5bdc94b13445db97b2ea965')

        obs = owm.weather_at_place(country) 

        w = obs.get_weather()

        l = obs.get_location()

        forecast = {'date':w.get_reference_time(timeformat = 'iso').split(' ')[0],'weather':w.get_status(),'temp':str(w.get_temperature(unit='celsius')['temp']),'location':country.split('/')[0]}

        return forecast
