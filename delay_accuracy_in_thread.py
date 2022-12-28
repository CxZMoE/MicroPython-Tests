import _thread, time

def test():
    while True:
        print("Process: %d" % (time.ticks_ms()))
        time.sleep_ms(100)

_thread.start_new_thread(test, ())

while True:
    print(time.ticks_ms())
    time.sleep_ms(100)