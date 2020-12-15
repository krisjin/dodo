import threading
from time import sleep
result = "Not Set"
lock = threading.Lock()
def map_func(x):
    sleep(100)
    raise Exception("Task should have been cancelled")
def start_job(x):
    global result
    try:
        sc.setJobGroup("job_to_cancel", "some description")
        result = sc.parallelize(range(x)).map(map_func).collect()
    except Exception as e:
        result = "Cancelled"
    lock.release()
def stop_job():
    sleep(5)
    sc.cancelJobGroup("job_to_cancel")
suppress = lock.acquire()
suppress = threading.Thread(target=start_job, args=(10,)).start()
suppress = threading.Thread(target=stop_job).start()
suppress = lock.acquire()
print(result)
