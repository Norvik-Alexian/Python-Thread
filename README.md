## Synchronous and Asynchronous
* Synchronous are operations that can be executed sequentially.
* Asynchronous are operations that can be executed in parallel.

## Concurrency and Parallelism
* `Concurrency`: parallel execution performed by one executor
* `Parallelism`: parallel execution performed by multiple executors

## Thread
* `Thread` is mechanism of parallel programming that have parent process, that shares memory with other threads of parent process.
* Each thread can start a new execution flow.
* All threads that are children of specific process can be executed only on one CPU. Thus, usually processes are better
for CPU-bound tasks, for IO-bound task usually perfer threads or other asynchronous programming mechanisms.

## GIL
GIL (Global Interpreter Lock) is part of CPython. GIL locks the Parallelism allows, to run in parallel only 1 thread
(done for simplifying work with memory and C-programs integration)

## CPU-bound and IO-bound
* CPU-bound tasks are the ones that use CPU
* IO-bound tasks are the ones that are using input/output streams (files, databases, console, etc.)

## Parallel Threads
If we run multiple CPU-bound threads on CPython, we will make the process slower as only one thread can execute according
to GIL and also that will require extra resources to switch between threads.

If we run multiple threads that are mostly IO-bound, we will make the process faster as when threads waits for IO response
from OS it releases GIL and the other thread can be executed.

## Thread Class:
* threading.Thread class is responsible for creation, control and monitoring of threads.
* Thread can be created based on function or inheriting Thread class and overriding run() method.
* To create based on function we should pass target parameter during creation.
* Threads are not started automatically, to start them we should call start() method.

## Join()
Threads have join() method that allows to wait for their execution.

## is_alive()
This method allows, to check if thread is in progress.

## Daemon Threads
* Python program will work until all the not-Daemon threads will finish the execution.
* To create a daemon-thread we can pass daemon=True argument to thread

## Threads Synchronization
Threads synchronization is a mechanism that protects a memory resource from parallel modification by several threads at
the same time. (threads share memory)

## Mutex
* Mutext means Mutual Exclusion
* It means that at a given specific time, only one thread can use a particular resource.
* If one program has multi-threads, then mutual exclusion restricts the treads to use that particular resource simultaneously.
It locks the other threads and restricts their entry into the critical section.
* We can use Lock mutex.

## Lock Object:
* Lock object can have 2 states: locked and released.
* Lock object has 2 main methods: acquire() and release()
* Running acquire() on released Lock makes it locked.
* If threads calls acquire() on locked Lock, it will froz until some other thread will call release() on that Lock object.
* Calling release() on released object generates RuntimeError.

## Lock Acquire()
* acquire(blocking=True, timeout=-1)
* Returns True when acquiring Lock successfully
* `blocking`: if True then calling on locked object will stop the thread execution and returns True.
* `timeout`: Lock timeout (how long the threads will be blocked)

## Lock status checking
* locked() returns True if Lock is acquired, otherwise False.

## Lock Object Usage Interface
It's better to make sure that lock will be released at the end, for that we can either use place in finally block lock.release()
or use with statement that automatically releases the Lock.

## Disadvantages of locks
* Locks affect the performance as locking and releasing consumes resources and time.
* Locks can cause deadlocks

## Deadlock
* Deadlock is a situation when threads can continuously wait each other.

## Re-entracy
A code is re-entrant if it can be safely called again. In other words, re-entrant code can be called more than once,
even though called by different threads, it still works correctly. So, the re-entrant section of code usually use local
variables only in such a way that each and every call to the code gets its own copy of data.

Non-reentrant code (if 2 concurrent threads will access val, the result will be dependent on their execution time)

## RLock
* `RLock`: re-entrant Lock
* It's like lock, but some differences
* RLock can be released only by the thread that acqquired it (unlike Lock)
* RLock supports nested locking, so the thread can acquire the lock again.
* RLock is useful in situation where it's not easy to keep track of whether you've already grabbed a lock.

## Queue
* `Queue`: is thread-safe collection of objects

## Semaphore
* Semaphore object has counter
* Running acquire() counter is decreased by 1
* Running release() counter is increased by 1
* Counter value can't be below 0
* If acquire() is called when counter equals to 0, then thread is locked until release() is called
* Semaphore are useful when we have resource with limitation of number of parallel handling.

## BoundedSemaphore
BoundedSemaphore also checks if the counter values is not greater than specified value.

## Condition Variable
