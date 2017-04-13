import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(2000):
            print(threading.currentThread().getName())

x = Messenger(name="the 1st thread")
y = Messenger(name="the 2nd thread")
x.start()
y.start()            