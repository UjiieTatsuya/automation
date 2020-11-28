
import datetime
import schedule
import time
import subprocess

def openGmail():
	subprocess.Popen(['open', '/Applications/Gmail.app'])

def startTask():
	subprocess.Popen(['open', '/Applications/Amazon Music.app'])
	subprocess.Popen(['open', '/Applications/AS Timer.app'])

# def shutdown():
# 	subprocess.run(('/sbin/shutdown', '-h', '1'))

Gmail = "12:00"
task = "09:00"
mindfulness = "22:00"
shutdown = "00:00"


schedule.every().day.at(Gmail).do(openGmail)
schedule.every().day.at(task).do(startTask)
schedule.every().day.at(mindfulness).do(startTask)
# schedule.every().day.at(shutdown).do(shutdown)

while True:
	schedule.run_pending()
	time.sleep(60)

