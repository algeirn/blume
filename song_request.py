import logging
import webbrowser, threading

artist = str(input('Which artist are you looking for ? '))
search = str(input('What song of ' + artist + ' are you looking for ? (format word1+word2) '))

def run():
  url = "https://www.youtube.com/results?search_query=" + artist + '+' + song
  logging.info("Starting browser at")
  threading.Timer(1.25, lambda: webbrowser.open_new(url)).start()
  
def search(artist, song):
  run()
  
search(artist, song)
