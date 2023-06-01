import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time
from URL import *

url = ("https://www.google.com/search?rlz=1C1ONGR_enUS1000US1000&sxsrf=APwXEdew2Gku-ZAmXzNhQ8h_CHX48EJfhQ:1685602588298"
       "&q=cereal&tbm=isch&sa=X&ved=2ahUKEwiy6If8vqH_AhXMJ0QIHQfjCNUQ0pQJegQICBAB&biw=2560&bih=1297&dpr=1")
def image_searcher(query):
