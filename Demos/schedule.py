import schedule
import time
import remotework
import new_db
import static_script
import dynamic_script

def run_scripts():
	execfile('static_script.py')
	execfile('dyanamic_script.py')

schedule.every().day.at("20:50").do(run_scripts)