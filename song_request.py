# once pip install pynput done and pip install pywhatkit
import pywhatkit
import logging
import webbrowser, threading
from pynput.keyboard import Key, Controller

song = str(input("What song are you looking for ? "))
keyboard = Controller()

def select_searchbar():
  keyboard.press(Key.tab)
  keyboard.release(Key.tab)

def run():
  url = "https://www.youtube.com/"
  logging.info("Starting browser at")
  threading.Timer(1.25, lambda: webbrowser.open_new(url)).start()
  for select_searchbar() in range(4):
    select_searchbar()  
  keyboard.type(song)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  
def search(song):
  run()
  
search(song)

# command = input("Enter your song : ")
# pywhatkit.playonyt(command)
