import schedule
import time
import remotework
import new_db
import static_script
import bearfounders
import secret

def run_static():
	execfile('static_script.py')
	
def run_dynamic():
	execfile('bearfounders.py')

schedule.every().day.at("11:55").do(run_static)
schedule.every().day.at("11:59").do(run_dynamic)

while True:
    schedule.run_pending()
    time.sleep(1)