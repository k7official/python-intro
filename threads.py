import threading


class MusaMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().name)


x = MusaMessenger(name='Send out messages')
y = MusaMessenger(name='Receive messages')
x.start()
y.start()
