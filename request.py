import requests
import concurrent.futures
import threading
import time


def func(n):
    print(n)
    f = open("test.txt","a+")
    f.write("%d \n" %n)
    f.close
    """
    do_run=True
    execution_count=5
    while do_run:
        execution_count -=1
        print(execution_count)
        if(execution_count <=0):
            do_run = false
    
"""
if __name__ == "__main__":
    start_time=time.time()
    numbers=[1,2]*30
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(func,numbers)
    duration = time.time() -start_time
    print(duration)
"""thread_local = threading.local()
print(thread_local)
print( hasattr(thread_local,"session"))
if not hasattr(thread_local,"session"):
    thread_local.session = requests.Session()
    print( hasattr(thread_local,"session"))
    print(requests.Session())
    print(thread_local.session)
    print(thread_local.session.get("http://192.168.1.90:4200"))"""
"""print (requests.get("http://192.168.1.90:4200", headers={'Host': 'example.com'}))
print (requests.get("http://192.168.1.72:", headers={'Host': 'example.com'}))
print(requests.Session())
f = open("test.txt","w")
f.write("\r\n" )
f.close()"""
