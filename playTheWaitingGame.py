# Challenge 
# waiting_game() Player has to hit enter after the exact time shown by the computer 

import time 
import random 

def waiting_game():
    target = random.randint(2, 6) # target second to wait
    print(f'\nYour target time is {target} seconds')
    
    input(" ---Press Enter to Begin--- ")
    start = time.perf_counter()
    
    input(f"\n...Press enter again after {target} seconds...")
    elapsed = time.perf_counter() - start
    
    print(f"\nElapsed time: {elapsed :.3f} seconds")
    if elapsed == target:
        print("(Unbelievable! Perfect timing!)")
    elif elapsed < target:
        print(f"({target - elapsed :.3f} seconds too fast)")
    else:
        print(f"({elapsed - target :.3f} seconds too slow)")
        
waiting_game()