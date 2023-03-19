import time
import requests
import pyfiglet as pg
import subprocess as sb
from colored import fg,bg
from bs4 import BeautifulSoup
# tool logo
color = fg('green')
Text=pg.figlet_format('WEB\n SCRAPING',font='standard')
print (color+Text)
# warning
color = fg('yellow')
print(color+'*****************************************************************')
print (color+'=>Information:You can use this program to work with scraping web.')
print(color+'*****************************************************************')
#Options
color = bg('white')
colors = fg('black')
print (colors+color+'    1.scraping                                                   ')
print (colors+color+'    2.pings                                                      ')
print (colors+color+'    3.ip                                                         ')
print (colors+color+'    4.exit                                                       ')

# Input
color = bg('red')
colors= fg('black')
Bot=int(input(colors+color+'##Apply These Methods:-'))
if Bot == 1