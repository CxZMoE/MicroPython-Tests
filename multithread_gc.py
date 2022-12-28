import gc, _thread
def foo():
  while True:
    time.sleep_ms(500)
    print(gc.mem_free())
    # if gc.mem_free() < 10000:
    gc.collect()

_thread.start_new_thread(foo,())
while True:
  print(str(128))