import threading
import time
 
class MyThread(threading.Thread):
 
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
 
    def run(self):
        print("Starting {0} at {1} \n".format(self.name, time.ctime(time.time())))
        self.do_stuff()
 
    def do_stuff(self):
        do_run=True
        execution_count = 5
        while do_run:
            execution_count -= 1
            time.sleep(self.thread_id * 2)
            print("{0}: {1}. Sleeping time: {2}".format(self.name, time.ctime(time.time()), self.thread_id * 2))
            if (execution_count <= 0):
                do_run = False
 
threads = []
number_threads = 2
for i in range(number_threads):
    t = MyThread(i, "Thread-{0}".format(i))
    t.start()
    threads.append(t)
 
for t in threads:
    t.join()
 
print("Exiting main thread")
