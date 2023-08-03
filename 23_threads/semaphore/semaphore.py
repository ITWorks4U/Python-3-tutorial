#!/usr/bin/python3

"""
	A semaphore represents a special case
	for multithreading. It's like a critical
	area, which allows up to n threads works
	with it at the same time.

	Imagine, you're with your car in front of a bridge.
	There's only space for one car. On the other side
	there're also cars. The semaphore might be a traffic
	light, which controls, on which side the cars may
	use the bridge, where the cars on the other side
	must wait before the traffic light turns from red to green.

	Typically, a semaphore allows only one
	thread at the certain time amount to work
	with anything. Since this thread is using
	this semaphore, every other thread must
	wait until the current thread has finished
	the job.

	The semaphore class requires an argument
	of 0 or higher. Don't use 0, because on runtime
	the first thread is waiting for eterinity
	to use the semaphore. Similar to the other threads.

	Unlike to the regular thread using, where's no guarantee,
	which thread is now running, with the semaphore the threads
	are running in the expected order.
"""

from time import sleep
from random import random
from threading import Thread, Semaphore

def task(semaphore, number) -> None:
	with semaphore:
		value = random()
		sleep(value)

		print(f'thread #{number} has got the value {value}')
	#end with
#end function

if __name__ == '__main__':
	#	define, how much threads are allowed
	#	to use the critical object
	s = Semaphore(1)

	for i in range(10):
		worker = Thread(target=task, args=(s, i))
		worker.start()
	#end for
#end main