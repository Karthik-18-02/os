import os
pid = os.fork()

if pid > 0:
    print("Parent process")
    print("Parent process id is :", os.getpid())
    print("Child process id is :", pid)

else:
    print("Child process")
    print("Child process id is :", os.getpid())
    print("Parent process id is :", os.getpid())