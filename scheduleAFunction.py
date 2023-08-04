# Challenge 
# Write a Python function to schedule another given function to execute at 
# a specified time.

import sched 
import time 

def schedule_function(event_time, function, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(event_time, 1, function, argument=args)
    print(f"{function.__name__}()scheduled for {time.asctime(time.localtime(event_time))}")
    s.run()
    
schedule_function(time.time() + 10, print, "hello")