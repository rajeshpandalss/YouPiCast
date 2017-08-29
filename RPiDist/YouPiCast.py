from flask import Flask							
import os
from threading import Thread

app=Flask(__name__)

def run(cmdStr):
	os.system(cmdStr)

@app.route('/yt/<url>')
def PlayNow(url):
	pid = os.system('$(pidof omxplayer)')
	if pid > 0:
		os.system('killall omxplayer.bin')
	modUrl = 'https://youtube.com/watch?v='+url
	cmdStr = 'omxplayer -o hdmi `youtube-dl -g -f 18 %s` --blank' % (modUrl)
	threads = Thread(target=run,args=(cmdStr,))
	threads.daemon = True
	threads.start()
	return 'Added : Url - ' + url

@app.route('/kill')
def Kill():
	pid = os.system('$(pidof omxplayer)')
	if pid > 0:
		os.system('killall omxplayer.bin')
	return 'Killed'


if __name__ == '__main__':
	app.run(host='0.0.0.0')
