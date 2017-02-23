import weather, music, display, threading
import sys, getch, os
from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import sys, pygame
import termios
import fcntl
import smbus
import time
import weather

def main():
  number = 0
  #lcd_init()
  th_flag = False
  display_update = False
  index = 0
  w = weather.weather_info("seoul")
  music_thread = music.MusicThread()
  music_thread.start()

  display_on = display.Display()
  weather_list = [w['date'], w['temp'], w['location'], w['weather']]
  music_list = ['None', 'None']
  display_on.set_info(weather_list, music_list)
  display_on.start()
  
  print("start loop")
  while True:
	number = getch.getch()
    	#print(number)
    	
      	if(number == '1'):
          display_update = True
          w = weather.weather_info("seoul")
            
        elif(number == '2'):
          display_update = True
          w = weather.weather_info("london")

        elif(number == '3'):
          display_update = True
          w = weather.weather_info("newyork")

        elif(number == 'a'):
          index = 0
          display_update = True
          th_flag = not th_flag
          music_thread.push_power_switch()
        elif(number == '4'):
          music_thread.pause()
        elif(number == '5'):
          music_thread.unpause()
        elif(number == 'b'):
          index = index+1
          display_update = True
          music_thread.play_next_music()
        elif(number == 'p'):
          music_thread.volume_up()
        elif(number == '-'):
          music_thread.volume_down()
        elif(number == '8'):
          music_thread.exit()
          display_on.exit()
       	  exit()

        if(display_update == True):
          print("display update...")
          weather_list = [w['date'], w['temp'], w['location'], w['weather']]
          music_list = music_thread.get_current_info(index%3)
          display_on.set_info(weather_list, music_list)

       	display_update = False

          
if __name__ == '__main__':

    main()

