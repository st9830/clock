import time

def timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Time remaining: {remaining_time} seconds", end="\r")
        time.sleep(1)
    print("Time's up!")

if __name__ == '__main__':
    timer(60)
