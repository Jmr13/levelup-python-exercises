import sched
import time

# Define a function to schedule another function to run at a specific time
def schedule_function(event_time, function, *args):
    # Create a scheduler object using time.time for current time and time.sleep for delay
    s = sched.scheduler(time.time, time.sleep)
    # Schedule the function to run at the absolute time `event_time` with priority 1 and arguments `args`
    s.enterabs(event_time, 1, function, argument=args)
    # Print a message indicating the function has been scheduled
    print(f"{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}")
    # Run the scheduler to execute the scheduled function
    s.run()

if __name__ == "__main__":
    # Schedule the built-in print function to run 1 second from now with the argument "Howdy!"
    schedule_function(time.time() + 1, print, "Howdy!", "How are you?")
