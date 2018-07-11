import schedule
import time
import remotework
import new_db
import static_script

def run_scripts():
	execfile('static_script.py')
	execfile('bearfounders.py')

schedule.every().day.at("20:50").do(run_scripts)

while True:
    schedule.run_pending()
    time.sleep(1)